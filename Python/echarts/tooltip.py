#coding: utf-8

from attr_object import EChartsObject

class ToolTip(EChartsObject):
	"""
	图表提示
	"""
	def __init__(self):
		self.trigger = 'item'			# 触发类型，默认数据触发item，可选为：'item' | 'axis'
		self.formatter = ''				# 内容格式器
