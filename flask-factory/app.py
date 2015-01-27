from flask import Flask
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware


# app factory
def create_app(name):
    app = Flask(name)

    @app.route("/")
    def index():
        return "WASSUP {}".format(name)

    return app

main_app = create_app("MAIN")
trill_app = create_app("TRILL")

multi_app = DispatcherMiddleware(main_app,
    {
        "/trill" : trill_app
    })

if __name__ == "__main__":
    run_simple("localhost", 8080, multi_app, use_reloader=True)
