from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_redis import get_redis_connection
import json
from .models import Blog
from .serializers import BlogSerializer




class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        queryset = Blog.objects.all().order_by('-created_at')
        count = self.request.query_params.get('count')
        if count is not None:
            try:
                count = int(count)
                queryset = queryset[:count]
            except ValueError:
                pass
        return queryset

    def list(self, request, *args, **kwargs):
        redis_conn = get_redis_connection("default")
        cache_key = 'active_blogs_sorted_set'

        set_size = redis_conn.zcard(cache_key)
        if set_size > 0:
            print("Cache hit: using sorted_set from Redis.")
            cached_blogs = redis_conn.zrevrange(cache_key, 0, -1)
            serialized_blogs = [json.loads(item) for item in cached_blogs]
        else:
            print("Cache miss: querying database and populating sorted_set.")
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            serialized_blogs = serializer.data

            redis_conn.delete(cache_key)

            for blog in serialized_blogs:
                created_at_timestamp = (
                    Blog.objects.get(id=blog['id']).created_at.timestamp()
                )
                redis_conn.zadd(
                    cache_key,
                    {json.dumps(blog): created_at_timestamp}
                )

            redis_conn.expire(cache_key, 60 * 60)

        return Response(serialized_blogs)