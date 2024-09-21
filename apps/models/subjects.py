from django.db.models import CharField, Model, IntegerField


class Subject(Model):
    subject_id = IntegerField(primary_key=True)
    name = CharField(max_length=25)


