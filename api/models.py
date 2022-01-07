import datetime
from doctest import REPORT_CDIFF

from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.postgres.fields import ArrayField
from django_pgviews import view as pg
from django.contrib.postgres.indexes import GinIndex

from django.conf import settings

from django.contrib.postgres.search import SearchVectorField


from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


class User(AbstractUser):
    name = models.CharField("Name of user", blank=True, max_length=255)


class Comment(models.Model):
    class Meta:
        unique_together = (('source', 'post_id'),)
        indexes = [GinIndex(fields=[
            'search_vector'
        ])]
        
    search_vector = SearchVectorField(null=True, blank=True)
    url = models.TextField(null=True)
    user_description = models.TextField(null=True)
    user_label = models.TextField(null=True)
    title = models.TextField(null=True)
    slug = models.TextField(null=True)
    content = models.TextField(null=True)
    parent = models.TextField(null=True)
    posted_date = models.DateTimeField(null=True)
    username = models.TextField(null=True)
    platform = models.TextField(null=True)
    subreddit = models.TextField(null=True)
    source = models.TextField(null=True)
    post_id = models.TextField(null=True)
    content_type = models.TextField(null=True)
    kids = models.TextField(null=True)
    post_link_title = models.TextField(null=True)
    post_link_url = models.TextField(null=True)
    score = models.IntegerField(null=True)
    num_comments = models.IntegerField(null=True)
    soundex = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    # tickers = models.ManyToManyField('Ticker', related_name='comments', blank=True)
    # author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    # searchparams = models.ManyToManyField('Searchparam', related_name='comments', blank=True)
    user_profile = models.TextField(null=True)
    user_id = models.TextField(null=True)
    user_created = models.DateTimeField(null=True)
    reply_count = models.TextField(null=True)
    like_count = models.TextField(null=True)
    mentioned_users = models.TextField(null=True)
    followers = models.TextField(null=True)
    qa = models.TextField(null=True)

    score_last_updated = models.DateTimeField(null=True)
    descendants = models.TextField(null=True)
