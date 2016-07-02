# coding: utf-8

from quokka.core.app import QuokkaModule
from views import AddTopicVideoLikeView, AddNewsArticleLikeView, SendMessageView, JoinMessageView, BrotherInfoView, BrotherLikeView, TopicsView, NewsView

module = QuokkaModule("brothers", __name__, template_folder="templates")

module.add_url_rule('/brothers/like', view_func=BrotherLikeView.as_view('brotherlike'))
module.add_url_rule('/topic/like', view_func=AddTopicVideoLikeView.as_view('topiclike'))
module.add_url_rule('/news/like', view_func=AddNewsArticleLikeView.as_view('newslike'))
module.add_url_rule('/brotherask/sendmessage', view_func=SendMessageView.as_view('sendmessage'))
module.add_url_rule('/joinmessages/sendmessage', view_func=JoinMessageView.as_view('joinmessage'))
module.add_url_rule('/brotherinfo', view_func=BrotherInfoView.as_view('brotherinfo'))
module.add_url_rule('/topicsinfo', view_func=TopicsView.as_view('topicsinfo'))
module.add_url_rule('/newsinfo', view_func=NewsView.as_view('newsinfo'))
