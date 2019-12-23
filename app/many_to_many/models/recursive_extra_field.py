from django.db import models


class InstagramUser(models.Model):
    name = models.CharField(max_length=20)
    following = models.ManyToManyField('self', through='Relation', related_name='followers', symmetrical=False)

    def __str__(self):
        return self.name


class Relation(models.Model):
    me = models.ForeignKey(InstagramUser, related_name='me_relation_set', on_delete=models.CASCADE)
    counterpart = models.ForeignKey(InstagramUser, related_name='counterpart_relation_set', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Relation (from_user: {self.me.name}, to_user: {self.counterpart.name})'

