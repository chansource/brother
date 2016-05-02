# coding: utf-8

from quokka.core.app import QuokkaModule
from views import AddLikeView

module = QuokkaModule("brothers", __name__, template_folder="templates")

module.add_url_rule('/brothervideos/addlike', view_func=AddLikeView.as_view('addlike'))
