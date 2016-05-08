# -*- coding: utf-8 -*-

from quokka import admin
from quokka.core.admin.models import BaseContentAdmin
from quokka.core.widgets import TextEditor, PrepopulatedText
from .models import BrotherVideos, BrotherInfo, BrotherArticles, Banner, Topic, News, About
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
        'contents',
        'add_image',
        'brother_is_video',
        'brother_videos',
        'brother_articles',
        'published',
    ]

    form_args = {
        'slug': {'widget': PrepopulatedText(master='title')}
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
        'shared_by',
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
        'author',
        'articles',
        'published',
    ]

    form_args = {
        'slug': {'widget': PrepopulatedText(master='title')}
    }


class TopicAdmin(BaseContentAdmin):
    form_columns = [
        'title',
        'slug',
        'summary',
        'contents',
        'add_image',
        'videos',
        'shared_by',
        'published',
        'channel',
    ]
    form_args = {
        'slug': {'widget': PrepopulatedText(master='title')}
    }


class NewsAdmin(BaseContentAdmin):
    form_columns = [
        'title',  # 标题
        'slug',  # 路由
        'summary',  # 摘要
        'articles',  # 文章
        'contents',
        'add_image',  # 图片
        'author',  # 作者
        'published',  # 是否发布
        'channel',
    ]
    form_args = {
        'slug': {'widget': PrepopulatedText(master='title')}
    }


class AboutAdmin(BaseContentAdmin):
    form_columns = [
        'title',
        'slug',  # 路由
        'articles',  # 文章
        'author',  # 作者
        'published',  # 是否发布
        'channel',
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
        'contents',
        'add_image',
        'url',
        'published',
    ]

    form_args = {
        'slug': {'widget': PrepopulatedText(master='title')}
    }

admin.register(BrotherInfo, BrotherInfoAdmin,
               category=_l("Content"), name=_l("BrotherInfo"))
admin.register(BrotherVideos, BrotherVideosAdmin,
               category=_l("Content"), name=_l("BrotherVideos"))
admin.register(BrotherArticles, BrotherArticlesAdmin,
               category=_l("Content"), name=_l("BrotherArticles"))
admin.register(Topic, TopicAdmin, category=_l("Content"), name=_l("Topic"))
admin.register(News, NewsAdmin, category=_l("Content"), name=_l("News"))
admin.register(About, AboutAdmin, category=_l("Content"), name=_l("About"))
admin.register(Banner, BannerAdmin, category=_l("Content"), name=_l("Banner"))
