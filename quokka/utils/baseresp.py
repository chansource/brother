# -*- coding: utf-8 -*-
from flask.json import jsonify

def _base_err_resp(err_msg="Default error message.", err_rtn=1):
    resp = {
        "rtn": err_rtn,
        "msg": err_msg,
    }
    return jsonify(resp)

def _base_normal_resp(data={}):
    resp = {
        "rtn": 0,
        "data": data,
    }
    return jsonify(resp)