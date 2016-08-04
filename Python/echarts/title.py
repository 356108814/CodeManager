#coding: utf-8

from attr_object import EChartsObject

class Title(EChartsObject):
	"""
	图表标题
	"""
	def __init__(self):
		self.text = ''
		self.subtext = ''
		self.x = ''					# 值为left、center、right
		self.y = ''					# 值为top、center、bottom


if __name__ == '__main__':
	t = Title()
	print t.get_json()