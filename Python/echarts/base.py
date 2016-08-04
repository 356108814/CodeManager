# coding:utf-8

from attr_object import EChartsObject
from title import Title
from toolbox import ToolBox
from tooltip import ToolTip
from legend import Legend
from axis import Axis
from series_base import SeriesBase


class ECharts(EChartsObject):
	"""
	图表
	"""

	def __init__(self, title_text='', title_subtext = ''):
		"""
		@param title_text 		标题
		@param title_subtext	副标题
		"""
		self.title = Title()
		self.tooltip = ToolTip()
		self.toolbox = ToolBox()
		self.calculable = 'true'
		self.legend = Legend()
		# self.xAxis = [Axis('category')]
		# self.yAxis = [Axis('value')]
		self.series = [SeriesBase()]

		# 初始化
		self.title.text = title_text
		self.title.subtext = title_subtext


	def get_dict(self):
		"""
		获取dict
		"""
		data_dict = super(ECharts, self).get_dict()

		# 对数组xAxis、yAxis、series进行再处理
		if data_dict.has_key('xAxis') and data_dict['xAxis'] != None:
			data_dict['xAxis'] = self.ec_obj_list_to_dict_list(data_dict['xAxis'])

		if data_dict.has_key('yAxis') and data_dict['yAxis'] != None:
			data_dict['yAxis'] = self.ec_obj_list_to_dict_list(data_dict['yAxis'])

		data_dict['series'] = self.ec_obj_list_to_dict_list(data_dict['series'])

		return data_dict


	def ec_obj_list_to_dict_list(self,ec_obj_list):
		"""
		图表属性对象转dict数组
		@param ec_obj_list EChartsObject数组
		"""
		dict_list = []
		for i, eco in enumerate(ec_obj_list):
			dict_list.append(eco.get_dict())
		return dict_list


if __name__ == '__main__':
	ec = ECharts()
	print ec.get_json()

