from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from datetime import datetime, date, timedelta
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
        date_param = request.query_params.get('date')

        if group_number:
            try:
                group = NewGroup.objects.get(number=group_number)
                events = self.queryset.filter(group=group)
            except NewGroup.DoesNotExist:
                return Response({'error': 'Group not found.'}, status=404)
        else:
            events = self.queryset.all()

        if date_param:
            try:
                date_obj = datetime.strptime(date_param, '%Y-%m-%d').date()
            except ValueError:
                return Response({'error': 'Invalid date format. Please use YYYY-MM-DD.'}, status=400)

            events = events.filter(start__date=date_obj)
        else:
            week_param = request.query_params.get('week')

            if week_param:
                try:
                    year, week_number = map(int, week_param.split('-W'))
                    week_start = datetime.strptime(f'{year}-W{week_number}-1', '%Y-W%W-%w').date()
                    week_end = week_start + timedelta(days=6)
                except (ValueError, OverflowError):
                    return Response({'error': 'Invalid week format. Please use the ISO week format (YYYY-WW).'}, status=400)

                events = events.filter(start__date__range=(week_start, week_end))
            else:
                today = date.today()
                start_of_week = today - timedelta(days=today.weekday())
                end_of_week = start_of_week + timedelta(days=6)
                events = events.filter(start__date__range=(start_of_week, end_of_week))

        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
