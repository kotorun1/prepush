from rest_framework import serializers
from .models import NewTeacher, NewLocation, NewClassroom, NewGroup, NewSubject, NewEvent

class NewTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewTeacher
        fields = '__all__'

class NewLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewLocation
        fields = '__all__'

class NewClassroomSerializer(serializers.ModelSerializer):
    location = NewLocationSerializer()

    class Meta:
        model = NewClassroom
        fields = ('id', 'name', 'location')


class NewGroupSerializer(serializers.ModelSerializer):
    course = serializers.CharField(source='get_course_display')

    class Meta:
        model = NewGroup
        fields = ('id', 'number', 'name', 'course')

class NewSubjectSerializer(serializers.ModelSerializer):
    teacher = NewTeacherSerializer()
    classroom = NewClassroomSerializer()

    class Meta:
        model = NewSubject
        fields = ('id', 'name', 'teacher', 'classroom')

class NewEventSerializer(serializers.ModelSerializer):
    subject = NewSubjectSerializer()
    group = NewGroupSerializer()

    class Meta:
        model = NewEvent
        fields = ('id', 'start', 'end', 'subject', 'group')