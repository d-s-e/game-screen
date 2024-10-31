/* GameScreen Control Panel */

document.addEventListener("DOMContentLoaded", event => {
    get_current_status()
        .then(status => {
            console.log("status: ", status)
            if (status) {
                update_control("set", "brightness", status.brightness)
                for (const layer in status.layers) {
                    update_control("toggle", layer, status.layers[layer].active)
                }
            }
        })

})


document.addEventListener('htmx:afterRequest', event => {
  if (event.detail.successful) {
      const response = JSON.parse(event.detail.xhr.response)
      update_control(response.action, response.key, response.value)
  }
})


function update_control(action, key, value) {
      switch (action) {
          case "toggle":
              if (value) {
                  document.getElementById(key).classList.add("active")
              }
              else {
                  document.getElementById(key).classList.remove("active")
              }
              break

          case "set":
              document.getElementById(key).value = value
              break
      }
  }


async function get_current_status() {
    const response = await fetch("/api/control/status/");
    if (response.ok) {
        return await response.json();
    }
}