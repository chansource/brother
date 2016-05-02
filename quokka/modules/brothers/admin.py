# -*- coding: utf-8 -*-

from quokka import admin
from quokka.core.admin.models import BaseContentAdmin
from quokka.core.widgets import TextEditor, PrepopulatedText
from .models import BrotherVideos, BrotherInfo, BrotherArticles, Banner
from quokka.utils.translation import _l

class BrotherInfoAdmin(BaseContentAdmin):

    form_columns = [
        'channel',
        'related_channels',
        'title',
        'slug',
        'brother_college_major', 
        'brother_college_name',
        'brother_tags',
        'brother_motto',
        'brother_experience_study',
        'brother_experience_work',
        'brither_experience_award',
        'add_image',
        'brother_is_video',
        'brother_videos',
        'brother_article',
        'published',
    ]

    form_args = {
        'slug': {'widget': PrepopulatedText(master='title')}
    }

    column_descriptions = {
        'title': 'name',
        'brother_college_major': 'major',
    }

    column_labels = {
        'title': 'test_label'
    }

    form_args = dict(
        title=dict(label=u'姓名')
    )

class BrotherVideosAdmin(BaseContentAdmin):
    
    form_columns = [
        'channel',
        'related_channels',
        'title',
        'slug',
        'videos',
        'published',
    ]

    form_args = {
        'slug': {'widget': PrepopulatedText(master='title')}
    }

class BrotherArticlesAdmin(BaseContentAdmin):
    
    form_columns = [
        'channel',
        'related_channels',
        'title',
        'slug',
        'articles',
        'published',
    ]
    
    form_args = {
        'slug': {'widget': PrepopulatedText(master='title')}
    }


class BannerAdmin(BaseContentAdmin):

    form_columns = [
        'channel',
        'related_channels',
        'title',
        'slug',
        'add_image',
        'url',
        'published',
    ]

    form_args = {
        'slug': {'widget': PrepopulatedText(master='title')}
    }

admin.register(BrotherInfo, BrotherInfoAdmin, category=_l("Content"), name=_l("BrotherInfo"))
admin.register(BrotherVideos, BrotherVideosAdmin, category=_l("Content"), name=_l("BrotherVideos"))
admin.register(BrotherArticles, BrotherArticlesAdmin, category=_l("Content"), name=_l("BrotherArticles"))
admin.register(Banner, BannerAdmin, category=_l("Content"), name=_l("Banner"))
