'''
Matthew Ragan | matthewragan.com
'''

import json

class Heartbeat:
	'''
		This is a sample class.

		This sample class has several important features that can be described here.


		Notes
		---------------
		Your notes about the class go here
 	'''

	def __init__(self, myOp):
		self.Active 		= parent().par.Active
		self.HeartbeatRole 	= parent().par.Heartbeatrole
		self.Udp_out		= op('udpout1')
		self.Udp_in 		= op('udpin1')
		pass
	
	def Request_hb(self):
		Controller 			= 1 if self.HeartbeatRole.eval() == 'controller' else 0

		if Controller:
			msg = {"heart_beat":"hello"}
			self.Udp_out.sendBytes(str(msg))
		else:
			pass
		pass
	
	def Send_hb(self, msg):
		pass

	def Process_msg(self, msg, debug=False):
		json_msg = json.dumps(msg)
		
		if debug:
			print(json_msg)
		pass
