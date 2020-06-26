from flask import Blueprint, request, abort
import validators

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

    url = format_urls_in_text(request.json['url'])

    link = Link(url=url)

    db.session.add(link)
    db.session.commit()

    return {"link": "https://estev.ao/u/" + link.slug, "slug": link.slug}


def format_urls_in_text(text):
    accepted_protocols = ['http://', 'https://']
    new_text = []

    for word in str(text).split():
        new_word = word
        accepted = [
            protocol for protocol in accepted_protocols if protocol in new_word
        ]

        if not accepted:
            new_word = 'http://{0}'.format(new_word)

        if not validators.url(new_word):
            new_word = word

        new_text.append(new_word)

    return ' '.join(new_text)
