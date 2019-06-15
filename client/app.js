var webSocket   = null;

function openWsConnection(handshake, callback){
		url = "ws://localhost:9000/paint";
		console.log('starting connection to: ' + url)
		try{
			webSocket = new WebSocket(url)
			webSocket.onopen = function(openEvent){
				handshake()
				console.log("Websocket OPEN:" + JSON.stringify(openEvent, null, 4))
			}
			webSocket.onclose = function(closeEvent){
				console.log("Websocket CLOSE:" + JSON.stringify(closeEvent, null, 4))
			}
			webSocket.onerror = function(errorEvent){
				console.error("Websocket ERROR:" + JSON.stringify(errorEvent, null, 4))
			}
			webSocket.onmessage = function(messageEvent){
				console.log("Websocket MESSAGE:" + JSON.stringify(messageEvent, null, 4))
				var message = messageEvent.data
				callback(message)
			}

		}catch(err){
			console.error(err)
		}
	}
