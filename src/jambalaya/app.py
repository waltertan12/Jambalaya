import flask
import authentication

app = flask.Flask(__name__,
                static_path=None,
                static_url_path=None,
                template_folder=None,
                instance_path=None,
                instance_relative_config=False,
                root_path=None)

app.register_blueprint(authentication.login_user_blpnt)
