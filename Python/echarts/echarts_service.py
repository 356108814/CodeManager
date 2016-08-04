# coding:utf-8

import logging

from echarts.echarts_line_bar import EChartsLineBar 


class EChartsService(object):
    """
    图表业务层基类
    """

    def __init__(self):
        # 日志
        self.logger = logging.getLogger('info')

    def get_line_bar_chart(self, title='', legend_name='', xAxis_name='', xAxis_data=[], series_name='', series_type='line', series_data=[]):
        """
        获取线图、柱状图图表对象
        @param title    标题
        @param legend_name 图例名称
        @param xAxis_name   x轴名称
        @param xAxis_data   x轴数据。数组
        @param series_name  系列名称
        @param series_type  系列类型
        @param series_data  系列数组。数组
        @return ECharts对象
        """
        # 线、柱状图
        echarts = EChartsLineBar()

        # 设置标题
        echarts.title.text = title

        # 设置图例
        echarts.legend.data = [legend_name]

        # 设置x轴。轴为数组
        echarts.xAxis[0].name = xAxis_name
        echarts.xAxis[0].data = xAxis_data

        # 设置系列。系列为数组
        series1 = echarts.series[0]
        series1.name = series_name
        series1.type = series_type
        series1.data = series_data

        return echarts

    def get_line_bar_chart_json(self, title='', legend_name='', xAxis_name='', xAxis_data=[], series_name='', series_type='line', series_data=[]):
        """
        获取线图、柱状图图表json数据
        @param title    标题
        @param legend_name 图例名称
        @param xAxis_name   x轴名称
        @param xAxis_data   x轴数据。数组
        @param series_name  系列名称
        @param series_type  系列类型
        @param series_data  系列数组。数组
        @return json字符串
        """
        echarts = self.get_line_bar_chart(title, legend_name, xAxis_name, xAxis_data, series_name, series_type, series_data)
        echarts.tooltip.formatter = u'%s：{b}<br>%s：{c}' % (xAxis_name, title)
        return echarts.get_json()

    def get_multi_line_bar_chart(self, title='', legend_name_list=[], xAxis_name='', xAxis_data=[], series_list=[]):
        """
        获取线图、柱状图多图例图表对象
        @param title    标题
        @param legend_name_list 图例名称数组
        @param xAxis_name   x轴名称
        @param xAxis_data   x轴数据。数组
        @param series_list  系列列表。dict数组
        @return ECharts对象
        """
        # 线、柱状图
        echarts = EChartsLineBar()

        # 设置标题
        echarts.title.text = title

        # 设置图例
        echarts.legend.data = legend_name_list

        # 设置x轴。轴为数组
        echarts.xAxis[0].name = xAxis_name
        echarts.xAxis[0].data = xAxis_data

        # 设置系列。系列为数组
        for index, series_dict in enumerate(series_list):
            if index == 0:
                series = echarts.series[0]
            else:
                series = echarts.new_series()
                echarts.series.append(series)
            series.name = series_dict['name']
            series.type = series_dict['type']
            series.data = series_dict['data']

        return echarts

    def get_multi_line_bar_chart_json(self, title='', legend_name_list=[], xAxis_name='', xAxis_data=[], series_list=[]):
        """
        获取线图、柱状图多图例图表json数据
        @param title    标题
        @param legend_name_list 图例名称数组
        @param xAxis_name   x轴名称
        @param xAxis_data   x轴数据。数组
        @param series_list  系列列表。dict数组
        @return json字符串
        """
        echarts = self.get_multi_line_bar_chart(title, legend_name_list, xAxis_name, xAxis_data, series_list)
        echarts.tooltip.formatter = u'%s：{b}<br>%s：{c}' % (xAxis_name, title)
        return echarts.get_json()
    

    

    
    



