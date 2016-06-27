# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask_mongoengine.wtf import model_form
from flask import request, url_for
from quokka.utils.baseresp import _base_err_resp, _base_normal_resp
from .models import BrotherVideos, BrotherArticles, BrotherAsk, JoinMessage, BrotherInfo, Topic, News
from pprint import pprint
import uuid
import logging
import datetime

logger = logging.getLogger('quokka')

class BrotherLikeView(MethodView):
    def get(self):
        """
            Get like number.

            `HTTP` is form-style request,json-style respond using post submit.

            POST param:
                id: BrotherInfo id

            HTTP return:
                Try it your self.
        """
        logger.debug("get brother like view")
        try:
            content_id = request.args.get("id")
            logger.debug("content_id:{}".format(content_id))
            result = BrotherInfo.objects(id=content_id).first()
            data={"like_numbers":result.like_numbers}
            return _base_normal_resp(data=data)

        except Exception, e:
            logger.error(str(e))
            return _base_err_resp("error")
               
    def post(self):
        """
            Add like number.

            `HTTP` is form-style request,json-style respond using post submit.

            POST param:
                id: BrotherInfo id

            HTTP return:
                Try it your self.
        """
        logger.debug("add brother like view")
        try:
            content_id = request.form["id"]
            logger.debug("content_id:{}".format(content_id))
            result = BrotherInfo.objects(id=content_id).first()
            logger.debug("pre like numbers:{}".format(result.like_numbers))
            result.like_numbers += 1
            result.save()
            logger.debug("after like numbers:{}".format(result.like_numbers))
            return _base_normal_resp()

        except Exception, e:
            logger.error(str(e))
            return _base_err_resp("error")

class AddTopicVideoLikeView(MethodView):
    def get(self):
        """
            Get like number.

            `HTTP` is form-style request,json-style respond using post submit.

            GET param:
                id: Topic id
                index: 一个话题可含多个视频，第一个index为0，依次类推

            HTTP return:
                Try it your self.
        """
        try:
            content_id = request.args.get("id")
            index = int(request.args.get("index"))
            result = Topic.objects(id=content_id).first()            
            data={"like_numbers": result.videos[index].like_numbers}
            return _base_normal_resp(data=data)
        except Exception, e:
            logger.error(str(e))
            return _base_err_resp("error")

    def post(self):
        """
            Add like number.

            `HTTP` is form-style request,json-style respond using post submit.

            POST param:
                id: Topic id
                index: 一个话题可含多个视频，第一个index为0，依次类推

            HTTP return:
                Try it your self.
        """
        try:
            content_id = request.form["id"]
            index = int(request.form["index"])
            result = Topic.objects(id=content_id).first()
            result.videos[index].like_numbers += 1
            result.save()
            return _base_normal_resp()
        except Exception, e:
            logger.error(str(e))
            return _base_err_resp("error")

class AddNewsArticleLikeView(MethodView):
    def get(self):
        """
            Get like number.

            `HTTP` is form-style request,json-style respond using post submit.

            GET param:
                id: News id
                index: 一个动态可含多个文章，第一个index为0，依次类推

            HTTP return:
                Try it your self.
        """
        try:
            content_id = request.args.get("id")
            index = int(request.args.get("index"))
            result = News.objects(id=content_id).first()
            data={"like_numbers": result.articles[index].like_numbers}
            return _base_normal_resp(data=data)
        except Exception, e:
            logger.error(str(e))
            return _base_err_resp("error")

    def post(self):
        """
            Add like number.

            `HTTP` is form-style request,json-style respond using post submit.

            POST param:
                id: News id
                index: 一个动态可含多个文章，第一个index为0，依次类推

            HTTP return:
                Try it your self.
        """
        try:
            content_id = request.form["id"]
            index = int(request.form["index"])
            result = News.objects(id=content_id).first()
            result.articles[index].like_numbers += 1
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
                brother_ask = BrotherAsk()
                form.populate_obj(brother_ask)
                brother_ask.slug = str(uuid.uuid1())
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
                join_message = JoinMessage()
                form.populate_obj(join_message)
                join_message.slug = str(uuid.uuid1())
                join_message.save()
                logger.debug("join_message saved.")
                return _base_normal_resp()
            else:
                logger.error("form.errors-{}".format(form.errors))
                return _base_err_resp("error in the form")
        except Exception, e:
            logger.error(str(e))
            return _base_err_resp("something went wrong")


class BrotherInfoView(MethodView):
    """
    Get brother list.

    `HTTP` is form-style request,json-style respond using post submit.

    POST param:
        offset: start position
        count: result count

    HTTP return:
        Try it your self.
    """

    def get(self):
        offset = int(request.args.get("offset", 0))
        count = int(request.args.get("count", 10))
        order_type = request.args.get("order", "")
        order_map = {"time": "-created_at", "hot": "-like_numbers"}
        ordering = order_map[order_type]
        logger.debug("offset-{} count-{} ordering-{}".format(offset,count,ordering))
        if ordering:
            now = datetime.datetime.now()
            filters = {
                'published': True,
                'available_at__lte': now,
            }
            logger.debug("order")
            results = BrotherInfo.objects(
                **filters).order_by(ordering).skip(offset).limit(count)
        else:
            results = BrotherInfo.objects.skip(offset).limit(count)
        brother_list = []
        for i in results:
            tmp = {
                "brother_tags": i["brother_tags"],
                "photo": url_for('quokka.core.media', filename=i["contents"][0]["content"].path),
                "brother_college_major": i["brother_college_major"],
                "brother_college_name": i["brother_college_name"],
                "name": i["title"],
                "brother_is_ask": i["brother_is_ask"],
                "brother_is_share": i["brother_is_share"],
                # TODO: 如何使用url_for优雅地拼接详情页的url
                # "details_link": url_for('quokka.core.detail', long_slug=i.slug)
                "details_link": "/brothers/" + i.slug + ".html"
            }
            brother_list.append(tmp)

        return _base_normal_resp(data=brother_list)
