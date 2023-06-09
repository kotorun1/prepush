from django.urls import path, include
from rest_framework import routers
from .views import NewTeacherViewSet, NewLocationViewSet, NewClassroomViewSet, NewGroupViewSet, NewSubjectViewSet,\
    NewEventViewSet

router = routers.DefaultRouter()
router.register(r'teachers', NewTeacherViewSet)
router.register(r'locations', NewLocationViewSet)
router.register(r'classrooms', NewClassroomViewSet)
router.register(r'groups', NewGroupViewSet)
router.register(r'subjects', NewSubjectViewSet)
router.register(r'events', NewEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/events/group_events/', NewEventViewSet.as_view({'get': 'group_events'}), name='group-events'),
    #/api/events/group_events/?group_number=<group_number>
]
