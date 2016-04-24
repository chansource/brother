# coding : utf-8

from quokka import admin
from quokka.core.admin.models import BaseContentAdmin
from quokka.core.widgets import TextEditor, PrepopulatedText
from .models import BrotherVideos, BrotherInfo, BrotherArticles
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

class BrotherVideosAdmin(BaseContentAdmin):
    
    form_columns = [
        'channel',
        'title',
        'slug',
        'videos',
    ]

    form_args = {
        'slug': {'widget': PrepopulatedText(master='title')}
    }

class BrotherArticlesAdmin(BaseContentAdmin):
    
    form_columns = [
        'channel',
        'title',
        'slug',
        'articles',
    ]
    
    form_args = {
        'slug': {'widget': PrepopulatedText(master='title')}
    }

admin.register(BrotherInfo, BrotherInfoAdmin, category=_l("Content"), name=_l("BrotherInfo"))
admin.register(BrotherVideos, BrotherVideosAdmin, category=_l("Content"), name=_l("BrotherVideos"))
admin.register(BrotherArticles, BrotherArticlesAdmin, category=_l("Content"), name=_l("BrotherArticles"))
