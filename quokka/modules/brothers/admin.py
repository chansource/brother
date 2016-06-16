# -*- coding: utf-8 -*-

from quokka import admin
from quokka.core.admin.models import BaseContentAdmin
from quokka.core.widgets import TextEditor, PrepopulatedText
from .models import BrotherVideos, BrotherInfo, BrotherArticles,  BrotherAsk, Banner, Topic, News, About,JoinMessage
from quokka.utils.translation import _l
from flask_admin.contrib.mongoengine import EmbeddedForm

class ExperienceField(EmbeddedForm):

    form_args = {
        'title': {'label': u'内容'},
        'time': {'label': u'时间'}
    }


class PhotoField(EmbeddedForm):

    form_args = {
        "content": {'label': u'素材'},
        "order": {'label': u'填写1'},
        "purpose": {'label': u'选择Main Image'},
    }

    form_columns = [
        "content",
        "order",
        "purpose",
    ]


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
        'brother_is_ask',
        'brother_is_share',
        'brother_is_video',
        'brother_videos',
        'brother_articles',
        'published',
        'order',
        'home_order',
        'sex',
        'email',
        'tel',
        'qq',
        'born_city',
        'college_city',
        'work_city',
        'work_company',
        'internship_company',
        'work_abroad',
        'work_industry',
        'science_liberal',
        'like_numbers',
    ]

    form_args = {
        'channel': {'label': u'频道'},
        'related_channels': {'label': u'相关频道'},
        'title': {'label': u'姓名'},
        'slug': {'widget': PrepopulatedText(master='title')},
        'brother_college_major': {'label': u'专业'},
        'brother_college_name': {'label': u'学校'},
        'brother_tags': {'label': u'标签'},
        'brother_motto': {'label': u'语录'},
        'brother_experience_study': {'label': u'学习经历'},
        'brother_experience_work': {'label': u'工作经历'},
        'brither_experience_award': {'label': u'获奖经历'},
        'contents': {'label': u'照片'},
        'brother_is_ask': {'label': u'是否提供答问服务'},
        'brother_is_share': {'label': u'是否提供分享'},
        'brother_is_video': {'label': u'是否视频'},
        'brother_videos': {'label': u'视频'},
        'brother_articles': {'label': u'文章'},
        'published': {'label': u'是否发表'},
        'order': {'label': u'师兄列表排序(数小靠前)'},
        'home_order': {'label': u'主页排序(数小靠前)'},
        'sex': {'label': u'性别'},
        'email': {'label': u'邮箱'},
        'tel': {'label': u'电话'},
        'qq': {'label': u'QQ'},
        'born_city': {'label': u'籍贯'},
        'college_city': {'label': u'学校城市'},
        'work_city': {'label': u'工作城市'},
        'work_company': {'label': u'工作公司'},
        'internship_company': {'label': u'实习公司'},
        'work_abroad': {'label': u'是否海外工作'},
        'work_industry': {'label': u'工作行业'},
        'science_liberal': {'label': u'文理科'},
        "like_numbers": {'label': u'点赞数'},
    }

    form_subdocuments = {
        'brother_experience_study': {
            'form_subdocuments': { None: ExperienceField() }
        },
        'brother_experience_work': {
            'form_subdocuments': { None: ExperienceField() }
        },
        'brither_experience_award': {
            'form_subdocuments': { None: ExperienceField() }
        },
        'contents': {
            'form_subdocuments': { None: PhotoField() }
        }
    }


class VideoField(EmbeddedForm):

    form_args = {
        "video_title": {'label': u'视频标题'},
        "video_url": {'label': u'视频flash地址'},
        
    }

    form_columns = [
        "video_title",
        "video_url",
        
    ]


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
        'slug': {'widget': PrepopulatedText(master='title')},
        'channel': {'label': u'频道'},
        'related_channels': {'label': u'相关频道'},
        'title': {'label': u'标题'},
        'shared_by': {'label': u'分享人'},
        'videos': {'label': u'视频'},
        'published': {'label': u'是否发表'},
    }

    form_subdocuments = {
        'videos': {
            'form_subdocuments': { None: VideoField() }
        },
    }


class ArticleField(EmbeddedForm):

    form_args = {
        "title": {'label': u'标题'},
        "body": {'label': u'内容'},
    }

    form_columns = [
        "title",
        "body",
    ]


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
        'channel': {'label': u'频道'},
        'related_channels': {'label': u'相关频道'},
        'title': {'label': u'标题'},
        'author': {'label': u'作者'},
        'published': {'label': u'是否发表'},
        'articles': {'label': u'文章'},
        'slug': {'widget': PrepopulatedText(master='title')}
    }

    form_subdocuments = {
        'articles': {
            'form_subdocuments': { None: ArticleField() }
        },
    }


