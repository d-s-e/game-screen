import json

from dataclasses import dataclass
from flask import Flask, jsonify
from flask import render_template, request


DEBUG = True

APP_INFO = {
    "name": "GameScreen",
    "version": "0.1.0"
}

@dataclass
class Layer:
    id: str
    name: str
    inverted: bool
    active: bool


# ----- START dynamic data -----

system_layers = {
    "_dark": Layer("_dark", "dark", False, False),
    "_bright": Layer("_bright", "bright", False, False),
}

preset_layers = {
    "section-red": Layer("section-red", "Red Section", True, False),
    "section-blue": Layer("section-blue", "Blue Section", True, False),
    "section-yellow": Layer("section-yellow", "Yellow Section", True, False),
    "section-elevator": Layer("section-elevator", "Elevator Section", True, False),
}

layers = {}
layers.update(system_layers)
layers.update(preset_layers)

current_preset = "Nemesis Lockdown Surface"
brightness = 100

# ----- END dynamic data -----


app = Flask(__name__)
log = app.logger


@app.route("/")
@app.route("/projector/")
def page_projector():
    return render_template('projector.html')


@app.route('/control/')
def page_control():
    return render_template('control.html', app_info=APP_INFO, current_preset=current_preset,
                           layers=layers.values(), brightness=brightness)


@app.get("/api/control/status/")
def api_control_status():
    return {
        "layers": layers,
        "brightness": brightness,
        "current_preset": current_preset,
    }, 200


@app.post("/api/control/toggle/")
def api_control_toggle():
    layer_id = request.form["layer"]
    layers[layer_id].active = not layers[layer_id].active

    if layers["_dark"].active:
        layers["_bright"].active = False
    elif layers["_bright"].active:
        layers["_dark"].active = False

    return {"action": "toggle", "key": layer_id, "value": layers[layer_id].active}, 200


@app.post("/api/control/set/")
def api_control_set():
    brightness_value = int(request.form["brightness"])
    brightness = max(0, min(brightness_value, 100))

    return {"action": "set", "key": "brightness", "value": brightness}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=DEBUG)

