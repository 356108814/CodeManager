#coding: utf-8

from attr_object import EChartsObject

class Legend(EChartsObject):
	"""
	图表图例
	"""
	def __init__(self):
		"""
		数组项通常为{string}
		如需个性化图例文字样式，可把数组项改为{Object}，指定文本样式和个性化图例icon，格式为 
		{
		  name : {string}, 
		  textStyle : {Object}, 
		  icon : {string}
		}
		"""
		self.data = []

		