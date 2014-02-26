########################################################################################################################
# File name: ddos_dst_entry_src_dst_pair_l4_type_src_dst.py
# Copyright(C) 2007-2013, A10 Networks Inc. All rights reserved.
# Software for all A10 products contain trade secrets and confidential
# information of A10 Networks and its subsidiaries and may not be
# disclosed, copied, reproduced or distributed to anyone outside of
# A10 Networks without prior written consent of A10 Networks, Inc.
########################################################################################################################
import sys
import json
sys.path.append("../common")
from axapi_common import *

BASE_URL = [
	'https://axapi.a10networks.com/axapi/v3/ddos/dst/entry/src-dst-pair/l4-type-src-dst',
]

def deserialize_L4_type_src_dst__template_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	tcp = data.get('tcp')
	udp = data.get('udp')
	result = L4_type_src_dst__template(tcp=tcp, udp=udp)
	return result

def deserialize_L4_type_src_dst_json(obj):
	if obj is None:
		return None
	if isinstance(obj, dict):
		data = obj
	else:
		data = json.loads(obj)
	protocol = data.get('protocol')
	glid = data.get('glid')
	template = deserialize_L4_type_src_dst__template_json(data.get('template'))
	result = L4_type_src_dst(protocol=protocol, glid=glid, template=template)
	return result

def serialize_L4_type_src_dst__template_json(obj):
	output = OrderedDict()
	if obj.tcp is not None:
		output['tcp'] = obj.tcp
	if obj.udp is not None:
		output['udp'] = obj.udp
	return output

def serialize_L4_type_src_dst_json(obj):
	output = OrderedDict()
	output['protocol'] = obj.protocol
	if obj.glid is not None:
		output['glid'] = obj.glid
	if obj.template is not None:
		output['template'] = serialize_L4_type_src_dst__template_json(obj.template)
	return output

def serialize_final_json(obj):
	return json.dumps(obj)

def deserialize_string_json(obj):
	if obj is None:
		return None
	if isinstance(obj, str):
		return json.loads(obj)
	return obj

def deserialize_list_L4_type_src_dst_json(obj):
	if obj is None:
		return None
	if isinstance(obj, list):
		data = obj
	else:
		data = json.loads(obj)
	container = []
	for item in data:
		container.append(deserialize_L4_type_src_dst_json(item))
	return list(container)

class L4_type_src_dst_protocol(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['tcp', 'udp', 'icmp', 'other'])
	def __init__(self, protocol):
		self.protocol = protocol

	def __str__(self):
		return str(self.protocol)

class L4_type_src_dst__template(AxapiObject):
	__metaclass__ = StructMeta 
	tcp=SizedString(1, 255)
	udp=SizedString(1, 255)
	def __init__(self, tcp=None, udp=None):
		self.tcp = tcp
		self.udp = udp

	def __str__(self):
		return ""

class L4_type_src_dst(AxapiObject):
	__metaclass__ = StructMeta 
	protocol = Enum(['tcp', 'udp', 'icmp', 'other'])
	glid=PosRangedInteger(1, 32000)
	def __init__(self, protocol, glid=None, template=None):
		self.protocol = protocol
		self.glid = glid
		self.template = template

	def __str__(self):
		return str(self.protocol)

class DdosDstEntrySrcdstpairL4typesrcdstClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def getDdosDstEntrySrcdstpairL4typesrcdst(self, l4_type_src_dst_protocol):
		"""
		Retrieve the l4_type_src_dst identified by the specified identifier
		
		Args:
			l4_type_src_dst_protocol L4_type_src_dst_protocol
		
		Returns:
			An instance of the L4_type_src_dst class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + str(l4_type_src_dst_protocol) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified l4_type_src_dst does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('l4-type-src-dst')
		return deserialize_L4_type_src_dst_json(payload)

	def putDdosDstEntrySrcdstpairL4typesrcdst(self, l4_type_src_dst_protocol, l4_type_src_dst):
		"""
		Replace the object l4_type_src_dst
		
		Args:
			l4_type_src_dst_protocol L4_type_src_dst_protocol
			l4_type_src_dst An instance of the L4_type_src_dst class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['l4-type-src-dst']=serialize_L4_type_src_dst_json(l4_type_src_dst)
		payload = serialize_final_json(output)
		conn.request('PUT', self.get_path() + '/' + str(l4_type_src_dst_protocol) .replace("/", "%2f") + query, payload, headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

	def deleteDdosDstEntrySrcdstpairL4typesrcdst(self, l4_type_src_dst_protocol):
		"""
		Remove the l4_type_src_dst identified by the specified identifier from the
		system
		
		Args:
			l4_type_src_dst_protocol L4_type_src_dst_protocol
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('DELETE', self.get_path() + '/' + str(l4_type_src_dst_protocol) .replace("/", "%2f") + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception', 404: 'Specified l4_type_src_dst does not exist'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

class AllDdosDstEntrySrcdstpairL4typesrcdstsClient(AbstractResourceClient):
	def __init__(self, endpoint=None, sessionid=None, ipaddress=None, debug=False):
		if not endpoint:
			if ipaddress:
				result = urlparse(BASE_URL[0])
				endpoint = result.scheme + '://' + ipaddress + result.path
		AbstractResourceClient.__init__(self, endpoint, sessionid, debug)

	def submitDdosDstEntrySrcdstpairL4typesrcdst(self, l4_type_src_dst):
		"""
		Create the object l4_type_src_dst
		
		Args:
			l4_type_src_dst An instance of the L4_type_src_dst class
		
		Returns:
			An instance of the string class
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		output=OrderedDict()
		output['l4-type-src-dst']=serialize_L4_type_src_dst_json(l4_type_src_dst)
		payload = serialize_final_json(output)
		conn.request('POST', self.get_path() + '/' + query, payload, headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		return deserialize_string_json(payload)

	def getAllDdosDstEntrySrcdstpairL4typesrcdsts(self):
		"""
		Retrieve all l4_type_src_dst objects currently pending in the system
		
		Returns:
			A list of L4_type_src_dst objects
		"""
		query = ''
		conn = self.get_connection()
		headers = { 'Content-type' : 'application/json', 'Authorization' : 'A10 %s' %self.sessionid}
		conn.request('GET', self.get_path() + '/' + query, headers=headers)
		response = conn.getresponse()
		expected_status = 200
		errors = {500: 'An unexpected runtime exception'}
		payload = self.get_output(response, expected_status, errors)
		conn.close()
		if self.debug:
			print 'payload:', payload
		if payload == '':
			payload = None
		if payload is not None:
			data = json.loads(payload)
			payload= data.get('l4-type-src-dstList')
		return deserialize_list_L4_type_src_dst_json(payload)

