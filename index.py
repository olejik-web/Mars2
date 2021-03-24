from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>������ ����������� �����</h1>'


@app.route('/index')
def new_page():
    return '<h2>� �� ����� ����� ������ ������!</h2>'


@app.route('/promotion_image')
def promotion_page():
    return '''
    <!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" 
                    href="static/css/style.css">
                    <title>������, ����!</title>
                  </head>
                  <body>
                    <h1>��� ���, ����!</h1>
                    <img src='static/img/mars.jpg' alt="����� ������ ���� ���� ��������, �� �� �������">
                    <div class="alert alert-primary" role="alert">
                      ������������ ��������� �� �������.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      ������������ ���� ���� �������.
                    </div>
                    <div class="alert alert-success" role="alert">
                      �� ������� ���������� ������������ ���� �������.
                    </div>
                    <div class="alert alert-danger" role="alert">
                      � ������ � �����!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      �������������!
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')