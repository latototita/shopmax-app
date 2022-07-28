import os

from bottle import route, template, redirect, static_file, error, run

@route('/')
def handle_root_url():
    redirect('/home')

@route('/home')
def show_home():
    return template('index')


@route('/about')
def about():
    return template('about')

@route('/single')
def show_home():
    return template('single')

@route('/shop')
def show_home():
    return template('shop')

@route('/cart')
def show_home():
    return template('cart')

@route('/thanks')
def show_home():
    return template('thanks')

@route('/checkout')
def show_home():
    return template('checkout')


@route('/contact')
def make_request():
    # make an API request here
    
    return template('contact')


@route('/static/<filename>')
def send_css(filename):
    return static_file(filename, root='./static')


@error(404)
def error404(error):
    return template('error', error_msg='404 error. Nothing to see here')


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
