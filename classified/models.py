from django.db import models
from mezzanine.pages.models import Page
from mezzanine.generic.fields import KeywordsField, CommentsField
from mezzanine.core.models import Displayable, Ownable
from mezzanine.generic.models import Rating
from mezzanine.generic.fields import RatingField, CommentsField


# Create your models here.

class Classified(models.Model):
    slug = models.SlugField(unique=True, blank=True, null=True)
    classified_title = models.CharField(max_length=100, null=True, blank=True)
    submission_date = models.DateField(null=True, blank=True)
    keywords = KeywordsField(null=True, blank=True)
    comments = CommentsField(null=True, blank=True)

    def save(self, *args, **kwargs):
         if not self.slug:
            self.slug = slugify(self.classified_title)
         super(Classified, self).save(*args, **kwargs)
    @models.permalink
    def get_absolute_url(self):
        return ("classified_detail", (), {"slug": self.slug})
    def __unicode__(self):
        return self.classified_title
