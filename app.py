from flask import Flask, jsonify, request, render_template
from Models import db, Streamers
from logging import exception



app = Flask(__name__, static_url_path="/static")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\streamers.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


# Aquí empiezan las rutas
@app.route("/")
def home():
    streamers = Streamers.query.all()
    streamers = [streamer.serialize() for streamer in streamers]
    return render_template("index.html", streamers=streamers)

@app.route("/api/streamers", methods=["GET"])
def getStreamers():
    try:
        streamers = Streamers.query.all()
        toReturn = [streamer.serialize() for streamer in streamers]
        return jsonify(toReturn), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@app.route("/api/streamer", methods=["GET"])
def getStreamerByName():
    try:
        nameStreamer = request.args["name"]
        streamer = Streamers.query.filter_by(name=nameStreamer).first()
        if not streamer:
            return jsonify({"msg": "Este streamer no existe"}), 200
        else:
            return jsonify(streamer.serialize()), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@app.route("/api/findstreamer", methods=["GET"])
def getStreamer():
    try:
        fields = {}
        if "name" in request.args:
            fields["name"] = request.args["name"]
        
        if "subs" in request.args:
            fields["subs"] = request.args["subs"]

        if "followers" in request.args:
            fields["followers"] = request.args["followers"]

        streamer = Streamers.query.filter_by(**fields).first()
        
        if not streamer:
            return jsonify({"msg": "Este streamer no existe"}), 200
        else:
            return jsonify(streamer.serialize()), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=4000)