# coding: utf-8

import json

class EChartsObject(object):
	"""
	图表项基类
	"""
	
	def __init__(self):
		pass
		

	def get_dict(self):
		"""
		获取dict
		"""
		attr_dict = {}

		for (attr, value) in self.__dict__.items():
			# 去掉''、空数组、空dict
			if value == '':
				continue

			if isinstance(value, list) or isinstance(value, dict):
				if len(value) == 0:
					continue

			if isinstance(value, EChartsObject):
				value_dict = value.get_dict()
				if len(value_dict) > 0:
					attr_dict[attr] = value_dict
			else:
				attr_dict[attr] = value

		return attr_dict

	def get_json(self):
		"""
		获取json格式数据
		"""
		data_dict = self.get_dict()
		json_data = json.dumps(data_dict)
		# 替换"true"为true，以符合echart的格式
		json_data = json_data.replace('\"true\"', 'true').replace('\"false\"', 'false')
		return json_data
