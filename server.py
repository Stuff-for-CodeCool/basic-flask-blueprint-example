from flask import Flask, redirect, url_for
from sky import sky
from earth import earth

app = Flask(__name__)
app.register_blueprint(sky)
app.register_blueprint(earth)


@app.route("/")
def index():
    return redirect(url_for("sky.index"))


app.run(debug=True)
