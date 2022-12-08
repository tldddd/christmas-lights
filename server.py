import json
from flask import Flask, jsonify, request
from app import App


api = Flask(__name__)

# Create the app.
app = App()


@api.route("/lights", methods=["GET"])
def get_lights():
    lights = app.get_lights()
    lights_dict = [l.__dict__ for l in lights]
    return jsonify(lights_dict)


@api.route("/lights", methods=["POST"])
def set_light():
    data = json.loads(request.data)
    id: int = data["id"]
    state: bool = data["state"]
    light = app.set_light(id, state)

    return jsonify(light.__dict__)


@api.route("/sequences", methods=["GET"])
def get_sequences():
    seqs = app.get_sequences()
    # seqs_dict = [l.__dict__ for l in seq]
    seqs_dict = get_json(seqs)
    return jsonify(seqs_dict)


@api.route("/sequences", methods=["POST"])
def start_seq():
    data = json.loads(request.data)
    name: int = data["name"]
    seq = app.start_seq(name)
    seqs_dict = get_json(seq)
    return jsonify(seqs_dict)


def get_json(obj):
    return json.loads(
        json.dumps(obj, default=lambda o: getattr(o, "__dict__", str(o)))
    )


if __name__ == "__main__":
    api.run(host="0.0.0.0")
