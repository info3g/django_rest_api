from django.conf.urls import url, include
from rest_framework import routers
# from rest_framework.urlpatterns import format_suffix_patterns

from backend_api.views import UserViewSet, StudentList, StudentDetail

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^students/$', StudentList.as_view()),
    url(r'^students/(?P<pk>[0-9]+)/', StudentDetail.as_view()),
] # + router.urls

# urlpatterns = format_suffix_patterns(urlpatterns)