# coding: utf-8

from quokka.core.app import QuokkaModule
from views import AddVideoLikeView, AddArticleLikeView, SendMessageView, JoinMessageView, BrotherInfoView,AddBrotherLikeView

module = QuokkaModule("brothers", __name__, template_folder="templates")

module.add_url_rule('/brothers/addlike', view_func=AddBrotherLikeView.as_view('addbrotherlike'))
module.add_url_rule('/brothervideos/addvideolike', view_func=AddVideoLikeView.as_view('addvideolike'))
module.add_url_rule('/brotherarticles/addarticlelike', view_func=AddArticleLikeView.as_view('addarticlelike'))
module.add_url_rule('/brotherask/sendmessage', view_func=SendMessageView.as_view('sendmessage'))
module.add_url_rule('/joinmessages/sendmessage', view_func=JoinMessageView.as_view('joinmessage'))
module.add_url_rule('/brotherinfo', view_func=BrotherInfoView.as_view('brotherinfo'))
