"""
URL configuration for library_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', TemplateView.as_view(template_name='utils/index.html')),
    
    path('api/', include('books.urls', namespace='books')),
    path('api/', include('authors.urls', namespace='authors')),

    # User management
    path('api/user/', include('accounts.urls', namespace='accounts')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Documentation
    path('docs/', include_docs_urls(title='LibraryAPI')),
    path('schema/', get_schema_view(title="LibraryAPI",
                                    description='Api for the LibraryAPI',
                                    version='1.0.0',),
                                    name='openapi-schema')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)