class TopicAdmin(BaseContentAdmin):
    form_columns = [
        'channel',
        'title',
        'slug',
        'summary',
        'contents',
        'videos',
        'shared_by',
        'published',
    ]

    form_args = {
        'title': {'label': u'标题'},
        'channel': {'label': u'频道'},
        'summary': {'label': u'摘要'},
        'contents': {'label': u'封面图'},
        'videos': {'label': u'视频'},
        'shared_by': {'label': u'分享人'},
        'published': {'label': u'是否发布'},
        'slug': {'widget': PrepopulatedText(master='title')}
    }

    form_subdocuments = {
        'contents': {
            'form_subdocuments': { None: PhotoField() }
        },
        'videos': {
            'form_subdocuments': { None: VideoField() }
        },
    }


class NewsAdmin(BaseContentAdmin):

    form_columns = [
        'channel',
        'title',  # 标题
        'slug',  # 路由
        'summary',  # 摘要
        'articles',  # 文章
        'contents',
        'author',  # 作者
        'published',  # 是否发布
    ]

    form_args = {
        'channel': {'label': u'频道'},
        'title': {'label': u'标题'},
        'summary': {'label': u'摘要'},
        'articles': {'label': u'文章'},
        'contents': {'label': u'封面图'},
        'author': {'label': u'作者'},
        'published': {'label': u'是否发布'},
        'slug': {'widget': PrepopulatedText(master='title')}
    }

    form_subdocuments = {
        'contents': {
            'form_subdocuments': { None: PhotoField() }
        },
        'articles': {
            'form_subdocuments': { None: ArticleField() }
        },
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
        'channel': {'label': u'频道'},
        'title': {'label': u'标题'},
        'articles': {'label': u'文章'},
        'author': {'label': u'作者'},
        'published': {'label': u'是否发布'},
        'slug': {'widget': PrepopulatedText(master='title')}
    }

    form_subdocuments = {
        'articles': {
            'form_subdocuments': { None: ArticleField() }
        },
    }


class BannerAdmin(BaseContentAdmin):

    form_columns = [
        'channel',
        'related_channels',
        'title',
        'slug',
        'contents',
        'url',
        'published',
    ]

    form_args = {
        'channel': {'label': u'频道'},
        'related_channels': {'label': u'相关频道'},
        'title': {'label': u'标题'},
        'contents': {'label': u'图片'},
        'url': {'label': u'链接'},
        'slug': {'widget': PrepopulatedText(master='title')},
        'published': {'label': u'是否发布'},
    }

    form_subdocuments = {
        'contents': {
            'form_subdocuments': { None: PhotoField() }
        },
    }



class BrotherAskAdmin(BaseContentAdmin):
    column_list = ['title','receiver','sender_email','created_at','status']
    column_searchable_list = ['title', 'message', 'receiver']
    column_expose_list = ['title', 'sender_email','receiver','created_at','message','status']
    column_filters = ['receiver','sender_email','created_at','status']
    form_columns = [
        'title',
        'created_at',
        'receiver',
        'brother',
        'sender_email',
        'message',
        'tags',
        'status',
    ]
    form_args = {
        'title': {'label': u'主题'},
        'created_at': {'label': u'提交时间'},
        'receiver': {'label': u'收件人'},
        'brother': {'label': u'对应的师兄'},
        'sender_email': {'label': u'发件人'},
        'message': {'label': u'提问内容'},
        'tags': {'label': u'标签'},
        'status': {'label': u'状态'},
    }
    column_expose_names={
        'title': u'主题',
        'created_at': u'提交时间',
        'receiver':u'收件人',
        'brother': u'对应的师兄',
        'sender_email': u'发件人',
        'message': u'提问内容',
        'tags': u'标签',
        'status': u'状态',
    }
class JoinMessageAdmin(BaseContentAdmin):
    column_list = ['sender_email','created_at','status']
    column_filters = ['sender_email','created_at','status']
    form_columns = [
        'title',
        'channel',
        'slug',
        'created_at',
        'sender_email',
        'message',
        'document',
        'status',
    ]
    form_args = {
        'title': {'label': u'主题'},
        'created_at': {'label': u'提交时间'},
        'sender_email': {'label': u'发件人'},
        'message': {'label': u'简介'},
        'document':{'label':u'附件'},
        'status': {'label': u'状态'},
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
admin.register(BrotherAsk, BrotherAskAdmin,
               category=_l("Content"), name=_l("BrotherAsk"))
admin.register(JoinMessage, JoinMessageAdmin,
               category=_l("Content"), name=_l("JoinMessage"))
