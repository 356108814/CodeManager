#coding: utf-8

from attr_object import EChartsObject
from series_base import SeriesBase

class SeriesPie(SeriesBase):
	"""
	饼图系列数据
	"""
	def __init__(self):
		self.center = ['50%', '50%']
		self.radius = [0, '75%']

