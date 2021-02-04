import html
from flask import Blueprint, current_app, session, request, render_template

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route('')
def landing_page() -> 'html':
    current_app.logger.info("accessing home page")
    session['ip'] = request.remote_addr
    return render_template('index.html')
