from django.urls import path

from . import views

app_name = 'bitbucket'

urlpatterns = [
    path(
        'bitbucket/projects/<str:project_id>/repos/<str:repo_name>/',
        views.BitbucketRepoView.as_view(),
        name='repo'
    ),  # this one is here to define how the interface should look like -> it's not implemented yet
    path(
        'bitbucket/projects/<str:project_id>/repos/',
        views.BitbucketReposView.as_view(),
        name='repos'
    ),
]
