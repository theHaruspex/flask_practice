from flask import Flask
from admin.views import admin

app = Flask(__name__)
app.register_blueprint(admin, url_prefix="/admin/")


@app.route('/')
def test():
    return "<h1>Test</h1>"


if __name__ == "__main__":
    app.run(debug=True)
