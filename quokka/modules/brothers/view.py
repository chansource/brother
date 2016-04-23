#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.views import MethodView
from quokka.core.templates import render_template
from .utils import get_brothers,get_brother


class BrotherListView(MethodView):
    """
    Show a full list of brothors
    """

    def get(self):
        return render_template('brothers/list.html', brothers=get_brothers())


class BrotherVideoView(MethodView):
    """
    Show specific  brother videos
    """

    def get(self, brother_id):
        brother=get_brother(brother_id)
        return render_template('brothers/video_detail.html',
                               brother=brother)

class  BrotherProfileView(MethodView):
    """
    show specific brother profile
    """
    def get(self,brother_id):
        brother=get_brother(brother_id)
        return render_template('brothers/profile_detail.html',brother=brother)

class  BrotherArticlesView(MethodView):
    """
    show specific brother arctiles
    """
    def get(self,brother_id):
        brother=get_brother(brother_id)
        return render_template('brothers/article_detail.html',brother=brother)


