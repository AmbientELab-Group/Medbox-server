from flask import Flask
import api

app = Flask(__name__)

app.register_blueprint(api.auth.auth_api)

if __name__ == '__main__':
    app.run(debug=True, port='8000', host='0.0.0.0')
