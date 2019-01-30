'''
Matthew Ragan | matthewragan.com
'''

class Heartbeat:
	'''
		This is a sample class.

		This sample class has several important features that can be described here.


		Notes
		---------------
		Your notes about the class go here
 	'''

	def __init__(self, myOp):
		self.MyOp 			= myOp

		self.Active 		= parent().par.Active
		self.HeartbeatRole 	= parent().par.Heartbeatrole
		self.ComCOMP 		= parent().par.Communicationcomp

		print("Heartbeat init")
		pass

	def Role_setup(self, role_par):
		if role_par == "node":
			op('lfo1').bypass = True
			pass
		else:
			op('lfo1').bypass = False
			pass
		pass

	def Request_hb(self):
		Controller 			= 1 if self.HeartbeatRole.eval() == 'controller' else 0

		if Controller:

			msg = {
				'messagekind'	: "Send_hb",
				'target'		: "all",
				'sender'		: self.HeartbeatRole.eval(),
				'output'		: None,
				'parameter'		: None,
				'value'			: None
				}

			op(self.ComCOMP).Send_msg(msg)
		else:
			pass
		pass
	
	def Send_hb(self, msg):
		out_msg = {
			'messagekind'	: "Hb_response",
			'target'		: msg.get("sender"),
			'sender'		: self.HeartbeatRole.eval(),
			'output'		: None,
			'parameter'		: None,
			'value'			: {
				"hostname"		: op(self.ComCOMP).Hostname,
				"ip_address" 	: op(self.ComCOMP).Ipaddress,
				"fps"			: None,
				"perform_mode"	: ui.performMode
			}
		}

		op(self.ComCOMP).Send_msg(out_msg)

		pass

	def Hb_response(self, msg):
		Controller 			= 1 if self.HeartbeatRole.eval() == 'controller' else 0
		if Controller:
			print(msg)
		else:
			pass
		pass
	


