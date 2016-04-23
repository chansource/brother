# -*- coding: utf-8 -*-

from quokka.core.db import db
from quokka.core.models.content import Content
from quokka.core.models.subcontent import SubContent

class Experience(db.EmbeddedDocument):
    """
    个人经历信息
    """
    title = db.StringField(max_length=255, required=True) # 名称
    time = db.StringField(max_length=255, required=True) # 时间区间

class BrotherVideo(db.EmbeddedDocument):
    """
    视频型师兄信息，含五个视频URL
    """ 
    brother_video1_url = db.StringField(max_length=255, required=False)
    brother_video2_url = db.StringField(max_length=255, required=False)
    brother_video3_url = db.StringField(max_length=255, required=False)
    brother_video4_url = db.StringField(max_length=255, required=False)
    brother_video5_url = db.StringField(max_length=255, required=False)

class BrotherArticle(db.EmbeddedDocument):
    """
    文章型师兄信息
    TODO: Complete it.
    """
    pass

class BrotherInfo(Content):
    """
    师兄信息
    """
    brother_name = db.StringField(max_length=255, required=False) # 师兄姓名
    brother_college_major = db.StringField(max_length=255, required=False) # 师兄专业
    brother_college_name = db.StringField(max_length=255, required=False) # 师兄毕业院校
    brother_tags = db.ListField(db.StringField(max_length=255)) # 师兄标签
    brother_motto = db.StringField(max_length=255, required=False) # 师兄语录
    brother_experience_study = db.ListField(
        db.EmbeddedDocumentField(Experience), required=False) # 师兄学习经历
    brother_experience_work = db.ListField(
        db.EmbeddedDocumentField(Experience), required=False) # 师兄工作经历
    brither_experience_award = db.ListField(
        db.EmbeddedDocumentField(Experience), required=False) # 师兄获奖经历
    brother_cover_small = db.StringField(max_length=255, required=False) # 师兄小封面
    brother_cover_middle = db.StringField(max_length=255, required=False) # 师兄中封面
    brother_cover_large = db.StringField(max_length=255, required=False) # 师兄大封面
    brother_is_video = db.BooleanField(required=True) # 是否视频类型
    brother_video = db.EmbeddedDocumentField(BrotherVideo, required=False) # 视频信息
    brother_article = db.EmbeddedDocumentField(BrotherArticle, required=False) # 文章信息

