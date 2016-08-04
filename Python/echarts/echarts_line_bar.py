# coding:utf-8

from attr_object import EChartsObject
from base import ECharts
from series_base import SeriesBase
from series_line_bar import SeriesLineBar
from axis import Axis


class EChartsLineBar(ECharts):
	"""
	直角系图表
	"""

	def __init__(self, title_text='', title_subtext = ''):
		super(EChartsLineBar, self).__init__(title_text, title_subtext)
		self.xAxis = [Axis('category')]
		self.yAxis = [Axis('value')]
		self.series = [SeriesLineBar()]


	def new_series(self):
		"""
		新建一个系列
		"""
		return SeriesLineBar()

if __name__ == '__main__':
	ec = EChartsLineBar()
	print ec.get_json()

