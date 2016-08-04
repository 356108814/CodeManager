#coding: utf-8

from attr_object import EChartsObject

class Series(EChartsObject):
	"""
	驱动图表生成的数据内容数组
	"""
	def __init__(self):
		self.name = ''					# 系列名称，如启用legend，该值将被legend.data索引相关
		self.type = ''					# 图表类型，如：bar、line等
		self.data = []					# 数据

