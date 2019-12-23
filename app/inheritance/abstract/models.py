from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']


class Student(CommonInfo):
    school = models.CharField(max_length=30)

    class Meta(CommonInfo.Meta):
        verbose_name = '학생'
        verbose_name_plural = '학생 목록'

    def __str__(self):
        return f'{self.name} (학교: {self.school})'


class Instructor(CommonInfo):
    academy = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} (학원: {self.academy})'


# Be careful with related_name and related_query_name
class Base(models.Model):
    m2m = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_set')

    class Meta:
        abstract = True


class ChildA(Base):
    pass


class ChildB(Base):
    pass
