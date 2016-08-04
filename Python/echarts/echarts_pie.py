# coding:utf-8

from attr_object import EChartsObject
from base import ECharts
from series_base import SeriesBase
from series_pie import SeriesPie


class EChartsPie(ECharts):
	"""
	饼图
	"""

	def __init__(self, title_text='', title_subtext = ''):
		super(EChartsPie, self).__init__(title_text, title_subtext)
		self.series = [SeriesPie()]

		# 提示
		self.tooltip.formatter = "{a} <br/>{b} : {c} ({d}%)"

		# 改变默认工具
		self.toolbox.feature.magicType.type = ['pie', 'funnel']
		self.toolbox.feature.magicType.option = { 'funnel': {'x': '25%', 'width': '50%', 'funnelAlign': 'left', 'max': 1548}}


	def new_series(self):
		"""
		新建一个系列
		"""
		return SeriesPie()

	def get_SeriesPie(self):
		"""
		获取饼图的系列。注意：饼图只有一个系列
		@return 

		"""
		return self.series[0]


if __name__ == '__main__':
	ec = EChartsPie()
	print ec.get_json()

