from django.db import models

from django.utils import timezone

# Create your models here.

class Tweet(models.Model):
    '''
    Represents a tweet, 280-char long, with an optional image attached.

    Date used is important since we don't want to re-use fresh tweets

    Default option is to be an engaging jab, but traffic-building right-hooks
    are also possible.
    '''
    text = models.TextField(max_length=280)
    image = models.URLField(blank=True) # url to image on the web

    # is this a right hook or a jab?

    category_choices = [
        ('JB', 'Jab'),
        ('RH', 'Right Hook'),
    ]

    category = models.CharField(
        max_length=2, 
        choices=category_choices,
        default='JB'
    )

    pubdate = models.DateField(default=timezone.now)

    def has_image(self):
        if self.image == "":
            return False
        else:
            return True

    # Name your tweets!
    def __str__(self):
        return self.text[0:40] + "(...)"

class Post(models.Model):
    '''
    A blog or other platform post, with title, outline (optional) content 
    (in Markdown), category and a date.

    Optional image as an URL.
    '''

    title = models.CharField(max_length=200)
    pubdate = models.DateField(default=timezone.now)
    outline = models.TextField(blank=True, help_text="Optional, just helps")
    content = models.TextField()
    CATEGORIES = [
        ('BL','Blog Post'),
        ('YT','YouTube Description'),
        ('PC','Podcast Episode'),
        ('FB','Facebook Post'),
    ]
    category = models.CharField(max_length=2, choices=CATEGORIES, default='BL') 
    image = models.URLField(blank=True, help_text="Optional for post")

    def __str__(self):
        return self.title

class AffiliateProduct(models.Model):
    '''
    Instead of writing down links in the napkin, use this database to always
    have the items you wanna sell available, regardless of Amazon state.

    Faster and more portable, especially with shortlinks that have the tag
    embedded already.
    '''

    name = models.CharField(max_length = 140)
    url = models.URLField()
    price = models.FloatField()

    # Foreign key from the AffiliatePlatform class.
    platform = models.ForeignKey('AffiliatePlatform', on_delete=models.CASCADE)

    # Ditto, for categories...
    category = models.ForeignKey('AffiliateCategory', on_delete=models.CASCADE)

    def profit(self):
        '''
        Previews the profit from the sale using a rule of thumb of 9% commision
        '''
        profit = self.price * .09
        return '{0:.2f}'.format(profit)

    def __str__(self):
        return self.name

class AffiliatePlatform(models.Model):
    '''
    An Affiliate Marketing website for which we have an account and are
    able to sell stuff for commission.
    '''
    platform_name = models.CharField(max_length = 80)
    def __str__(self):
        return self.platform_name

class AffiliateCategory(models.Model):
    '''
    A product category for stuff we sell for commission.
    '''
    category_name = models.CharField(max_length = 80)
    def __str__(self):
        return self.category_name
