from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer


class LastBlogViewSet(ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer

    @action(detail=False, methods=['get'])
    def latest(self, request):
        latest_blogs = self.queryset[:3]
        serializer = self.get_serializer(latest_blogs, many=True)
        return Response(serializer.data)