from echarts.base import Base

class Gauge(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, attr, value, *,
              scale_range=None,
              angle_range=None, **kwargs):
        """

        :param name:
            图例名称
        :param attr:
            属性名称
        :param value:
            属性所对应的值
        :param scale_range:
            仪表盘数据范围
        :param angle_range:
            仪表盘角度范围
        :param kwargs:
        """
        self._option.update(tooltip={"formatter": "{a} <br/>{b} : {c}%"})
        _min, _max = 0, 100
        if scale_range:
            if len(scale_range) == 2:
                _min, _max = scale_range
        _start, _end = 225, -45
        if angle_range:
            if len(angle_range) == 2:
                _start, _end = angle_range
        self._option.get('legend').get('data').append(name)
        self._option.get('series').append({
            "type": "gauge",
            "detail": {"formatter": '{value}%'},
            "name": name,
            "min": _min,
            "max": _max,
            "startAngle": _start,
            "endAngle": _end,
            "data": [{"value": value, "name": attr}]
        })
        self._legend_visualmap_colorlst(**kwargs)
