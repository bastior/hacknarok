from flask import Blueprint
from flask import render_template
from flask.views import MethodView

offer_blueprint = Blueprint('offer', __name__, template_folder='../templates/offers')


class AddOffer(MethodView):
    def get_template_name(self):
        return 'add_offer.html'

    def get(self):
        return render_template(self.get_template_name())

offer_blueprint.add_url_rule('/offers/add', view_func=AddOffer.as_view('add_offer'))
