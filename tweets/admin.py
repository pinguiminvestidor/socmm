from django.contrib import admin

from tweets.models import Tweet, Post, AffiliateProduct, AffiliateCategory, AffiliatePlatform

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
   list_display = (
       'text',
       'has_image',
       'pubdate',
       'category',
   )
   ordering = ['-pubdate']
   list_filter = ['pubdate','category']

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pubdate',
        'category',
    )
    ordering = ['-pubdate']
    list_filter = ['pubdate', 'category']

class AffiliateProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'url',
        'category',
        'platform',
        'profit',
    )
    list_filter = ['category', 'platform']
    ordering = ['-id','price']

class AffiliateCategoryAdmin(admin.ModelAdmin):
    list_dislay = (
        'category_name'
    )

class AffiliatePlatformAdmin(admin.ModelAdmin):
    list_dislay = (
        'platform_name'
    )

admin.site.register(Tweet, TweetAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(AffiliateProduct, AffiliateProductAdmin)
admin.site.register(AffiliateCategory, AffiliateCategoryAdmin)
admin.site.register(AffiliatePlatform, AffiliatePlatformAdmin)

# Do some mild branding:
admin.site.site_header = "Social Media Administration"
admin.site.site_title = "Social Media Administration"
