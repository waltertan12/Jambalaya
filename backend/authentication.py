import flask
import werkzeug.datastructures

login_user_blpnt = flask.Blueprint('login_user', __name__)

# TODO: check and see if there's a standard 'flask' way of doing this
@login_user_blpnt.route('/login', methods=['POST'])
def _login_user():
    headers = werkzeug.datastructures.Headers()
    if flask.request.form['username'] == 'admin' and flask.request.form['password'] == 'admin':
        res = flask.jsonify(hello='world')
        headers.add('token', '123456')
        res.headers = headers
        return res
    else:
        return flask.abort(401)

