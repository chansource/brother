# -*- coding: utf-8 -*-

from quokka.core.db import db
from quokka.core.models.content import Content
from quokka.core.models.subcontent import SubContent


class Video(db.EmbeddedDocument):
    """
    单一视频
    """
    video_title = db.StringField(max_length=255,required=True,default="default title of the video")  # 视频标题
    video_url = db.StringField(max_length=255, required=True)  # 视频url
    like_numers = db.IntField(default=0)  # 点赞数


class BrotherVideos(Content):
    """
    师兄视频集
    """
    shared_by = db.StringField(max_length=255, required=True)  # 分享人
    videos = db.ListField(
        db.EmbeddedDocumentField(Video, required=True), required=False)  # 师兄视频列表


class Article(db.EmbeddedDocument):
    """
    师兄单一文章
    """
    title = db.StringField(max_length=255, required=True)  # 文章标题
    body = db.StringField(required=True)  # 文章正文


class BrotherArticles(Content):
    """
    师兄文章集
    """
    articles = db.ListField(
        db.EmbeddedDocumentField(Article, required=True), required=False)  # 师兄文章列表


class Experience(db.EmbeddedDocument):
    """
    个人经历信息
    """
    title = db.StringField(max_length=255, required=True)  # 名称
    time = db.StringField(max_length=255, required=True)  # 时间区间


class BrotherInfo(Content):
    """
    师兄信息
    """
    # 师兄封面图片，使用Content.path
    # 师兄姓名，使用Content.title
    brother_college_major = db.StringField(
        max_length=255, required=True)  # 师兄专业
    brother_college_name = db.StringField(
        max_length=255, required=True)  # 师兄毕业院校
    brother_tags = db.ListField(db.StringField(
        max_length=255), required=False)  # 师兄标签
    brother_motto = db.StringField(max_length=255, required=True)  # 师兄语录
    brother_experience_study = db.ListField(
        db.EmbeddedDocumentField(Experience), required=False)  # 师兄学习经历
    brother_experience_work = db.ListField(
        db.EmbeddedDocumentField(Experience), required=False)  # 师兄工作经历
    brither_experience_award = db.ListField(
        db.EmbeddedDocumentField(Experience), required=False)  # 师兄获奖经历
    brother_is_video = db.BooleanField(required=False, default=True)  # 是否视频类型
    brother_videos = db.ReferenceField(BrotherVideos, required=False)  # 视频
    brother_articles = db.ReferenceField(
        BrotherArticles, required=False)  # 文章信息


class Topic(Content):
    """
    话题类
    """
    shared_by = db.StringField(max_length=255, required=True)  # 分享人
    videos = db.ListField(
        db.EmbeddedDocumentField(Video, required=True), required=False)  # 分享视频

class News(Content):
    """
    动态
    """
    author = db.StringField(max_length=255, required=True)  # 作者
    articles = db.ListField(
        db.EmbeddedDocumentField(Article, required=True), required=False)  # 文章列表

class About(Content):
    """
    关于
    """
    author = db.StringField(max_length=255, required=True)  # 作者
    articles = db.ListField(
        db.EmbeddedDocumentField(Article, required=True), required=False)  # 文章列表