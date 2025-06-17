---
type: Tool
collections: Liunx
title: Text
tags: []
---

在xxx.txt文件中搜索关键字abc

- grep -n abc xxx.txt

- grep -n ^abc xxx.txt（正则：在xxx.txt文件中搜索字符串abc开头的行）

- grep -n abc$ xxx.txt（正则：在xxx.txt文件中搜索字符串abc结尾的行）

将终端输出的结果添加到某个文件末尾（>覆盖，>>重定向到末尾）

- echo hello word >> a.txt

- tree >> a.txt

- ll >> a.txt

查看行数，字符数，字节数

- wc xxx.txt

显示文件前n行

- head -n 行数 文件

显示文件倒数前n行

- tail -n 行数 文件

输出文件第五行内容（成文件）

- cat nowcoder.txt | tail -n +5 | head -n 1

- cat nowcoder.txt | tail -n +5 | head -n 1 > 5th.txt

将一个文件顺序打乱输出到另一个文件

- shuf a.txt > b.txt

- shuf a.txt -o b.txt

将一个文件中的数据随机获取30条数据存到另一个文件中

- shuf a.txt -o b.txt -n 30

对比两个文本文件的不同，对于对比得出的结果而言，左右两侧代表行号，小于号<是旧规则的结果，>大于号是新规则的结果

- diff th_old.txt th_new.txt > th_diff.txt

