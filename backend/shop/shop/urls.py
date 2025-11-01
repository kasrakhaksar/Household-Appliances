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
from product.views import ProductViewSet , ProductCategoryListView , ProductSearchCategoryViewSet
from blog.views import BlogViewSet
from django.conf.urls.static import static
import shop.settings
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

router = DefaultRouter()


router.register(r'product', ProductViewSet , basename='product')
router.register(r'products/categories', ProductCategoryListView , basename='categories')
router.register(r'products/search', ProductSearchCategoryViewSet, basename='products-search')
router.register(r'blog', BlogViewSet , basename='blog')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))
] + static(shop.settings.MEDIA_URL, document_root=shop.settings.MEDIA_ROOT)
