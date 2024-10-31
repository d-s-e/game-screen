/* GameScreen Projector */

let offset = "0"

document.addEventListener("DOMContentLoaded", e => {
    const darkBrightLayer = document.getElementById("dark_bright")
    const sse = new EventSource("/api/projector/sse/")

    sse.addEventListener("update", event => {
        const data = JSON.parse(event.data)

        switch (data.action) {
            case "toggle":
                if (data.key.startsWith("_")) {
                    if (data.key === "_dark" && data.value === true) {
                        darkBrightLayer.classList.add("black")
                        darkBrightLayer.classList.remove("white")
                    }
                    else if (data.key === "_bright" && data.value === true) {
                        darkBrightLayer.classList.add("white")
                        darkBrightLayer.classList.remove("black")
                    }
                    else {
                        darkBrightLayer.classList.remove("black")
                        darkBrightLayer.classList.remove("white")
                    }
                }
                else {
                    document.getElementById(data.key).style.opacity = data.value ? "1.0" : offset
                }
                break

            case "set":
                console.log(event.data)
                switch (data.key) {
                    case "brightness":
                        document.getElementById("dimmer").style.opacity = (1.0 - data.value / 100).toFixed(2)
                        break
                    case "offset":
                        offset = (data.value / 100).toFixed(2)
                        break
                }
        }
    })
})
