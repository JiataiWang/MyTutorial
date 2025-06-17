---
type: Tool
collections: Liunx
title: System Architecture
tags: []
---

### 磁盘信息

查看剩余磁盘空间，重点放在挂载点在根目爱他

| **序号** | **命令**      | **作用**                  |
| :----- | :---------- | :---------------------- |
| 01     | df -h       | `disk free` 显示磁盘剩余空间    |
| 02     | du -h [目录名] | `disk usage` 显示目录下的文件大小 |
| 03     | tree —du -h | 显示当前目录下文件大小             |

### 进程

**ps查看进程**

- ps au/ps -ef

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ee37e53-4084-4a1d-b5e2-a9c5da484c4b/Untitled.png)

[Untitled](Images/Untitled%20(2).md)

USER是由哪个用户在终端执行的进程。

PID进程ID。

COMMAND也就是CMD，执行了什么命令。

**top查看进程**

top会按照利用率排序，而且会一直动态监控，按q退出。

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/35759f03-cd5b-4b7a-a92a-17dd5072a139/Untitled.png)

[Untitled](Images/Untitled%20(3).md)

**杀死进程kil** kill -9 PID

### 其他命令

软链接文件名是带有箭头的，硬链接是不带箭头的，源文件被删除，软链接会失效，硬链接不会。

建立软链接

- ln -s 文件的绝对路径 softlink1

建立硬链接

- ln 文件的绝对路径 hardlink1

### 压缩与解压

在 `Linux` 中，最常见的压缩文件格式就是 `xxx.tar.gz`

压缩文件

- tar -zcvf 压缩包.tar.gz 被压缩的文件(夹)

zip -r myfolder.zip myfolder

解压文件

- tar -zxvf 压缩包.tar.gz

- tar -zxvf 压缩包.tar.gz -C 目标路径

在 `Linux` 中，其他常见的压缩文件格式就是 `xxx.tar.bzip2`

压缩文件

- tar -jcvf 压缩包.tar.bz2 被压缩的文件(夹)

解压文件

- tar -jxvf 压缩包.tar.bz2

- tar -jxvf 压缩包.tar.bz2 -C 目标路径

其他解压路径下所有压缩包：

- unzip *.zip

- gunzip *.gz

- zstd -d *.zst

### 软件安装

**apt（ubuntu）**

更新软件包

- sudo apt-get update

- sudo apt-get upgrade

安装软件

- sudo apt install 软件包

卸载软件

- sudo apt remove 软件名

还有其他工具如：**yum（centos），pip，conda，brew，git等等。**

