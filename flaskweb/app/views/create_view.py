from flask import Blueprint, render_template, request, url_for, redirect
from ..db import get_db_connection

bp = Blueprint('web_create', __name__, url_prefix='/create')

@bp.route('/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        writer = request.form['writer']
        password = request.form['password']
        if title and content and writer and password:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"INSERT INTO posts (title, content, writer, password) VALUES ('{title}', '{content}', '{writer}', '{password}')")
                conn.commit()
            conn.close()
            return redirect(url_for('web_index.index'))
        else:
            return "<script>alert('빈칸이 존재합니다.');history.back(-1);</script>"
    return render_template('create.html')