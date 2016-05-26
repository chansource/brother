#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path as op
import os
from flask.views import MethodView
from quokka.core.templates import render_template
from flask import request,url_for
from .models import Media,File,FileUploadField
from quokka.utils.upload import *
from quokka.utils.baseresp import _base_err_resp,_base_normal_resp
import uuid
from flask_mongoengine.wtf import model_form
import logging

logger = logging.getLogger("quokka")


class ListView(MethodView):

    def get(self):
        logger.info('getting list of media')
        medias = Media.objects.all()
        return render_template('media/list.html', medias=medias)


class DetailView(MethodView):

    @staticmethod
    def get_context(slug):
        media = Media.objects.get_or_404(slug=slug)

        context = {
            "media": media
        }
        return context

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('medias/detail.html', **context)


class UploadFileView(MethodView):
    '''提供统一的上传文件接口，保存文件，返回path'''
    permission=0o666

    def post(self):
        '''接受post请求'''
        f = request.files['file']
        file_obj=File()  #创建file对象
        filename=dated_path(file_obj,f)  #TODO 使用FileUplloadField进行文件上传的管理
        path=op.join(media_path(),filename)
        file_obj.title=f.filename
        file_obj.slug=str(uuid.uuid1())
        file_obj.path=filename
        try:
            file_obj.channel=File().get_default_channel()  #获取默认的channel
            #先保存文件，之后再保存model
            if not op.exists(op.dirname(path)):
                                os.makedirs(os.path.dirname(path), self.permission | 0o111)
            f.save(path)
            file_obj.save()
        except Exception, e:
            logger.error(str(e))
            return _base_err_resp("something went wrong")
        # return _base_normal_resp({'path':url_for('quokka.core.media', filename=filename)})
        return _base_normal_resp({'file_id':str(file_obj.id)})
