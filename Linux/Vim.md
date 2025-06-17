---
type: Tool
collections: Liunx
title: Vim
tags: []
---

创建.vimrc文件

```python
vim ~/.vimrc
#添加下面几行
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8
#wq退出即可
```

```python
#往vim里粘贴时，自动缩进会导致错误排版。所以先打开粘贴模式，粘贴完再关闭：
set paste
set nopaste
#显示行号  命令模式下输入
set nu
#搜索关键字,注意千万不是命令模式，按n或者大写n切换
/XXX加回车
#如果需要设置常亮,则必须在命令模式执行一下命令：
set hlsearch
noh
#vi 文件名 直接看文件，ZZ退出
#长按d全部删除
#新建文件或者touch：
vim XXX.txt
```

