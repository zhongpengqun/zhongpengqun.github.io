---
layout: default
title: Hello
description: Introduction about this site and me.
---

### CNCF

## Docker
- Docker
    - Use case of docker tags
    - Is it possible that 2 same pods run on one k8s node ?
    - What is overlay ?
    - Network
      - Bridge
      - Host
      - ...
    - docker manifest
    - docker sbom command
    - Configmap
    - 进入pod与进入container的区别？
    - How to get docker disk usage ?  `docker system df`
    - docker export & docker save ?
    - docker import & docker load ?
- Docker-compose
- kubectl
  - kubectl create & kubectl apply
  - Services
    - ClusterIp (Default)
    - NodePort
    - 

- Dockerfile
  - VOLUME
    - When do we need VOLUME 
    - 3 docker volume types
  - COPY --from=builder /opt/static static

- Docker stop all containers
    - stop all containers: `docker stop $(docker ps -aq)`
    - remove all containers: `docker rm $(docker ps -aq)`
    - delete all images `docker rmi $(docker images -q)`
- Why during my usage of docker, the docker disk usage is bigger and bigger ?
- docker network
- docker-compose `ports`, left or right is container port ?
- Host-port:Container-port

- Which command both in docker and docker-compose, is there any difference in usage in docker and docker-compose ?
- docker save & docker export

# docker-compose
- Why `links` ? Is it has any association with `depends_on` ?

`depends_on` determines the order of create containers.

An example
```yaml
version: '3.6'     # version of format of this yaml file, it can be 1, 2.x, 3.x, it's matter of the compatible with docker
services:
    nginx:
        build:
            context: fish        
            dockerfile: Dockerfile.nginx    # dockerfile is located at fish/Dockerfile.nginx
        restart: always     # it's equal to `docker run --restart always`, it is one kind of `restart policies`, 
                            # docker daemon will always try to restart the container infinitely until container starts successfully.
        links:          
            - gunicorn    # By links, gunicorn:80 will works, same as 10.0.0.4:80
        volumes:
            - nfs-storage:/build/toolchain    # `nfs-storage` is defined in below high level `volumes` block.
            - "./runtime/fish_nginx.conf:/etc/nginx/sites-available/fish.conf:ro"     # mount local file into container
        ports:
            - "80:80"   # host-port: container-port

    gunicorn:
        image: "fish_django_backend"    # my guess: 
        build:
            context: fish
            dockerfile: Dockerfile.django
        command: ["./bin/gunicorn_entrypoint.sh"]
        restart: always
        links:
            - db
            - couchdb
            - rabbitmq
        volumes:
            - nfs-storage:/build/toolchain
        expose:
            - "8000"
        ports:
            - "8001:8000"
        secrets:
            - host_ssh_key    # `host_ssh_key` is declared below, in high level block `secrets`

    coder_manager:
        image: "fish_django_backend"
        build:
            context: buildaudit
            dockerfile: Dockerfile.django
        command: ["./manage.py", "service_appcheck_manager"]
        restart: always
        links:
            - db
            - rabbitmq
        volumes:
            - "./runtime/buildaudit.yaml:/opt/buildaudit.yaml"

    coder:
        build:
            context: coder
            # here no `dockerfile` argument, so it will run the default `Dockerfile` file, i guess..
        links:
            - rabbitmq
        restart: always

    rabbitmq:
        build:
            context: ./rabbitmq
        expose:
            - "5672"
            - "15672"
        ports:
            - "15673:15672"
            - "5673:5672"
        environment:
            - RABBITMQ_DEFAULT_USER=admin
            - RABBITMQ_DEFAULT_PASS=123456

    db:
        image: postgres:11.9
        expose:
            - "5432"
        ports:
            - "5433:5432"
        environment:
            - POSTGRES_USER=root
            - POSTGRES_PASSWORD=123456
        command: "-c config_file=/etc/postgresql/postgresql.conf"
        volumes:
            - "./runtime/fish-postgres.conf:/etc/postgresql/postgresql.conf"

    couchdb:
        build:
            context: couchdb
            dockerfile: Dockerfile
        restart: always
        environment:
            - COUCHDB_USER=123456
            - COUCHDB_PASSWORD=123456
        expose:
            - "5984"
        ports:
            - "5984:5984"
        volumes:
            - "./db/couchdb_data:/opt/couchdb/data"

volumes:      # Declare all volumes in this list, it's convenient to be referred by many places
    nfs-storage:
        driver: local
        driver_opts:
            type: nfs
            o: "addr=storage.micro-hard.com,ro,nolock"
            device: ":/storage1"

secrets:
    host_ssh_key:
        file: ~/.ssh/id_rsa
```

