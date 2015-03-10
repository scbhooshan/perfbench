class UserContext:

	def __init__(self, name, deployments, scenarios, args):
		
		self.username = name
		#############################
		#      [ 
		#       {"HOS1.1" : 
		#	 {
		#		"uuid":'',
		#		"authurl":'',
		#		"tenant':'',
		#		"user":''
		#	 },
		#  	{ "CS8.5" : 
		#	 {
		#		"uuid":'',
		#		"authurl":'',
		#		"tenant':'',
		#		"user":''
		#	  }
		#	}
		#      ]
		#############################

		self.deployment = deployments

		#############################
		#      { "neutron" : [
		#		x,
		#		y
		#	    ],
		#  	  "nova" : [
		#		x,
		#		y
		#	    ]
		#	}
		#############################
		self.scenarios  = scenarios 

		self.results	= {}
		self.args	= args.copy()

import uuid

class RallyUtility:
	
	def deployment_create(self, deployment_friendly_name, 
			deployment_owner, 
			osc_type, 
			osc_auth_url, 
			osc_endpoint_type, 
			osc_region_name, 
			osc_tenant_name, 
			osc_tenant_user, 
			osc_tenant_password):

		return uuid.uuid4()

	def deployment_use(self, deployment_friendly_name):
		pass

	def deployment_delete(self, deployment_friendly_name):
		pass
	
	def deployment_check(self, deployment_friendly_name):
		pass

	def rally_scenarios_list(self, component_types = {'neutron', 'nova'}):
		scene_by_type_list = []	
		scene_neutron_tuple = ('neutron', 'sample_scene')
		scene_nova_tuple = ('nova', 'sample_scene')
		
		scene_by_type_list.append(scene_neutron_tuple)
		scene_by_type_list.append(scene_nova_tuple)

		return scene_by_type_list

	def rally_run_scenarios(self, deployment_friendly_name, scenario_listing = []):
		pass
	
	def rally_launch_report(self, task_id):
		pass



	
	