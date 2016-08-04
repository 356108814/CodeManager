#coding: utf-8

from attr_object import EChartsObject

class Axis(EChartsObject):
	"""
	图表坐标轴
	"""
	def __init__(self,axis_type='category'):
		# 可选值'category' | 'value' | 'time' | 'log'
		self.type = axis_type				# 坐标轴类型，横轴默认为类目型'category'，纵轴默认为数值型'value'
		self.axisLabel = AxisLabel()		# AxisLabel
		self.data = []						# 数据


class AxisLabel(EChartsObject):
	"""
	坐标抽标签
	"""
	def __init__(self):
		self.formatter = ''					# 间隔名称格式器：{string}（Template） | {Function}


if __name__ == '__main__':
	axis = Axis()
	print axis.get_json()
		
