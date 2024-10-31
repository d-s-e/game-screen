import json
from flask import Flask
from flask import render_template, request, Response

from sse import SSEMessageQueue
from presets import Layer


from presets import nemesis_lockdown_surface, nemesis_lockdown


DEBUG = True

APP_INFO = {
    "name": "GameScreen",
    "version": "0.1.0"
}


# ----- START dynamic data -----

current_preset = nemesis_lockdown_surface

# ----- END dynamic data -----


system_layers = {
    "_dark": Layer("_dark", "Full Darkness", False, False, None),
    "_bright": Layer("_bright", "Full Light", False, False, None),
}

layers = {}
layers.update(system_layers)
layers.update(current_preset.layers)

brightness = 100
offset = 0

app = Flask(__name__)
log = app.logger

sse_queue = SSEMessageQueue()


@app.route("/")
@app.route("/projector/")
def page_projector():
    return render_template('projector.html',
                           layers=current_preset.layers.values(),
                           preset_id=current_preset.id)


@app.route('/control/')
def page_control():
    return render_template('control.html',
                           app_info=APP_INFO, preset_name=current_preset.name,
                           layers=layers.values(), brightness=brightness, offset=offset)


@app.get("/api/control/status/")
def api_control_status():
    return {
        "layers": layers,
        "brightness": brightness,
        "offset": offset,
        "preset": current_preset.name,
    }, 200


@app.post("/api/control/toggle/")
def api_control_toggle():
    layer_id = request.form["layer"]
    layers[layer_id].active = not layers[layer_id].active

    if layer_id == "_dark" and layers["_dark"].active:
        layers["_bright"].active = False
    elif layer_id == "_bright" and layers["_bright"].active:
        layers["_dark"].active = False

    data = {"action": "toggle", "key": layer_id, "value": layers[layer_id].active}
    sse_queue.announce(json.dumps(data))

    return data, 200


@app.post("/api/control/set/")
def api_control_set():
    data = {"action": "set"}

    if "brightness" in request.form:
        brightness_value = int(request.form["brightness"])
        brightness = max(0, min(brightness_value, 100))
        data["key"] = "brightness"
        data["value"] = brightness
    elif "offset" in request.form:
        offset_value = int(request.form["offset"])
        offset = max(0, min(offset_value, 50))
        data["key"] = "offset"
        data["value"] = offset

    sse_queue.announce(json.dumps(data))
    return data, 200


@app.get('/api/projector/sse/')
def listen():
    def stream():
        messages = sse_queue.listen()
        while True:
            msg = messages.get()
            yield msg

    return Response(stream(), mimetype='text/event-stream')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=DEBUG)
