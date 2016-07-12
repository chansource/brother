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
from wechat_sdk import WechatConf, WechatBasic
import json
from Sign import Sign
from flask import current_app

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
    """获取师兄列表

        采用GET请求方式。

    GET参数:
        order: 排序规则，time按时间排序，hot按点赞数排序
        offset: 起始偏移量
        count: 返回结果数量

    """

    def get(self):
        offset = int(request.args.get("offset", 0))
        count = int(request.args.get("count", 10))
        order_type = request.args.get("order", "")
        order_map = {"time": "-created_at", "hot": "-like_numbers"}
        ordering = order_map[order_type]
        logger.debug("offset-{} count-{} ordering-{}".format(offset,count,ordering))
        if ordering:
            # 先查询有order字段不为0的，按照order字段排序
            now = datetime.datetime.now()
            filters = {
                'published': True,
                'available_at__lte': now,
                'order__ne': 0,
            }
            resultsa = BrotherInfo.objects(
                **filters).order_by("order")
            logger.debug("get %d ordered items", resultsa.count())
            # TODO: 这种聚合queryset的方式太挫了，找到更好的方式。（学习mongoengine使用）
            tmp = []
            for i in resultsa:
                tmp.append(i)
            resultsa = tmp
            # 再查询order字段为0的，按照time或hot排序
            filters = {
                'published': True,
                'available_at__lte': now,
                'order': 0,
            }
            resultsb = BrotherInfo.objects(
                **filters).order_by(ordering)
            logger.debug("get %d unordered items", resultsb.count())
            # TODO: 这种聚合queryset的方式太挫了，找到更好的方式。（学习mongoengine使用）
            tmp = []
            for i in resultsb:
                tmp.append(i)
            resultsb = tmp
            # 拼接两次查询的列表，并按照offset和count截取结果
            results = (resultsa + resultsb)[offset : offset + count]
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

class TopicsView(MethodView):
    """获取话题列表

        采用GET请求方式。

    GET参数:
        offset: 起始偏移量
        count: 返回结果数量
    """
    def get(self):
        offset = int(request.args.get("offset", 0))
        count = int(request.args.get("count", 10))
        results = Topic.objects.skip(offset).limit(count)
        rtn_list = []
        for i in results:
            tmp = {
                "cover_img": url_for('quokka.core.media', filename=i["contents"][0]["content"].path),
                "title": i["title"],
                "summary": i["summary"],
                # TODO: 如何使用url_for优雅地拼接详情页的url
                # "details_link": url_for('quokka.core.detail', long_slug=i.slug)
                "link": "/topics/" + i.slug + ".html"
            }
            rtn_list.append(tmp)

        return _base_normal_resp(data=rtn_list)


class NewsView(MethodView):
    """获取动态列表

        采用GET请求方式。

    GET参数:
    
        offset: 起始偏移量
        count: 返回结果数量
    """
    def get(self):
        offset = int(request.args.get("offset", 0))
        count = int(request.args.get("count", 10))
        results = News.objects.skip(offset).limit(count)
        rtn_list = []
        for i in results:
            tmp = {
                "cover_img": url_for('quokka.core.media', filename=i["contents"][0]["content"].path),
                "title": i["title"],
                "summary": i["summary"],
                # TODO: 如何使用url_for优雅地拼接详情页的url
                # "details_link": url_for('quokka.core.detail', long_slug=i.slug)
                "link": "/news/" + i.slug + ".html"
            }
            rtn_list.append(tmp)

        return _base_normal_resp(data=rtn_list)

class WechatBaseView(MethodView):
    def __init__(self, *args, **kargs):
        conf = WechatConf(
            token=current_app.config.get("WECHAT")["token"],
            appid=current_app.config.get("WECHAT")["appid"],
            appsecret=current_app.config.get("WECHAT")["appsecret"],
            encrypt_mode=current_app.config.get("WECHAT")["encrypt_mode"],  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
            encoding_aes_key=current_app.config.get("WECHAT")["encoding_aes_key"],  # 如果传入此值则必须保证同时传入 token, appid
            access_token_getfunc=self._get_access_token_function,
            access_token_setfunc=self._set_access_token_function,
            jsapi_ticket_getfunc=self._get_jsapi_ticket_function,
            jsapi_ticket_setfunc=self._set_jsapi_ticket_function,
        )
        self.wechat = WechatBasic(conf=conf)

    def _get_access_token_function(self):
        """ 注意返回值为一个 Tuple，第一个元素为 access_token 的值，第二个元素为 access_token_expires_at 的值 """
        try:
            f = open(current_app.config.get("WECHAT")["access_token"], "r")
            content = f.read()
            access_token = json.loads(content)["access_token"]
            access_token_expires_at = json.loads(content)["access_token_expires_at"]
            f.close()
        except IOError, e:
            access_token = None
            access_token_expires_at = None

        return (access_token, access_token_expires_at)

    def _set_access_token_function(self, access_token, access_token_expires_at):
        f = open(current_app.config.get("WECHAT")["access_token"], "w")
        conent = json.dumps({
            "access_token": access_token,
            "access_token_expires_at": access_token_expires_at,
        })
        f.write(conent)
        f.close()

    def _get_jsapi_ticket_function(self):
        """ 注意返回值为一个 Tuple，第一个元素为 jsapi_ticket 的值，第二个元素为 jsapi_ticket_expires_at 的值 """
        try:
            f = open(current_app.config.get("WECHAT")["jsapi_ticket"], "r")
            content = f.read()
            jsapi_ticket = json.loads(content)["jsapi_ticket"]
            jsapi_ticket_expires_at = json.loads(content)["jsapi_ticket_expires_at"]
            f.close()
        except IOError, e:
            jsapi_ticket = None
            jsapi_ticket_expires_at = None

        return (jsapi_ticket, jsapi_ticket_expires_at)      

    def _set_jsapi_ticket_function(self, jsapi_ticket, jsapi_ticket_expires_at):
        f = open(current_app.config.get("WECHAT")["jsapi_ticket"], "w")
        conent = json.dumps({
            "jsapi_ticket": jsapi_ticket,
            "jsapi_ticket_expires_at": jsapi_ticket_expires_at,
        })
        f.write(conent)
        f.close()

class WechatCheckView(WechatBaseView):
    """接入验证请求"""
    def get(self):
        signature  = request.args.get("signature")
        timestamp  = request.args.get("timestamp")
        nonce  = request.args.get("nonce")

        if self.wechat.check_signature(signature, timestamp, nonce):
            logger.debug("wechat.check_signature success")
            return request.args.get("echostr")
        else:
           logger.error("wechat.check_signature failed")

class WechatJsView(WechatBaseView):
    """JS-SDK签名"""
    def get(self):
        jsapi_ticket = self.wechat.get_jsapi_ticket()
        sign = Sign(jsapi_ticket["jsapi_ticket"], request.args.get("url")).sign()
        return json.dumps(sign)
