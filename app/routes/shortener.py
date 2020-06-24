from flask import Blueprint, request, abort

from app.extensions.database import db
from app.models.link import Link

short = Blueprint('short', __name__)

@short.route('/links/<slug>', methods=['GET'])
def get_url(slug):
    """GET the url from a slug"""
    link = Link.query.filter_by(slug=slug).first_or_404()

    link.visits = link.visits + 1
    db.session.commit()

    return {"url": link.url}


@short.route('/links', methods=['POST'])
def create_slug():
    """POST a new slug for a url"""
    if not request.json or not 'url' in request.json:
        abort(400)

    link = Link(url=request.json['url'])

    db.session.add(link)
    db.session.commit()

    return {"link": "https://estev.ao/u/" + link.slug}
