from flask import Blueprint, render_template
from ..db import get_db_connection

bp = Blueprint('web_detail', __name__, url_prefix='/view')

@bp.route('/<int:post_id>')
def view(post_id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM posts WHERE id = {post_id}")
        post = cursor.fetchone()
    conn.close()
    return render_template('view.html', post=post)