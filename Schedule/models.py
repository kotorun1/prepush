from django.db import models

# Новые модели 06.07.23

class NewTeacher(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

class NewLocation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

class NewClassroom(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(NewLocation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'

class NewGroup(models.Model):
    number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    course = models.CharField(
        max_length=100,
        choices=[
            ('1', 'Курс 1'),
            ('2', 'Курс 2'),
            ('3', 'Курс 3'),
            ('4', 'Курс 4'),
        ]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class NewSubject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(NewTeacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(NewClassroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class NewEvent(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    subject = models.ForeignKey(NewSubject, on_delete=models.CASCADE)
    group = models.ForeignKey(NewGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subject} - {self.group}'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['start']
