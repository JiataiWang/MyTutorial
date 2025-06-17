---
type: Tool
collections: Liunx
title: Permission
tags: []
---

linux是一种多用户的操作系统。而且只有系统管理员来做添加用户和删除用户，所以在开发团队中，如果是IT岗位或者系统管理员会常用这部分命令。

登录上服务器(云或者离线机)，先登录自己的用户，是非常不推荐用root账户登录的，不允许随便修改系统设置：

```python
su wangjiatai
wangjiataiS9052621
```

### ll命令详解

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d4a47b73-ace8-40fe-b60b-d2b7bfbef8e5/Untitled.png)

[Untitled](Images/Untitled%20(1).md)

**权限**，第 1 个字符如果是 `d` 表示目录。

**硬链接数**，通俗地讲，就是有多少种方式，可以访问到当前目录／文件。文件的硬链接一般只有一种，文件夹的硬链接数等于2(绝对路径和相对位置)+子目录数。

**拥有者（u）**，家目录下 文件／目录 的拥有者通常都是当前用户。

**组（g）**，在 Linux 中，很多时候，会出现组名和用户名相同的情况。

**其他用户（o）**。

### chmod命令

修改文件权限： chmod u/g/o/a =  [rwx](https://so.csdn.net/so/search?q=rwx&spm=1001.2101.3001.7020) 文件名 chmod u = r-x 文件名 权限分为三个组，每组三个字母共9个字母：u文件所有者4，g用户组2，o其他用户1 反正就记住ugoa这四个字母就行 普通文件变可执行文件需要修改权限成 rwxr-xr-x

如果是文件夹的话chmod -R 777 文件夹名 ，这里注意这个R必须大写，一般使shell脚本拥有可执行权限，.sh是linux中的可执行文件。

### 组管理

**创建组** / **删除组** 的终端命令都需要通过 `sudo` 执行，或者直接登录root账户。

| **命令**             | **作用**      |
| :----------------- | :---------- |
| groupadd 组名        | 添加组         |
| groupdel 组名        | 删除组         |
| cat /etc/group     | 查看组信息       |
| chgrp -R 组名 文件/目录名 | 修改文件/目录的所属组 |

### 用户管理

**创建用户** / **删除用户** / **修改其他用户密码** 的终端命令都需要通过 `sudo` 执行

| **命令**                   | **作用**   | **说明**                         |
| :----------------------- | :------- | :----------------------------- |
| useradd -m -g 组名 新建用户名   | 添加新用户    | -m 自动建立用户家目录                   |
| -g 指定用户所在的组，否则会建立一个和同名的组 |          |                                |
| passwd 用户名               | 设置用户密码   | 如果是普通用户，直接用 passwd 可以修改自己的账户密码 |
| userdel -r 用户名           | 删除用户     | r 选项会自动删除用户家目录                 |
| cat /etc/passwd          | grep 用户名 | 查看用户信息                         |

上表橙色部分是添加一个用户必须要执行的两个命令。

**查看用户信息**

| **序号** | **命令** | **作用**            |
| :----- | :----- | :---------------- |
| 01     | id 用户名 | 查看用户 UID 和 GID 信息 |
| 02     | who    | 查看当前所有登录的用户列表     |
| 03     | whoami | 查看当前登录用户的账户名      |

**设置主组和附加组**

在添加了用户之后，默认该用户是不可以用sudo来执行命令的，如果想让新加的用户用sudo执行命令，就必须要要把这个用户添加到sudo这个附加组中。

修改用户的主组（passwd 中的 GID）

- usermod -g 组 用户名

修改用户的附加组(group 中的 用户的附加权限)

- usermod -G 组 用户名（sudo usermod -G sudo wangjiatai）

修改(新建)用户登录显示 Shell

- usermod -s /bin/bash 用户名

**which命令**

`/etc/passwd` 是用于保存用户信息的文件

`/usr/bin/passwd` 是用于修改用户密码的程序

which命令可以查看执行命令所在位置，例如

- which ls

- which useradd

我们发现很多命令都在bin 和 sbin中，那这两个文件夹有什么区别吗？

在 Linux 中，绝大多数可执行文件都是保存在 /bin、/sbin、/usr/bin、/usr/sbin /bin（binary）是二进制执行文件目录，主要用于具体应用 /sbin（system binary）是系统管理员专用的二进制代码存放目录，主要用于系统管理 /usr/bin（user commands for applications）后期安装的一些软件 /usr/sbin（super user commands for applications）超级用户的一些管理程序

`cd` 这个终端命令是内置在系统内核中的，没有独立的文件，因此用 `which` 无法找到 `cd` 命令的位置

