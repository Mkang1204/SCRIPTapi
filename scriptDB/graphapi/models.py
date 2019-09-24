from neomodel import StringProperty, DateTimeProperty, StructuredNode, StructuredRel, UniqueIdProperty
from django_neomodel import DjangoNode

from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
# sample from github neo_model
class Person(StructuredNode):
    name = StringProperty(unique_index=True)
    born = DateTimeProperty()

    # def signal_func(sender, instanse, signal, created):
    # def signal_func(self)
    #     pass
    # signal_func.post_save.connect(signal_func, sender=Person)
    def born(self):
        self.born_date = timezone.now()
        self.save()


    def _str_(self):
        return self.name

#switch from StucturedNode to DjangoNode
class Movie(DjangoNode):
    title = StringProperty(unique_index=True)
    tagline = StringProperty(unique_index=True)
    released = DateTimeProperty()

# class MovieForm(ModelForm):
#     class Meta:
#         model = Movie
#         fields = ['title', 'status']