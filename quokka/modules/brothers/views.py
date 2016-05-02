# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import request
from flask.json import jsonify
from .models import BrotherVideos
from flask_wtf import csrf
from pprint import pprint

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
    def _base_err_resp(self, err_msg="Default error message.", err_rtn=1):
        resp = {
            "rtn": err_rtn,
            "msg": err_msg,
        }
        return jsonify(resp)

    def _base_normal_resp(self, data={}):
        resp = {
            "rtn": 0,
            "data": data,
        }
        return jsonify(resp)

    def post(self):
        try:
            content_id = request.form["id"]
            index = int(request.form["index"])

            result = BrotherVideos.objects(id=content_id).first()
            result.videos[index].like_numbers += 1
            result.save()

            return self._base_normal_resp()

        except Exception, e:
            return self._base_err_resp(str(e))

