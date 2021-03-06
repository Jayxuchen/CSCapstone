"""ProjectsApp URL Configuration

Created by Harris Christiansen on 10/02/16.
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^project/all$', views.getProjects, name='Projects'),
    url(r'^project/form$', views.getProjectForm, name='ProjectsForm'),
    url(r'^project$', views.getProject, name='Project'),
    url(r'^project/join$', views.joinProject, name='JoinProject'),
    url(r'^project/unjoin$', views.unjoinProject, name='UnjoinProject'),
    url(r'^project/edit$', views.editProject, name='EditProject'),
    url(r'^bookmarks$', views.viewBookmarks, name='Bookmarks')
]