## K8S
- Run k8s locally
  - Minikube
    - Is it possible for minikube to run 2 clusters on one physical machine ?
      - I guess it's impossible, we use `minikube start` to start a cluster
    - Run a cluster with multiple nodes ?
      - `minikube start --nodes 2 -p multinode-demo`
    - `minikube dashboard`
- What's relationship between Deployment, Pod, Service ?
- kubeadm & kubelet & kubectl
- apiserver & 
- Control plane
- kind notation ?
- `configMapKeyRef`
- k9s
- Comparison of many kinds of k8s local simulate tools, kind, k3s, minikube.
- Nodeport, clusterIP
- Why service ?
- Why ingress ?
- Kustomize VS Helm
  - kustomize yaml
    - resources
    - configMapGenerator
    - patchesStrategicMerge
- Kubectl 内置 Kustomize, 怎么用呢？
- Loadblanch与Ingress的联系？
- services的selector是select pods which label matched，还是select deployments which label matched ?
- 一个pod多个containers，deployment yaml怎么写？
- 一个deployment多个pods怎么写？
- replicat 与 pod是one to one的关系吗？
- Is k8s node a physical computer ?
   - A node can be a physical machine or a virtual machine, and can be hosted on-premises or in the cloud.
- Nginx ingress controller

## Concourse
- What is concourse target, why fly -t (target) ?
- is concourse pipeline yaml file independent of concourse instance ? i mean a yaml file is able to run everywhere.
- groups
- var_sources
- inputs
- reveal: true
- in_parallel
- input_mapping / output_mapping


## Make
- make -p

## Helm
- Charts & release
- https://artifacthub.io/


## Python
- argparse nargs='+'
```
import signal, os

# 定义一个信号处理函数，该函数打印收到的信号，然后raise IOError
def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

# 对SIGALRM(终止)设置处理的handler, 然后设置定时器，5秒后触发SIGALRM信号
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.alarm(0)          # 关闭定时器
该示例实现的功能是，为了防止打开一个文件出错或者其他异常一直处于等待的状态，设定一个定时器，5秒后触发IOError。如果5s内正常打开文件，则清除定时器。
```

```
parser.add_argument(
    '--test',
    dest='test', default=None, type=int, help='test'
    action='store',     # 
)
```

### python3
from collections.abc import Iterable
typing module, TypedDict
```python
>>> def tt(kk: int, xx: Optional[int]):
...     print(kk)
>>> tt(None)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: tt() missing 1 required positional argument: 'xx'
```

run a simple httpserver
```shell
python3 -m http.server
```

Only compress files in folder, not include this folder.

```shell
tar -czvf python-3.10.6-with-openssl-3.0.5.tar.gz -C python-3.10.6/ .
```

## Owner of this site
- /etc/localtime
- apt-get update
- 动态库 & 静态库
- 向下兼容、向后兼容、向上兼容、向前兼容
## tox
https://tox.wiki/en/latest/

## Jira
todo

## skaffold
https://skaffold.dev

## kustomize
https://kustomize.io/
- patchesStrategicMerge

## k8s
- ConfigMap & secret
- Label, what, why

## Concourse
https://concourse-ci.org/resources.html
- resource_types、resources、var_sources、groups、jobs

- Practice

## RabbitMQ
- What is channel ? Why channel ?
- Channel is able to basic_consume and basic_publish ?


## Shell
- Is it possible to write a game by shell script ?
- Makefile
 - $(1) means ?
 - What does colon do in path ?


