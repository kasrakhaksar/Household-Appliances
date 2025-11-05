"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from api_shop.views import  SignupView
from product.views import ProductViewSet 
from blog.views import BlogViewSet
from newsletter.views import SubscriberViewSet
from django.conf.urls.static import static
import shop.settings
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="Shop API",
        default_version='v1',
        description="API documentation for the shop project",
    ),
    public=True,
    permission_classes=(IsAuthenticatedOrReadOnly,),
)

router = DefaultRouter()


router.register(r'product', ProductViewSet , basename='product')
router.register(r'blog', BlogViewSet , basename='blog')
router.register(r'subscribe', SubscriberViewSet , basename='subscribe')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('swagger(<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),




    path('', include(router.urls))
] + static(shop.settings.MEDIA_URL, document_root=shop.settings.MEDIA_ROOT)