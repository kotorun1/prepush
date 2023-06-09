from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import NewTeacher, NewLocation, NewClassroom, NewGroup, NewSubject, NewEvent
from .serializers import NewTeacherSerializer, NewLocationSerializer, NewClassroomSerializer, NewGroupSerializer, \
    NewSubjectSerializer, NewEventSerializer


class NewTeacherViewSet(viewsets.ModelViewSet):
    queryset = NewTeacher.objects.all()
    serializer_class = NewTeacherSerializer


class NewLocationViewSet(viewsets.ModelViewSet):
    queryset = NewLocation.objects.all()
    serializer_class = NewLocationSerializer


class NewClassroomViewSet(viewsets.ModelViewSet):
    queryset = NewClassroom.objects.all()
    serializer_class = NewClassroomSerializer


class NewGroupViewSet(viewsets.ModelViewSet):
    queryset = NewGroup.objects.all()
    serializer_class = NewGroupSerializer


class NewSubjectViewSet(viewsets.ModelViewSet):
    queryset = NewSubject.objects.all()
    serializer_class = NewSubjectSerializer


class NewEventViewSet(viewsets.ModelViewSet):
    queryset = NewEvent.objects.all()
    serializer_class = NewEventSerializer


class NewEventViewSet(viewsets.ModelViewSet):
    queryset = NewEvent.objects.all()
    serializer_class = NewEventSerializer

    @action(detail=False, methods=['GET'])
    def group_events(self, request):
        group_number = request.query_params.get('group_number')
        if group_number:
            events = self.queryset.filter(group__number=group_number)
            serializer = self.get_serializer(events, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Please provide a group_number parameter.'}, status=400)
