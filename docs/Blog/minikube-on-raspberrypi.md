打算用树莓派部署个minikube来学习k8s

- Minikube的硬件要求
```
https://minikube.sigs.k8s.io/docs/start/

What you’ll need
2 CPUs or more
2GB of free memory
20GB of free disk space
Internet connection
Container or virtual machine manager, such as: Docker, QEMU, Hyperkit, Hyper-V, KVM, Parallels, Podman, VirtualBox, or VMware Fusion/Workstation
```

我的树莓派:
4代B型, 内存4G, 操作系统为Ubuntu 18.04.5 LTS
```shell
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.5 LTS
Release:        18.04
Codename:       bionic
```
CPU核心数：4核
```
$ cat /proc/cpuinfo | grep "processor" | wc -l
4

$ lscpu
架构：           aarch64
字节序：         Little Endian
CPU:             4
在线 CPU 列表：  0-3
每个核的线程数： 1
每个座的核数：   4
座：             1
厂商 ID：        ARM
型号：           3
型号名称：       Cortex-A72
步进：           r0p3
CPU 最大 MHz：   1500.0000
CPU 最小 MHz：   600.0000
BogoMIPS：       108.00
L1d 缓存：       32K
L1i 缓存：       48K
L2 缓存：        1024K
标记：           fp asimd evtstrm crc32 cpuid
```

- 提前安装好docker
捣鼓了一阵，安装过程总报错，还是安装docker-ce吧
```
直接 apt-get install docker-ce 会报错：
下列软件包有未满足的依赖关系：
 docker-ce : 依赖: containerd.io (>= 1.6.4) 但是它将不会被安装
             推荐: pigz 但无法安装它
E: 无法修正错误，因为您要求某些软件包保持现状，就是它们破坏了软件包间的依赖关系。

------------
1. 先 apt-cache madison docker-ce 看下哪些版本能安装
2. sudo apt install docker-ce=18.03.1~ce~3-0~ubuntu
3. docker -v
不行，docker-ce版本过低，minikube --driver=docker的时候报错
------------
源码安装docker-ce

~$ sudo apt install ./docker-ce_20.10.0~3-0~debian-buster_arm64.deb
正在读取软件包列表... 完成
正在分析软件包的依赖关系树
正在读取状态信息... 完成
注意，选中 'docker-ce' 而非 './docker-ce_20.10.0~3-0~debian-buster_arm64.deb'
有一些软件包无法被安装。如果您用的是 unstable 发行版，这也许是
因为系统无法达到您要求的状态造成的。该版本中可能会有一些您需要的软件
包尚未被创建或是它们已被从新到(Incoming)目录移出。
下列信息可能会对解决问题有所帮助：

下列软件包有未满足的依赖关系：
 docker-ce : 依赖: containerd.io (>= 1.4.1) 但是它将不会被安装
             推荐: pigz 但无法安装它
E: 无法修正错误，因为您要求某些软件包保持现状，就是它们破坏了软件包间的依赖关系。

----------
1. 安装高版本 containerd.io 
https://download.docker.com/linux/debian/dists/buster/pool/stable/arm64/ 挑选一个
curl -O https://download.docker.com/linux/debian/dists/buster/pool/stable/arm64/containerd.io_1.6.9-1_arm64.deb
sudo apt install ./containerd.io_1.6.9-1_arm64.deb

2. 
curl -O https://download.docker.com/linux/debian/dists/buster/pool/stable/arm64/docker-ce_20.10.0~3-0~debian-buster_arm64.deb
sudo apt install ./docker-ce_20.10.0~3-0~debian-buster_arm64.deb
```

安装minikube, 根据官网的提示得到以下命令
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-arm64
sudo install minikube-linux-arm64 /usr/local/bin/minikube
```
```
$ minikube start --driver=docker

 因 RSRC_DOCKER_STORAGE 错误而退出：Docker 的磁盘空间已满！（/var 目录已使用 99% 的容量）。您可以传递 '--force' 参数跳过此检查。
--------------
迁移docker https://blog.csdn.net/zzhuan_1/article/details/102953841 , (我尝试迁移到U盘，但是失败了，问题多)
--------------
重新安装docker到指定的目录：

```




#### 插曲
- 树莓派sd卡空间不足，需将docker数据转移到新的U盘上，操作步骤如下 (Docker能安装再U盘上吗？)



ubuntu完全卸载docker, uninstall docker
    - https://blog.csdn.net/weixin_45881248/article/details/134363865


```
~$ /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
WARN[2024-03-01T11:50:00.909235805+08:00] The "graph" config file option is deprecated. Please use "data-root" instead.
INFO[2024-03-01T11:50:00.909614622+08:00] Starting up
dockerd needs to be started with root. To see how to run dockerd in rootless mode with unprivileged user, see the documentation

--------------
使用Docker Rootless模式，运行Docker服务


```