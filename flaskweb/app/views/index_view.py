from flask import Blueprint, render_template, request
from ..db import get_db_connection

bp = Blueprint('web_index', __name__, url_prefix='/')

@bp.route('/', methods=('GET','POST'))
def index():
    conn = get_db_connection()
    if request.method == 'POST':
        search_type = request.form['search_type']
        search_name = request.form['search_name']
        with conn.cursor() as cursor:
            if search_type == 'all':
                cursor.execute(f"SELECT * FROM posts WHERE title LIKE '%{search_name}%' OR content LIKE '%{search_name}%' OR writer LIKE '%{search_name}%'")
            else:
                cursor.execute(f"SELECT * FROM posts WHERE {search_type} LIKE '%{search_name}%'")
                    
            posts = cursor.fetchall()
    else:     
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, title, writer, created_at FROM posts ORDER BY id DESC")
            posts = cursor.fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

