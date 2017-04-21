#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: captcha.py
@time: 16-4-11 下午9:23
"""


import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from config import BASE_DIR


class Captcha(object):
    """
    验证码（生成）
    """
    # map:将str函数作用于后面序列的每一个元素
    _letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母, 去除可能干扰的i, l, o, z
    _upper_cases = _letter_cases.upper()  # 大写字母
    _numbers = ''.join(map(str, range(3, 10)))  # 数字, 去除可能干扰的0, 1, 2
    init_chars = ''.join((_upper_cases, _numbers))

    def __init__(self,
                 size=(120, 30),
                 chars=init_chars,
                 mode="RGB",
                 bg_color=(255, 255, 255),
                 fg_color=(255, 0, 0),
                 line_color=(255, 0, 0),
                 point_color=(255, 0, 0),
                 font_type='%s/%s' % (BASE_DIR, 'app_backend/static/fonts/Ubuntu-B.ttf'),
                 font_size=18,
                 length=4,
                 draw_lines=True,
                 n_lines=(1, 2),
                 draw_points=True,
                 point_chance=2):
        """
        :param size: 图片的大小，格式（宽，高），默认为(120, 30)
        :param chars: 允许的字符集合，格式字符串
        :param mode: 图片模式，默认为RGB
        :param bg_color: 背景颜色，默认为白色
        :param fg_color: 前景色，验证码字符颜色
        :param font_type: 验证码字体
        :param font_size: 验证码字体大小
        :param length: 验证码字符个数
        :param draw_lines: 是否划干扰线
        :param n_lines: 干扰线的条数范围，格式元组，默认为(1, 2)，只有draw_lines为True时有效
        :param draw_points: 是否画干扰点
        :param point_chance: 干扰点出现的概率，大小范围[0, 50]
        :return:
        """
        self.size = size
        self.width, self.height = size
        self.chars = chars
        self.bg_color, self.fg_color, self.line_color, self.point_color = bg_color, fg_color, line_color, point_color
        self.font_type, self.font_size = font_type, font_size
        self.length = length
        self.draw_lines, self.n_lines, self.draw_points = draw_lines, n_lines, draw_points
        self.point_chance = point_chance
        self.img = Image.new(mode, size, bg_color)  # 创建图形
        self.draw = ImageDraw.Draw(self.img)  # 创建画笔

    def _get_chars(self):
        """
        生成给定长度的字符串，返回列表格式
        """
        return random.sample(self.chars, self.length)

    def _create_lines(self):
        """
        绘制干扰线
        """
        line_num = random.randint(*self.n_lines)  # 干扰线条数

        for i in range(line_num):
            # 起始点
            begin = (random.randint(0, self.size[0]), random.randint(0, self.size[1]))
            # 结束点
            end = (random.randint(0, self.size[0]), random.randint(0, self.size[1]))
            self.draw.line([begin, end], fill=self.line_color)

    def _create_points(self):
        """
        绘制干扰点
        """
        chance = min(50, max(0, int(self.point_chance)))  # 大小限制在[0, 50]

        for w in xrange(self.width):
            for h in xrange(self.height):
                tmp = random.randint(0, 50)
                if tmp > 50 - chance:
                    self.draw.point((w, h), fill=self.point_color)

    def _create_code_str(self):
        """
        绘制验证码字符
        """
        c_chars = self._get_chars()
        c_str = '%s' % ''.join(c_chars)

        font = ImageFont.truetype(self.font_type, self.font_size)
        font_width, font_height = font.getsize(c_str)

        self.draw.text(((self.width - font_width) / 3, (self.height - font_height) / 4),
                       c_str, font=font, fill=self.fg_color)
        return c_str

    def get(self):
        if self.draw_lines:
            self._create_lines()
        if self.draw_points:
            self._create_points()
        code_str = self._create_code_str()

        # 图形扭曲参数
        params = [1 - float(random.randint(1, 2)) / 100,
                  0,
                  0,
                  0,
                  1 - float(random.randint(1, 10)) / 100,
                  float(random.randint(1, 2)) / 500,
                  0.001,
                  float(random.randint(1, 2)) / 500
                  ]
        img = self.img.transform(self.size, Image.PERSPECTIVE, params)  # 创建扭曲

        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强（阈值更大）

        return img, code_str


if __name__ == '__main__':
    pass
