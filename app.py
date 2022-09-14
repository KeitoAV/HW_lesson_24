import os
from flask import Flask, request, abort, Response
from utils import get_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/")
def get_page() -> str:
    return '<h2>' + 'Lesson 24. Homework.' + '</h2>' + '\n' + \
           '<h3>' + 'Request examples:' + '</h3>' + '\n' + \
           '<p>' + '/perform_query/?cmd1=filter&val1=POST&cmd2=limit&val2=3&file_name=apache_logs.txt' + '</p>' + \
           '<p>' + '/perform_query/?cmd1=filter&val1=POST&cmd2=map&val2=0&file_name=apache_logs.txt' + '</p>' + \
           '<p>' + '/perform_query/?cmd1=filter&val1=POST&cmd2=unique&val2=""&file_name=apache_logs.txt' + '</p>' + \
           '<p>' + '/perform_query/?cmd1=filter&val1=POST&cmd2=sort&val2=desc&file_name=apache_logs.txt' + '</p>' + \
           '<p>' + '/perform_query/?cmd1=filter&val1=POST&file_name=apache_logs.txt' + '</p>' + \
           '<p>' + '/perform_query/?cmd1=regex&val1=images/\\w+\\.png&cmd2=sort&val2=asc&file_name=apache_logs.txt'


@app.route("/perform_query/")
def perform_query() -> Response:
    cmd1 = request.args.get('cmd1')
    val1 = request.args.get('val1')
    cmd2 = request.args.get('cmd2')
    val2 = request.args.get('val2')
    file_name = request.args.get('file_name')

    if not (cmd1 and val1 and file_name):
        abort(400, 'Недостаточно команд для выполнения запроса.')

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return abort(400, 'Файл не найден.')

    with open(file_path) as file:
        res = get_query(str(cmd1), str(val1), file)
        if cmd2 and val2:
            res = get_query(str(cmd2), str(val2), iter(res))

        return app.response_class("\n".join(res), content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
