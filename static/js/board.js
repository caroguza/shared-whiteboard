var boardSocket = new WebSocket('ws://' + window.location.host + '/')

boardSocket.onclose = event => {
    console.error('Chat socket closed unexpectedly')
};

/*Board*/
let canvas = false
let ctx = false
let flag = false
let prevX = 0
let currX = 0
let prevY = 0
let currY = 0
let dotFlag = false
let strokeCoordenates = []
let currentColor
let inkColor = "black"
let strokeWidth = 2

document.getElementsByClassName('user')[0].innerText = username

init = () => {
    canvas = document.getElementById('canvas-board')
    ctx = canvas.getContext("2d")
    w = canvas.width
    h = canvas.height

    canvas.addEventListener("mousemove", function (e) {
        setCoordenates('move', e)
    }, false);
    canvas.addEventListener("mousedown", function (e) {
        setCoordenates('down', e)
    }, false);
    canvas.addEventListener("mouseup", function (e) {
        setCoordenates('up', e)
    }, false);
    canvas.addEventListener("mouseout", function (e) {
        setCoordenates('out', e)
    }, false);
}

erase = obj => {
    $('#canvas-board').addClass('erase')
    
    currentColor = inkColor
    inkColor = "white"
    strokeWidth = 14
    
}

setColor = obj => {
    $('.color').removeClass('selected-color')
    $(obj).addClass('selected-color')
    
    switch (obj.id) {
        case "green":
            inkColor = "green"
            break;
        case "blue":
            inkColor = "blue"
            break;
        case "red":
            inkColor = "red"
            break;
        case "yellow":
            inkColor = "yellow"
            break;
        case "orange":
            inkColor = "orange"
            break;
        case "black":
            inkColor = "black"
            break;
        case "white":
            inkColor = "white"
            break;
    }
    if (inkColor == "white") strokeWidth = 14;
    else strokeWidth = 2;
}

usePencil = () => {
    $('#canvas-board').removeClass('erase')
    inkColor = currentColor
    strokeWidth = 2
}

draw = () => {
    // console.log('start draw()', prevX, prevY, currX, currY)

    ctx.beginPath()
    ctx.moveTo(prevX, prevY)
    ctx.lineTo(currX, currY)
    ctx.strokeStyle = inkColor
    ctx.lineWidth = strokeWidth
    ctx.stroke()
    ctx.closePath()

}

drawPoint = () => {
    ctx.beginPath()
    ctx.fillStyle = inkColor
    ctx.fillRect(currX, currY, 2, 2)
    ctx.closePath()
}

sendCoordenates = () => {
    if (strokeCoordenates != '') {
        boardSocket.send(JSON.stringify({
            'action': 'draw',
            'coordenates': strokeCoordenates,
            'username': username,
            'color': inkColor
        }))
    }
    strokeCoordenates = []
}

saveImage = (image_name) => {
    boardSocket.send(JSON.stringify({
        'action': 'save',
        'image_name': image_name,
        'username': username
    }))
}

loadImage = (image_name) => {
    boardSocket.send(JSON.stringify({
        'action': 'load',
        'image_name': image_name,
        'username': username
    }))
}

clearBoard = () => {
    ctx.clearRect(0, 0, w, h)
    boardSocket.send(JSON.stringify({
        'action': 'clear',
        'username': username
    }))
}

setCoordenates = (res, e) => {
    if (res == 'down') {
        prevX = currX
        prevY = currY
        currX = e.clientX - canvas.offsetLeft
        currY = e.clientY - canvas.offsetTop

        flag = true
        dotFlag = true
        if (dotFlag) {
            drawPoint()
            dotFlag = false
        }
    }
    if (res == 'up' || res == "out") {
        flag = false
    }
    if (res == 'up') {
        coordenates = {'prevX': currX, 'prevY': currY, 'x': currX, 'y': currY, 'is_point': 1}
        strokeCoordenates.push(coordenates)
        sendCoordenates()
    }
    if (res == 'move') {
        if (flag) {
            prevX = currX
            prevY = currY
            currX = e.clientX - canvas.offsetLeft
            currY = e.clientY - canvas.offsetTop
            draw()
            coordenates = {'prevX': prevX, 'prevY': prevY, 'x': currX, 'y': currY, 'is_point': 0}
            strokeCoordenates.push(coordenates)
        }
    }
}

boardSocket.onmessage = event => {
    message = JSON.parse(event.data)
    strokes = message['strokes']
    for (stroke of strokes) {
        prevX = stroke.prev_x
        prevY = stroke.prev_y
        currX = stroke.coordenate_x
        currY = stroke.coordenate_y
        inkColor = stroke.inkColor
        // console.log(prevX, prevY, currX, currY)
        draw()
    }
};

document.addEventListener('DOMContentLoaded', init(), false)