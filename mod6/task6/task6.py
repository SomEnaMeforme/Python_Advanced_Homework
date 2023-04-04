from flask import Flask, url_for

app = Flask(__name__)


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route('/hello')
def hello():
    return 'Hello'


@app.route('/hello/world')
def hello_world():
    return 'Hello, world!'


def site_map():
    links = []

    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return links


app.route('/bb')
def error():
    return 404


@app.errorhandler(404)
def page_not_found(e):
    links = site_map()
    response = 'Страница не найдена, на нашем сайте имеются следующие страницы, вы можете перейти к ним: <br>'
    base_url = '127.0.0.1:5000'
    for link in links:
        response += f'{link[1]} - {base_url}{link[0]}<br>'
    return response

if __name__ == '__main__':
    app.run()