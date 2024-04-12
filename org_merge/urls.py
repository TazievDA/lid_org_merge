"""
URL configuration for org_merge project.

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
from django.contrib import admin
from django.urls import path, include

from merging.views import MergingViews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", MergingViews().index_view),
    path("find/", MergingViews().show_org_view),
    path("preview_orgs/", MergingViews().show_orgs_to_merge_view),
    path("merge_orgs/", MergingViews().show_orgs_to_merge_view),
]
