'''
Matthew Ragan | matthewragan.com
'''
import socket
import json

class Com:
	'''
		This is a bare bones Communcation class.

		This sample class has several important features that can be described here.


		Notes
		---------------
		Your notes about the class go here
 	'''

	def __init__(self, myOp):
		self.MyOp 			= myOp
		self.Active 		= parent().par.Active
		self.Udp_out		= op('udpout1')
		self.Udp_in 		= op('udpin1')
		self.Hostname 		= None
		self.Ipaddress 		= None
		self.Get_set_network()
		print("Com init")
		pass

	def Get_set_network(self):

		self.Hostname 			= socket.gethostname()
		self.Ipaddress			= socket.gethostbyname(self.Hostname)
		parent().par.Hostname 	= self.Hostname
		parent().par.Ipaddress 	= self.Ipaddress

		pass


	def Role_setup(self, role_par):
		if role_par == "node":
			op('lfo1').bypass = True
			pass
		else:
			op('lfo1').bypass = False
			pass
		pass


	def Send_msg(self, pyobject):
		'''
		message = {
			'messagekind'	: ,
			'target'		: ,
			'sender'		: ,
			'output'		: ,
			'parameter'		: ,
			'value'			:
			}

		e.g.
		out_msg = {
			'messagekind'	: "Hb_response",
			'target'		: msg.get('sender'),
			'sender'		: op.Com.Hostname,
			'output'		: None,
			'parameter'		: None,
			'value'			: {
				"hostname"		: op.Com.Hostname,
				"ip_address" 	: op.Com.Ipaddress,
				"fps"			: None,
				"perform_mode"	: ui.performMode
			}
		}

		'''
		message 				= json.dumps(pyobject).encode('utf-8')

		self.Udp_out.sendBytes(message)

		pass

	def Receive_msg(self, str_msg):

		json_msg 			= json.loads(str_msg)

		parent().Processmessage(json_msg)
		pass

	def Processmessage(self, message, debug=False):
		'''
			Process a message call.

			Notes
			---------
			The functional blocks below differ from our previous approach in solving the
			challenges of good modular design in calling blocks functions across the
			network. The change here is to use python built-ins to determine if a function exists, 
			and then to call that function without going through a complex set of nested if/else 
			statements. Here hasattr and getattr are used to check the parent object for
			methods, and then to pass the message contents through to that target method.
			
			The assumption here is that the "messagekind" key matches the method to be called.
			For example, let's use the following as an example:

			message = {
				output			: None,
				messagekind		: Server_status,
				parameter		: None,
				value			: None,
				sender			: None
			}

			The incoming message is first parsed to extract the messagekind value: 
			"Server_status". We check to see if this is an attribute of the self.Target
			operator. If there is a matching method, we then call that function, and pass
			along the contents of message. If it's not a matching method we'll then log 
			an Invalid Call.


			Args
			---------
			message (dict):
			> The message dictionary - 
			> message = {
			> 	'output'			: None,
			> 	'messagekind'		: 'Server_status',
			> 	'parameter'			: None,
			> 	'value'				: None,
			> 	'sender'			: None
			> }

			Returns
			---------
			none		
		'''

		# Get incoming message elements
		incoming_messagekind 		= message.get('messagekind', None)
		incoming_output 			= message.get('output', None)
		incoming_parameter 			= message.get('parameter', None)
		incoming_value 				= message.get('value', None)
		incoming_sender 			= message.get('sender', None)

		# test to see if a matching method exists
		if hasattr(self.MyOp, incoming_messagekind):
			function 				= getattr(self.MyOp, incoming_messagekind)

			# call the method if it exists
			function(message)
		
		else:
			# return an invalid message if no matching method exists
			print("Invalid Call")
		
		pass