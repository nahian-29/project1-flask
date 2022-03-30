"""A simple flask web app"""
from flask import Flask, render_template


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    @app.route("/")
    @app.route("/base.html")
    def index():
        return render_template('base.html')
    @app.route("/git.html")
    def gitPage():
        return render_template('git.html')
    @app.route("/docker.html")
    def dockerPage():
        return render_template('docker.html')
    @app.route("/python.html")
    def pythonPage():
        return render_template('python.html')
    @app.route("/cicd.html")
    def cicdPage():
        return render_template('cicd.html')
    @app.route("/glossary.html")
    def glossaryPage():
        return render_template('glossary.html')
    @app.route("/aaatesting.html")
    def AAATestingPage():
        return render_template('aaatesting.html')
    @app.route("/oops.html")
    def OOPsPage():
        return render_template('oops.html')
    @app.route("/solid.html")
    def SOLIDPage():
        return render_template('solid.html')

    return app
