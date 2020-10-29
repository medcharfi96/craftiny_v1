#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home_page():
    """Return html template containing home page"""
    return render_template('home.html')

@app.route('/whoweare')
def who_we_are():
    """Return html template containing who we are page"""
    return render_template('whoweare.html')

@app.route('/services')
def services():
    """Return html template containing services page"""
    return render_template('services.html')

@app.route('/projects')
def projects():
    """Return html template containing projects page"""
    return render_template('projects.html')

@app.route('/contactus')
def contact_us():
    """Return html template containing contact us page"""
    return render_template('contactus.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2002, debug=True)