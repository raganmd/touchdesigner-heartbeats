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
		self.MyOp 				= myOp

		self.Active 			= parent().par.Active
		self.HeartbeatRole 		= parent().par.Heartbeatrole
		self.ComCOMP 			= parent().par.Communicationcomp
		self.Cluster 			= parent().par.Cluster
		self.Cluster_machines 	= op('null_cluster_machines')
		self.Status_table 		= op('table_status')
		self.Perform_chop 		= op('perform1')

		self.Status_headers 	= ["hostname", "ip_address", "fps", "perform_mode"]
		self.Status_setup()

		print("Heartbeat init")
		pass

	def Status_setup(self):
		# clear table
		self.Status_table.clear()
		
		# insert headers
		self.Status_table.appendRow(self.Status_headers)
		
		# loop through reference table of network machines and create a row
		for each_machine in self.Cluster_machines.cols(0)[0][1:]:
			self.Status_table.appendRow([each_machine])
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
				"fps"			: self.Perform_chop['fps'][0],
				"perform_mode"	: ui.performMode
			}
		}

		op(self.ComCOMP).Send_msg(out_msg)

		pass

	def Hb_response(self, msg):
		Controller 			= 1 if self.HeartbeatRole.eval() == 'controller' else 0
		received_vals 		= msg.get("value")
		if Controller:
			for msg_keys, msg_vals in received_vals.items():
				target_row 	= received_vals.get("hostname")
				self.Status_table[target_row, msg_keys] = msg_vals
		else:
			pass
		pass
	