### My life and experiences
- Don't integrate other team API which is still on beta, not upgraded on production.
- atomic a series of operations.
- Never hardcode


### Software management
<b>What is the Difference Between Build and Release in Software Testing ?</b>

The main difference between Build and Release in Software Testing 

is that Build is a version of a software the development team hands over to the testing team for testing purposes

while Release is a software the testing team hands over to the customer.


<b>what is `deliverable` in software management ?</b>

todo

<b> project vs product </b>

It also leads to another questions

project manager vs product manager
project mindset vs product mindset

<b> inventory </b>

TODO

# Terms
- sandbox, what, why ?

# Angular
- angular vs angularJs
- What's the relationship between angular and Typescript ?

# Typescript
- online playground https://www.typescriptlang.org/play



## Mark
- 2022年09月12日11:17:14
```Shell
tar zcvf dist.tar.gz -C dist 
```

```Shell
python3 -m ensurepip
```

Shell 中的 `:=` ?

make all

```shell
ldconfig
```

```
symbolic links & hard links
```

```shell
vzhong@vzhong-vm-2:~/osspi-cli$ sudo ln -s /home/vzhong/osspi-cli/build/resources/openssl/Openssl-3.0.5/lib64/libcrypto.so.3 /usr/lib/libcrypto.so.3
```

```python
vzhong@vzhong-vm-2:~/osspi-cli$ sudo ln -s /home/vzhong/osspi-cli/build/resources/openssl/Openssl-3.0.5/lib64/libssl.so.3 /usr/lib/libssl.so.3
```

```shell
openssl: error while loading shared libraries: libssl.so.3
```

```shell
DYLD_LIBRARY_PATH=/home/vzhong/osspi-cli/build/python/lib:/home/vzhong/osspi-cli/build/resources/openssl/Openssl-3.0.5/lib64/ build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3 -m ensurepip
build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3: /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.29' not found (required by build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3)
build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3: /lib/x86_64-linux-gnu/libm.so.6: version `GLIBC_2.35' not found (required by build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3)
build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.28' not found (required by build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3)
build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.32' not found (required by build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3)
build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.33' not found (required by build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3)
build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found (required by build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3)
build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.33' not found (required by /usr/lib/libcrypto.so.3)
build/python/Python-3.10.7-with-openssl-3.0.5/bin/python3: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found (required by /usr/lib/libcrypto.so.3)
Makefile:121: recipe for target 'virtualenv' failed
make: *** [virtualenv] Error 1

solution:

wget https://ftp.gnu.org/gnu/libc/glibc-2.36.tar.gz

```

```shell
GNU M4 1.4.6 or later is required; 1.4.16 or newer is recommended.
```


```shell
/usr/bin/install -c /home/vzhong/glibc/glibc-2.36/build/elf/ld.so /lib64/ld-linux-x86-64.so.2.new
mv -f /lib64/ld-linux-x86-64.so.2.new /lib64/ld-linux-x86-64.so.2
rm -f /usr/bin/ld.so.new
Inconsistency detected by ld.so: dl-call-libc-early-init.c: 37: _dl_call_libc_early_init: Assertion `sym != NULL' failed!
Makefile:1390: recipe for target '/usr/bin/ld.so' failed
make[2]: *** [/usr/bin/ld.so] Error 127
make[2]: Leaving directory '/home/vzhong/glibc/glibc-2.36/elf'
Makefile:484: recipe for target 'elf/subdir_install' failed
make[1]: *** [elf/subdir_install] Error 2
make[1]: Leaving directory '/home/vzhong/glibc/glibc-2.36'
Makefile:12: recipe for target 'install' failed
make: *** [install] Error 2
```


