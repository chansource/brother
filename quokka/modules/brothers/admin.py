# coding : utf-8

from quokka import admin
from quokka.core.admin.models import BaseContentAdmin
from quokka.core.widgets import TextEditor, PrepopulatedText
from .models import BrotherVideo, Experience, BrotherInfo, BrotherArticle
from quokka.utils.translation import _l

class BrotherInfoAdmin(BaseContentAdmin):

    form_columns = [
        'title',
        'slug',
        'channel',
        'brother_name', 
        'brother_college_major', 
        'brother_college_name',
        'brother_tags',
        'brother_motto',
        'brother_experience_study',
        'brother_experience_work',
        'brither_experience_award',
        'tags',
        'brother_is_video',
        'brother_video',
        'brother_article',
    ]

admin.register(BrotherInfo, BrotherInfoAdmin, category=_l("Content"), name=_l("BrotherInfo"))