from django.urls import path
from . import views
from learning import studentviews,adminviews,teacherviews

urlpatterns = [
    path('postnav/',views.NavCreateView.as_view(), name="postnav"),
    path("getnav/",views.NavListView.as_view(),name='getnav'),
    path("create_nav/",views.create_nav,name='create_nav'),
]