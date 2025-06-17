---
type: Tool
collections: Liunx
title: Introduction
tags: []
---

操作系统本质上就是操控硬件，并将这种操作封装成系统调用。而Linux内核就是用bash当作开发环境，gcc当作编译工具。基于内核，众多发行版如Ubuntu，Redhat，Debian，CentOS等。

[https://linux265.com](https://linux265.com)

**Linux 简介**

Linux 是一种 **开源**、**类 Unix** 的操作系统，它由 **Linus Torvalds** 于 1991 年发布，并在全球范围内广泛应用。Linux 以其 **稳定性**、**安全性** 和 **灵活性** 而受到服务器、嵌入式系统、超级计算机等领域的青睐。

**1. Linux 主要特点**

• **开源免费**：基于 GPL（GNU General Public License），任何人都可以自由使用、修改和分发。

• **稳定可靠**：适用于长时间运行的服务器，几乎不会像 Windows 那样频繁崩溃。

• **多用户多任务**：支持多个用户同时登录，允许同时运行多个进程。

• **高安全性**：权限管理、用户隔离机制、SELinux 等安全机制，使其更难受到病毒攻击。

• **兼容 POSIX 标准**：提供类似 Unix 的命令行和 API 结构，适用于开发人员和服务器管理。

**2. Linux 主要发行版（Distributions）**

Linux 并不是单一的操作系统，而是多个不同发行版（简称“发行版”或“Distro”）的集合，常见的 Linux 发行版包括：

**（1）服务器级**

**发行版** **特点**

**Ubuntu Server** 适合新手，社区支持活跃

**Debian** 稳定性高，适合企业级应用

**CentOS / Rocky Linux** RHEL（Red Hat Enterprise Linux）的免费版，广泛用于企业

**Red Hat Enterprise Linux（RHEL）** 付费支持，企业级应用的标准

**SUSE Linux Enterprise Server（SLES）** 适用于大型企业，尤其在 SAP 领域

**AlmaLinux** CentOS 的替代品，面向企业

**（2）桌面级**

**发行版** **特点**

**Ubuntu** 适合个人用户和开发者，界面友好

**Linux Mint** 类似 Windows UI，适合从 Windows 转换的用户

**Fedora** 新技术实验平台，RHEL 的社区版

**Manjaro** 基于 Arch Linux，适合喜欢滚动更新的用户

**Zorin OS** 界面接近 Windows，适合初学者

**3. Linux 目录结构**

Linux 遵循 **FHS（Filesystem Hierarchy Standard）**，主要目录包括：

**目录** **作用**

/ 根目录，所有文件和目录的起点

/bin 存放基本的可执行命令（如 ls, cp, rm）

/sbin 仅限管理员使用的系统命令

/etc 配置文件目录

/home 普通用户的家目录

/root root 用户的主目录

/usr 用户应用程序和库文件

/var 存放日志和动态数据

/tmp 临时文件目录

/dev 设备文件，如磁盘、USB、键盘

/proc 虚拟文件系统，存放系统进程信息

/mnt 挂载点目录（如 U 盘）

**4. Linux 常用命令**

**（1）文件和目录操作**

**命令** **作用**

ls 列出当前目录下的文件

cd 切换目录

pwd 显示当前路径

mkdir 创建目录

rm 删除文件/目录

cp 复制文件/目录

mv 移动或重命名文件

find 查找文件

touch 创建空文件

**（2）用户和权限管理**

**命令** **作用**

whoami 显示当前用户

who 显示在线用户

passwd 修改密码

chown 更改文件所有者

chmod 修改权限

groups 显示当前用户所属的组

**（3）进程管理**

**命令** **作用**

ps 查看运行中的进程

top 动态监视进程

kill 终止进程

pkill 按进程名终止

htop 交互式进程管理（需安装）

**（4）网络相关**

**命令** **作用**

ping 测试网络连通性

curl 获取网页内容

wget 下载文件

ifconfig / ip a 查看 IP 地址

netstat 显示网络连接信息

**5. Linux 软件管理**

不同 Linux 发行版使用不同的软件包管理工具：

**（1）Debian/Ubuntu 系**

使用 apt（Advanced Package Tool）：

sudo apt update      # 更新软件源

sudo apt upgrade     # 升级系统

sudo apt install vim # 安装 Vim 编辑器

sudo apt remove vim  # 卸载 Vim

**（2）RHEL/CentOS 系**

使用 yum 或 dnf：

sudo yum update      # 更新系统（旧版）

sudo dnf update      # 更新系统（新版）

sudo yum install vim # 安装 Vim

sudo yum remove vim  # 卸载 Vim

**（3）Arch Linux 系**

使用 pacman：

sudo pacman -Syu       # 更新系统

sudo pacman -S firefox # 安装 Firefox

sudo pacman -R firefox # 卸载 Firefox

**6. Linux Shell 和 Bash**

Linux 主要通过 **Shell**（命令行解释器）与用户交互，常见 Shell 有：

• **Bash（默认 Shell）**

• **Zsh（更强的自动补全）**

• **Fish（用户友好的交互体验）**

• **Sh（POSIX 兼容，最基础的 Shell）**

**查看当前 Shell：**

echo $SHELL

**更改默认 Shell：**

chsh -s /bin/bash  # 切换到 Bash

chsh -s /bin/zsh   # 切换到 Zsh

**7. Linux 适用场景**

Linux 在多个领域广泛应用：

• **服务器**（网站托管、数据库服务器、云计算）

• **嵌入式设备**（智能手机 Android、路由器、IoT）

• **开发环境**（程序员和 DevOps 首选）

• **人工智能与大数据**（TensorFlow、Hadoop 运行环境）

• **安全与黑客工具**（Kali Linux）

**8. Linux 资源学习**

如果你是初学者，可以从以下资源学习：

• [The Linux Command Line](https://linuxcommand.org/) - 命令行指南

• [Linux Journey](https://linuxjourney.com/) - 交互式学习网站

• [Arch Wiki](https://wiki.archlinux.org/) - 深入技术文档（适用于所有 Linux 发行版）

**总结**

• **Linux 是一个开源、稳定、安全的操作系统**，广泛用于服务器、云计算、嵌入式系统等。

• **不同发行版适用于不同需求**（如 Ubuntu 适合桌面用户，CentOS 适合企业服务器）。

• **掌握 Linux 基础命令**（文件操作、用户管理、进程管理等）对系统管理和开发至关重要。

如果你是新手，可以从 Ubuntu 或 CentOS 开始，结合实际操作学习！

