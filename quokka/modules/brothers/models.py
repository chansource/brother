# -*- coding: utf-8 -*-

from quokka.core.db import db
from quokka.core.models.content import Content
from quokka.core.models.subcontent import SubContent
from quokka.core.models.signature import Ordered


class Video(db.EmbeddedDocument):
    """
    单一视频
    """
    video_title = db.StringField(max_length=255, required=True)  # 视频标题
    video_url = db.StringField(max_length=255, required=True)  # 视频url
    like_numbers = db.IntField(default=0)  # 点赞数

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
    author = db.StringField(max_length=255, required=True)  # 分享人
    articles = db.ListField(
        db.EmbeddedDocumentField(Article, required=True), required=False)  # 师兄文章列表


class Experience(db.EmbeddedDocument):
    """
    个人经历信息
    """
    title = db.StringField(max_length=255, required=True)  # 名称
    time = db.StringField(max_length=255, required=True)  # 时间区间


class BrotherInfo(Content, Ordered):
    """
    师兄信息
    """

    meta = {
        'allow_inheritance': True,
        'ordering': ['order'],
    }

    # 师兄列表排序，使用Ordered.order
    # 师兄封面图片，使用Content.contents
    # 师兄姓名，使用Content.title
    home_order = db.IntField(required=True, default=1) # 主页排序
    brother_college_major = db.StringField(
        max_length=255, required=False)  # 师兄专业
    brother_college_name = db.StringField(
        max_length=255, required=False)  # 师兄毕业院校
    brother_tags = db.ListField(db.StringField(
        max_length=255), required=False)  # 师兄标签
    brother_motto = db.StringField(max_length=255, required=False)  # 师兄语录
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
    sex = db.StringField(
        max_length=255, required=False)  # 性别
    email = db.StringField(
        max_length=255, required=False)  # 邮箱
    tel = db.StringField(
        max_length=255, required=False)  # 电话
    qq = db.StringField(
        max_length=255, required=False)  # QQ
    born_city = db.StringField(
        max_length=255, required=False)  # 籍贯
    college_city = db.StringField(
        max_length=255, required=False)  # 学校城市
    work_city = db.StringField(
        max_length=255, required=False)  # 工作城市
    work_company = db.StringField(
        max_length=255, required=False)  # 工作公司
    internship_company = db.StringField(
        max_length=255, required=False)  # 实习公司
    work_abroad = db.BooleanField(required=False) # 是否海外工作
    work_industry = db.StringField(
        max_length=255, required=False)  # 工作行业
    science_liberal = db.StringField(
        max_length=255, required=False)  # 文理科

class Banner(Content):
    """
    轮播图
    """
    # 轮播图片，使用Content.path
    url = db.StringField(max_length=255, required=True) # 链接地址


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
