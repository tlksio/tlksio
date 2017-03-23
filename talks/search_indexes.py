import datetime
from haystack import indexes

from talks.models import Talk

class TalkIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(model_attr='title', document=True)
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Talk

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created__lte=datetime.datetime.now())
