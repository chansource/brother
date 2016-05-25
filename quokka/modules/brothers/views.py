# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask_mongoengine.wtf import model_form
from flask import request
from quokka.utils.baseresp import _base_err_resp,_base_normal_resp
from .models import BrotherVideos,BrotherAsk,JoinMessage
from pprint import pprint
import uuid
import logging

logger = logging.getLogger('quokka')

# def _base_err_resp(err_msg="Default error message.", err_rtn=1):
#     resp = {
#         "rtn": err_rtn,
#         "msg": err_msg,
#     }
#     return jsonify(resp)

# def _base_normal_resp(data={}):
#     resp = {
#         "rtn": 0,
#         "data": data,
#     }
#     return jsonify(resp)

class AddLikeView(MethodView):
    """
    Add like number.

    `HTTP` is form-style request,json-style respond using post submit.

    POST param:
        id: BrotherVideos id
        index: video index,eg 0,1,2,3,4

    HTTP return:
        Try it your self.
    """

    def post(self):
        logger.debug("add like view")
        try:
            content_id = request.form["id"]
            index = int(request.form["index"])
            logger.debug("content_id:{}  index:{}".format(content_id,index))
            result = BrotherVideos.objects(id=content_id).first()
            result.videos[index].like_numbers += 1
            result.save()
            return _base_normal_resp()

        except Exception, e:
            logger.error(str(e))
            return _base_err_resp("error")


class SendMessageView(MethodView):
    """
    Send message to brother.

    `HTTP` is form-style request,json-style respond using post submit.

    POST param:
        brother_id: BrotherInfo id
        receiver: the receiver of the message
        sender_email:  the email address of the sender
        title: the title of the message
        message: the content of the message

    HTTP return:
        Try it your self.
    """

    def post(self):
        logger.debug("new ask message")
        BrotherAskForm = model_form(BrotherAsk)
        try:
            form = BrotherAskForm(request.form)
            if form.validate():
               logger.debug("form validate.form data: {}".format(form.data))
               brother_ask=BrotherAsk()
               form.populate_obj(brother_ask)
               brother_ask.slug=str(uuid.uuid1())
               brother_ask.save()
               logger.debug("brother ask message saved.")
               return _base_normal_resp()
            else:
                logger.error("form.errors-{}".format(form.errors))
                logger.error("form.data-{}".format(request.form))
                return _base_err_resp("error in the form")
        except Exception, e:
            logger.error(str(e))
            return _base_err_resp("something went wrong")

class JoinMessageView(MethodView):
    """
    Send message to admin.

    `HTTP` is form-style request,json-style respond using post submit.

    POST param:
        sender_email:  the email address of the sender
        message: the content of the message

    HTTP return:
        Try it your self.
    """

    def post(self):
        logger.debug("new join_message")
        JoinMessageForm = model_form(JoinMessage)
        try:
            form = JoinMessageForm(request.form)
            if form.validate():
               logger.debug("form validate.form data: {}".format(form.data))
               join_message=JoinMessage()
               form.populate_obj(join_message)
               join_message.slug=str(uuid.uuid1())
               join_message.save()
               logger.debug("join_message saved.")
               return _base_normal_resp()
            else:
                logger.error("form.errors-{}".format(form.errors))
                return _base_err_resp("error in the form")
        except Exception, e:
            logger.error(str(e))
            return _base_err_resp("something went wrong")
