# coding: utf-8

from quokka.core.app import QuokkaModule
from views import AddLikeView, SendMessageView, JoinMessageView, BrotherInfoView

module = QuokkaModule("brothers", __name__, template_folder="templates")

module.add_url_rule('/brothervideos/addlike', view_func=AddLikeView.as_view('addlike'))
module.add_url_rule('/brotherask/sendmessage', view_func=SendMessageView.as_view('sendmessage'))
module.add_url_rule('/joinmessages/sendmessage', view_func=JoinMessageView.as_view('joinmessage'))
module.add_url_rule('/brotherinfo', view_func=BrotherInfoView.as_view('brotherinfo'))