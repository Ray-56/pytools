#!/usr/bin/env python3
# encoding: utf-8

from re import template
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from jinja2.environment import Template
import imgkit

# 从指定位置加载模板的环境
# loader = PackageLoader('commons', 'templates')
loader = FileSystemLoader("templates")
env = Environment(loader=loader, autoescape=select_autoescape(["html", "xml"]))


# 获取模板
template = env.get_template("index.html")

title = "表格标题"
# 一行显示列的个数
col_count = 2
columns = [
    # {"title": "date", "data_index": "date"},
    # {"title": "weekday", "data_index": "weekday"},
    {"title": "激活量", "data_index": "active_number"},
    {"title": "cpa(现金）", "data_index": "cpa"},
    {"title": "现金支出", "data_index": "output"},
    {"title": "累时次留", "data_index": "sum"},
    {"title": "激励视频PV", "data_index": "pv"},
    {"title": "首日ROI", "data_index": "roi"},
    {"title": "次留成本", "data_index": "keep"},
    # {"title": "次留成本11", "data_index": "keep11"},
]
data_source = [
    {
        "date": "20200610",
        "weekday": "周一",
        "active_number": "10000000",
        "active_number_ratio": "10%",
        "active_number_percent": "90%",
        "cpa": "¥4",
        "cpa_ratio": "30%",
        "cpa_percent": "66%",
        "output": "¥240,000.00",
        "output_ratio": "-22.22%",
        "output_percent": "10%",
        "sum": "-28.11%",
        "sum_ratio": "-01.11%",
        "sum_percent": "55%",
    },
    {
        "date": "20200611",
        "weekday": "周二",
        "active_number": "80",
        "active_number_ratio": "-10%",
        "cpa": "¥8",
        "cpa_ratio": "-60.99%",
        "output": "¥60,000,000.00",
        "output_ratio": "-100.00%",
        "sum": None,
        "sum_ratio": "-01.11%",
    },
    {
        "date": "20200611",
        "weekday": "周二",
        "active_number": "80",
        "active_number_ratio": "-10%",
        "cpa": "¥8",
        "cpa_ratio": "-60.99%",
        "output": "¥60,000,000.00",
        "output_ratio": "61.11%",
        # "sum": "-28.11%",
        "sum_ratio": "-01.11%",
    },
    {
        "date": "20200611",
        "weekday": "周二",
        "active_number": "80",
        "active_number_ratio": "-10%",
        "cpa": "¥8",
        "cpa_ratio": "-60.99%",
        "output": "¥60,000,000.00",
        "output_ratio": "61.11%",
        # "sum": "-28.11%",
        "sum_ratio": "-01.11%",
    },
    {
        "date": "20200611",
        "weekday": "周二",
        "active_number": "80",
        "active_number_ratio": "-10%",
        "cpa": "¥8",
        "cpa_ratio": "-60.99%",
        "output": "¥60,000,000.00",
        "output_ratio": "61.11%",
        # "sum": "-28.11%",
        "sum_ratio": "-01.11%",
    },
    {
        "date": "20200611",
        "weekday": "周二",
        "active_number": "80",
        "active_number_ratio": "-10%",
        "cpa": "¥8",
        "cpa_ratio": "-60.99%",
        "output": "¥60,000,000.00",
        "output_ratio": "61.11%",
        # "sum": "-28.11%",
        "sum_ratio": "-01.11%",
    },
    {
        "date": "20200611",
        "weekday": "周二",
        "active_number": "80",
        "active_number_ratio": "-10%",
        "cpa": "¥8",
        "cpa_ratio": "-60.99%",
        "output": "¥60,000,000.00",
        "output_ratio": "61.11%",
        # "sum": "-28.11%",
        "sum_ratio": "-01.11%",
    },
]

# 渲染模板
result = template.render(
    title=title, col_count=col_count, columns=columns, data_source=data_source
)

# 流创建文件
# Template('{{ result }}').stream(result=result).dump('dist/new_file_by_stream.html')

with open("dist/new_file.html", "w") as fh:
    fh.write(result)

options = {
    "enable-local-file-access": None,
    "width": 620, # 三列使用 860, 两列使用 620
    # "height": 600,
    # "crop-h": "3000",
    # "crop-w": "600",
    # "crop-x": "300",
    # "crop-y": "300",
    # "encoding": "UTF-8",
    "quality": 50,  # 质量，int 区间 [0,100]
}
# css = ["dist/bootstrap.min.css"]
css = ["static/bootstrap.min.css", "static/styles.css"]
# with open("dist/new_file.html") as f:
imgkit.from_string(result, "dist/out.jpg", options, css=css)
