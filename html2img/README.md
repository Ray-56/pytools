# HTML_TO_IMG

<details>
<summary>目录</summary>

[TOC]

</details>

## jinja2

> Python 模板引擎 `jinja2`

[jinja2-template-examples repo](https://github.com/hooj0/jinja2-template-examples)

## imgkit

<a href="https://github.com/jarrekk/imgkit" target="_blank">imgkit repo</a>

[Installation](https://github.com/jarrekk/imgkit#installation)

## 问题&解决

生成图片时外部 CSS 文件引入无效。改为 HTML 文件内定义

## 数据类型

```ts
interface Props {
  /** 表格标题 */
  title: string;
  /** 一行显示列的个数(不包含 data、weekday) */
  col_count: number;
  /** 列描述数据对象 */
  columns: {
    /** 列头显示文字 */
    title: string;
    /** 列数据在数据项中对应的`key` */
    data_index: string;
  }[];
  /**
   * 数据数组  
   * 包含带有`_ratio`后缀字段
   */
  data_source: {
    [key: string]: string;
  }[];
}
```