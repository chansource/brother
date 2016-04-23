# coding: utf-8

from quokka.core.app import QuokkaModule
from .views import BrotherListView, BrotherVideosView,BrotherProfileView,BrotherArticlesView


module = QuokkaModule("brothors", __name__, template_folder="templates")
module.add_url_rule('/brothor/videos/<brothor_id>/',
                    view_func=BrotherVideosView.as_view('brothor_videos'))
module.add_url_rule('/brothers/',
                    view_func=BrotherListView.as_view('brothers'))
module.add_url_rule('/brother/profile/<brother_id>/',
                    view_func=BrotherProfileView.as_view('brother_profile'))
module.add_url_rule('/brother/articles/<brother_id>',
                    view_func=BrotherArticlesView.as_view('brother_articles'))
