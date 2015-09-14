from utils import appendKey
from flask import *

album = Blueprint('album', __name__, template_folder='views')

@album.route(appendKey('/album/edit'))
def album_edit_route():
	options = {
		"edit": True
	}
	return render_template("album.html", **options)

@album.route(appendKey('/album'))
def album_route():
	options = {
		"edit": False
	}
	return render_template("album.html", **options)