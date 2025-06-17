---
type: Tool
collections: Liunx
title: InterNet
tags: []
---

### ifconfig和ping的基础配置。

Liunx的IP地址就是IPv4地址。

- apt install net-tools

- apt install iputils-ping

- ifconfig

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8ba6b9e3-0802-4d1a-87f0-0966b264de0e/Untitled.png)

[Untitled](Images/Untitled.md)

第一块网卡的名字叫eth0，第二块网卡的名字叫lo。

inet addr就是分别就是两块网卡的IP地址。

127.0.0.1被称为本地回环地址，一般用来测试本机网卡是否正常，time越大网速越慢。

- ping IP地址/域名 （*检测到目标主机是否连接正常）*

- ping 127.0.0.1 （*检测本地网卡工作正常）*

### SSH基础

在 Linux 中 SSH 是 **非常常用** 的工具，通过 **SSH 客户端** 我们可以连接到运行了 **SSH 服务器** 的远程机器上。这里的SSH客户端和SSH服务器都只是软件。

**IP 地址**：通过 **IP 地址** 找到网络上的 **计算机。**

**端口号**：通过 **端口号** 可以找到 **计算机上运行的服务器软件**，一般是IP地址后面加冒号**。**

**域名：**其实就是IP地址的另一个名字，就是网址。

常见服务端口号列表：

| **序号** | **服务**  | **端口号** |
| :----- | :------ | :------ |
| 01     | SSH 服务器 | 22      |
| 02     | Web 服务器 | 80      |
| 03     | HTTPS   | 443     |
| 04     | FTP 服务器 | 21      |

红色部分就是主机号，p后面的6157部分是端口号，作为docker镜像的使用者，我们一般不关注内部端口，只需要外部端口，所以p后面的也是外部端口号。

- ssh root@10.131.145.4 (mailto:root@10.131.145.4) -p6157

ssh -p 24310 [root@region-9.autodl.pro](mailto:root@region-9.autodl.pro)

**mac文件传输用scp**

将mac本机文件（文件夹）复制到远程服务器

- scp -P7006 (-r) /Users/titus.w/Desktop/setup.py root@10.131.145.3 (mailto:root@10.131.145.3):/root/data/test/hah.txt

将远程服务器的文件（文件夹）复制到mac本机

- scp -P7006 (-r) root@10.131.145.3 (mailto:root@10.131.145.3):/root/data/fairseq/setup.py /Users/titus.w/Desktop/setup.py

**windows文件传输用ftp**

```python
ftp
10.84.73.77
bj_research
bj_research_11123411
dir或者ls
cd wangjiatai
dir或者ls
get
put 的时候本地路径，远程路径
put命令必须要传远程路径创建文件，不能省
bye
#只能上传下载文件，不能是文件夹
#文件夹的话必须得压缩一下，所以这一点不如scp
前面加感叹号就是本机操作
！pwd
！dir
切换目录是cd
本机切换目录是lcd
甚至还能！mkdir
或者有批量下载mget *
但是会漏掉一些文件夹和文件
注意get命令的两个路径名必须是文件名
要么get 路径文件名 啥也没有
要么get 路径文件名 路径文件名
```

[http://localhost:8889/?token=d24b53184586615b4afca6f864530356b354c02fc0f528c6](http://localhost:8889/?token=d24b53184586615b4afca6f864530356b354c02fc0f528c6)

### 网络请求

**curl / wget**

云服务器查看公网IP命令

```text
curl ipinfo.io
curl ifconfig.me
```

curl命令远端文件网站，只能显示，但是不能下载，想要下载需要加上一个参数：

- curl -O 网址

- curl -O 特定路径 网址

如果链接中包含问号，需要为整个链接加上双引号(--no-check-certificate可以无视证书)：

```python
wget --no-check-certificate -O AdGen.tar.gz  "<https://cloud.tsinghua.edu.cn/f/b3f119a008264b1cabd1/?dl=1>"
```

### 代理配置

[不同公司都不太相同](https://www.notion.so/15280fb17b698179aeaddab91e23f18d?pvs=21)

# 不同公司都不太相同

如果没有网的话就改代理配置 vim ~/.bashrc 在 ~/.bashrc （没有则新建）中写入以下配置

```jsx
export http_proxy=http://wgw.myoas.com:9090
export https_proxy=http://wgw.myoas.com:9090
export no_proxy=localhost,127.0.0.1,10.0.0.0/8,192.168.0.0/16,172.16.0.0/12,.myoas.local,.myoas.com,.adc.com,.oppo.com,.oasqa.com,oppoit.com,.oppo.local
```

配置完成后执行source ~/.bashrc 注意：no_proxy 对 curl 不生效，需要用curl的命令参数指定，例如 curl --noproxy *.myoas.com [upm.myoas.com](http://upm.myoas.com/)

curl --noproxy 127.0.0.1 [http://127.0.0.1:8888/](http://127.0.0.1:8888/)[http://127.0.0.1:8888](http://127.0.0.1:8888)

新的服务器装conda环境,我只能说太简单了。 y有一些和网络相关的东西

~/.bashrc

~/.condarc

pip的源

~/.pip/pip.conf时候会有不存在的情况，此时我们必须得先新建文件夹。

mkdir ~/.pip

vi是有新建文件和查看的作用，而vim最好只用于编辑。vi ~/.pip/pip.conf

### 网络带宽监控工具

- apt-get install bwm-n

- bwm-ng

### 跳板机设置

有一种方法是设置SSH跳板机，在~/.ssh/config中添加以下内容：

```python
Host my-bastion
  HostName 10.131.145.3
  Port 7009
  User your_username_on_bastion
Host my-target
  HostName 10.131.145.30
  Port 7009
  User your_username_on_target
  ProxyJump my-bastion
```

通过这样配置，当执行**`ssh my-target`**时，SSH客户端会自动先连接到跳板机（10.131.145.3），然后再从跳板机连接到目标服务器（10.131.145.30）。

但是我更加建议下面这种方法

### 隧道转发

SSH隧道允许你通过一个中转服务器（10.131.145.3）来访问最终目标服务器（10.131.145.30）。这里是一个示例命令，展示如何创建一个SSH隧道：

- ssh -L 7009:10.131.145.30:6157 root@10.131.145. (mailto:user@10.131.145.3)4

这条命令会创建一个监听本地端口6157的隧道，将所有通过该端口的流量转发到10.131.145.30的7009端口，通过10.131.145.4作为中转。一旦隧道建立，就可以直接通过本地的6157端口连接到10.131.145.30。

隧道建立后，就可以像连接到本地服务器一样连接到10.131.145.30。例如，想通过SSH连接可以使用：

- ssh user@localhost:6157

在这里，`user`**是你在10.131.145.30上的用户名。注意，由于隧道的存在，尽管你连接的是**`localhost`，实际上你是在连接10.131.145.30。

### **在VSCode中使用SSH隧道**

1. 在终端j建立SSH隧道

2. 在VSCode中，打开命令面板（`Ctrl+Shift+P`**或**`Cmd+Shift+P`），然后搜索并选择“Remote-SSH: Open Configuration File”。选择你的SSH配置文件（通常是**`~/.ssh/config`**）

3. 在配置文件中，添加以下配置

```python
Host my-remote-server
  HostName localhost
  Port 6157
  User your_username_on_10.131.145.30
```

4.现在，当你通过VSCode连接到**`my-remote-server`**时，它实际上会通过本地的7009端口连接到10.131.145.30，密码也是输入10.131.145.30的密码。

5.如果想要隧道一直生效的话可以用tmux或者nohup。

