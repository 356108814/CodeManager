# coding: utf-8

from attr_object import EChartsObject

class ToolBox(EChartsObject):
	"""
	图表工具箱
	"""
	def __init__(self):
		self.show = 'true'						# true、false
		self.feature = ToolBoxFeature()


class ToolBoxFeature(EChartsObject):
	"""
	工具箱启用功能
	"""
	def __init__(self):
		self.mark = {'show': 'true' }
		self.dataView = {'show': 'true', 'readOnly': 'false'}
		self.magicType = FeatureMagicType()
		# self.magicType = {'show' : 'false', 'title' : { 'line' : '折线图切换', 'bar' : '柱形图切换'}, 'type' : ['line', 'bar',] }
		self.restore = {'show' : 'true'}
		self.saveAsImage = {'show' : 'true'}


class FeatureMagicType(EChartsObject):
	"""
	动态类型切换
	"""
	def __init__(self):
		self.show = 'true'
		self.type = ['line', 'bar']
		self.option = {}

if __name__ == '__main__':
	toolbox = ToolBox()
	print toolbox.get_json()