```shell
Inconsistency detected by ld.so: dl-call-libc-early-init.c: 37: _dl_call_libc_early_init: Assertion `sym != NULL' failed!
```




## 2022年09月13日12:50:10
```python
subprocess.check_output(cmd, shell=True, text=True)
```

## 2022年09月14日16:42:30
linux install docker-compose

```shell
https://github.com/docker/compose/releases/tag/v2.10.2
https://github.com/docker/compose/releases/download/v2.10.2/docker-compose-linux-x86_64
```

2022年09月15日11:06:08
```shell
docker-compose stop & docker-compose down
```

Rebuild and restart container

```shell
docker-compose up --detach --build gunicorn
docker-compose up --build gunicorn
```

```
Referer is insecure while host is secure
```

2022年09月16日11:53:20
```shell

```

2022年09月19日13:40:15

```python
>>> 'http://xx.com'.lstrip('xhttfffff://p')
'.com'
```

scrum与waterfall，难道不是只是粒度变细了吗？

2022年09月20日10:09:50

```shell
curl --unix-socket /var/run/docker.sock http://localhost/version
```

- ingress-nginx

install docker on ubuntu
```shell
apt-get install docker.io
```

Crash & Crush

differences between `helpnow` and `servicedesk`


```shell
pytest tox.ini lint
```

```shell
coverage run --branch --source=. --omit=*/tests*,*__init__* -m unittest discover
```

---------
https://www.bilibili.com/video/BV1LD4y1o79K/?spm_id_from=autoNext&vd_source=f209dde1a1d76e06b060a034f36bb756

https://www.gutenberg.org/files/1998/1998-h/1998-h.htm

https://www.gutenberg.org/files/1998/1998-h/1998-h.htm#link2H_INTR

2022年09月21日10:49:03

- test --> side effect

- How coverage test a specific case ?

```python
>>> try:
...     assert 1==2
... except Exception as exc:
...     print(str(exc))
...

>>>
```

--------------------
2022年10月09日15:21:06

`LD_RUN_PATH和LD_LIBRARY_PATH是干什么的?`

module from so file ?
```python
>>> import _tkinter
>>>
>>> _tkinter
<module '_tkinter' from '/usr/local/python-3.10.6-with-openssl-3.0.5/lib/python3.10/lib-dynload/_tkinter.cpython-310-x86_64-linux-gnu.so'>
>>>
```

2022年09月22日14:01:09

- How do I run a docker instance from a DockerFile?

2022年09月23日13:50:44

github
```shell
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/zhongpengqun/mirror.git/'
```
s: https://stackoverflow.com/questions/68775869/message-support-for-password-authentication-was-removed-please-use-a-personal


2022年09月26日15:31:05

- echo $(PWD) 啥都没有..



- 沟通技巧

2022年09月27日15:25:27
- 动态库与静态库

2022年09月30日10:34:26

- what's standard output standard input ?

2022年10月04日09:14:39

- echo $?


### Work
  - [Note](./note.html)
  - 技术选型怎么做?
  - 如何熟悉新项目    /自问自答
  - Professional
    - 计算机组成原理 
      - 科学计数法 & 浮点数
  - Project details understanding
  - [K8s studying](./k8s-studying.html)
  - Django-rest-framework
      - 2种url参数的区别，为什么要这样？
  - RabbitMQ
  - JIRA
  - Django
      - safe url
      - url endswith '/' & not endswith
      - Path Parameters
  - Python
      - python 3
      - logging
      - urllib urlparse
      -         "message": "Dangerous default value {} as argument",
      - super 放在不同的位置会怎样？
      - when staticmethod, when classmethod ?
      - collections
      - array & list
      - lambda, filter
  - Git
      - Git branch strategy
  - Society studying & Social practice
    - Laws of the People's Republic of China
  - OS
    - Lock
    - linux cpio
  - Remote edit
  - [Software Life Circle](./software-life-circle.html)
  - [Angular](./angular.html)
  - code snippet
  - The experience of using grafana

## Study
  - [English Studying](./english-studying.html)
  - [Translation](./translation.html)
  - Linux 0.0.1

  - Road traffic laws and rules
    - [Motorcycles i might buy](./motorcycles.html)

  - English Reading Notes
    - Thus spoke Zarathustra
    - https://www.quora.com/Did-Nietzsche-have-any-dark-secrets
    - [The Communist Manifesto](./the-communist-manifesto.html)


- [back](./)
