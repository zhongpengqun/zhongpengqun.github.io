### Setup a Splunk server

Run a Splunk server container

```shell
docker run --name splunk -p 8000:8000 -p 8088:8088 -d outcoldman/splunk:6.3.3
```

- startup a splunk server
    - docker-compose.yaml
```
version: "3"
services:
  splunk:
    container_name: splunk
    user: root
    image: outcoldman/splunk:6.3.3
    ports:
      - "8000:8000"
```

- Splunk
    - https://www.youtube.com/watch?v=m95GiTF0zd0
    - https://www.youtube.com/watch?v=bO_-fv6e7u4
    - https://medium.com/airwalk/log-aggregation-in-kubernetes-and-transporting-logs-to-splunk-for-analysis-ad8599607372
    - https://cloud.google.com/architecture/logging-anthos-with-splunk-connect?hl=zh-cn
    - k8s logs
        - objects
        - metrics


setup a splunk server:
```shell
docker run --name splunk -p 8000:8000 -p 8088:8088 -d outcoldman/splunk:6.3.3


docker run --name hello --log-driver=splunk --log-opt splunk-token=AEB5A127-3AC2-447C-8E3F-D7027AFE31D1 --log-opt splunk-url=http://139.196.39.92:8088 --log-opt splunk-sourcetype=Docker rickfast/hello-oreilly


docker run --name hello --log-driver=splunk --log-opt splunk-token=A3260AEC-672D-41D2-9B64-8BAB933EA5DE --log-opt splunk-url=http://139.196.39.92:8088 --log-opt splunk-sourcetype=Docker rickfast/hello-oreilly



docker run --name hello --log-driver=splunk --log-opt splunk-token=1620a639-5064-43dc-8d81-72ae38ec639b --log-opt splunk-url=http://10.79.128.59:8088 --log-opt splunk-sourcetype=Docker rickfast/hello-oreilly

minikube start --nodes 4 --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 1

minikube start --nodes 4 --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 1 --driver=docker
```

- Splunk 可以用来分析网站是否被黑客扫描

- vmware kube-fluentd-operator
    - https://pkg.go.dev/github.com/vmware/kube-fluentd-operator#section-readme





```shell
$ curl -k http://139.196.39.92:8088/services/collector/event -H "Authorization: Splunk AEB5A127-3AC2-447C-8E3F-D7027AFE31D1" -d '{"event": "hello world"}'
{"text":"Success","code":0}
```

=============

splunk log success: https://www.youtube.com/watch?v=qROXrFGqWAU&t=11s

curl https://10.79.128.59:8088/services/collector/event -H "Authorization: Splunk 1620a639-5064-43dc-8d81-72ae38ec639b" -d '{"event": "hello world"}'

docker built-in send log to splunk ?
https://www.w3cschool.cn/doc_docker_1_13/docker_1_13-engine-admin-logging-splunk-index.html

install splunk by cmd
https://www.inmotionhosting.com/support/security/install-splunk/

9ED0A79E-F7B8-43DC-B7A0-7B49AE7450B9

```shell
root@iZuf6bpc1lt9qlf2ma9p2lZ:~# helm install anthos-splunk -f values.yaml --namespace splunk-connect https://github.com/splunk/splunk-connect-for-kubernetes/releases/download/1.4.1/splunk-connect-for-kubernetes-1.4.1.tgz

Error: INSTALLATION FAILED: Get "https://github.com/splunk/splunk-connect-for-kubernetes/releases/download/1.4.1/splunk-connect-for-kubernetes-1.4.1.tgz": unexpected EOF
```


```shell
$ kubectl create namespace splunk-connect
$ kubectl config set-context --current --namespace=splunk-connect
$ 
helm install anthos-splunk -f values.yaml --namespace splunk-connect https://github.com/splunk/splunk-connect-for-kubernetes/releases/download/1.4.1/splunk-connect-for-kubernetes-1.4.1.tgz
``` 

- Splunk indexer
    - 相当于一个database
    - 我们查询日志的时候，要先确认筛选是哪个database。
默认index：main (如果转发过来的数据不指定索引，则会保存在默认的main索引中)

- source
    - 对于从文件和目录监视的数据, source的值是路径，比如 /var/log
    - 基于网络的是协议和端口, 比如 UDP: 514
- sourcetype
    - 是其来源的数据输入的格式，sourceType决定了数据的格式化方式。选择不同的sourceType，Splunk自动识别的常见源类型列表包括NCSA组合格式HTTP Web服务器日志，标准Apache Web服务器错误日志，Cisco网络设备（包括PIX防火墙，路由器，ACS等）生成的标准syslog。查询还可以根据sourceType来筛选


- fluent-plugin-splunk-hec
    - https://github.com/splunk/fluent-plugin-splunk-hec
- kube-fluentd-operator
    - https://github.com/vmware/kube-fluentd-operator


```
#0 unexpected error error_class=RestClient::SSLCertificateNotVerified error="SSL_connect returned=1 errno=0 state=error: certificate verify failed (self signed certificate in certificate chain)"

solution:
https://anujarosha.medium.com/sending-logs-to-splunk-using-fluent-plugin-splunk-hec-fluentd-output-plugin-462baba53b4f
```


