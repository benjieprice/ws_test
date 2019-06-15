from tornado import websocket
import tornado.ioloop
import json

class PaintWebsocket(websocket.WebSocketHandler):

	paintings = {}
	def open(self):
		print "Websocket Opened"

	def on_message(self, message):
		if(message.startswith('handshake')):
			self.handshake(message)
		else:
			self.update_paintings(message)
		

	def on_close(self):
		print "Websocket closed"

	def check_origin(self, origin):
		return True

	def update_paintings(self, message):
		user, paint = message.split(":")
		print self.paintings
		if user in self.paintings:
			self.paintings[user]["paint"] += ";" + paint
		else:
			self.paintings[user]["paint"] = paint
		self.write_message(message)

	def handshake(self,hsMessage):
		print hsMessage
		print self.paintings
		hsh = hsMessage.split(":")
		if(len(hsh) == 3):
			self.paintings[hsh[1]] = { "color" : hsh[2], "paint": ''}
		else:
			self.write_message(u"handshake: %s" % json.dumps(self.paintings))


application = tornado.web.Application([(r"/paint", PaintWebsocket),])

if __name__ == "__main__":
	application.listen(9000)
	tornado.ioloop.IOLoop.instance().start()