#### Deploy Gitlab
<a href='https://docs.gitlab.com/ee/install/docker.html'> Official tutorial </a>

I choose Helm to deploy gitlab on cluster, for i'd like to have a practise on Helm.

Basically, i referred to this articles

https://www.yangpiqiulaotou.cn/2021/03/25/helm3%E5%AE%89%E8%A3%85gitlab/
https://cloud.tencent.com/developer/article/1471464
https://www.jianshu.com/p/024aa83f1dac

### prerequisite
kubectl create ns gitlab
kubectl config set-context --current --namespace=gitlab
kubectl config get-contexts


helm upgrade --install gitlab gitlab-jh/gitlab \
  --version 5.6.2 \
  --timeout 600s \
  --set global.hosts.domain=example.com \
  --set global.hosts.externalIP=10.79.128.59 \
  --set certmanager-issuer.email=me@example.com

##### setup Helm  and then helm install gitlab
- Install Helm
https://helm.sh/docs/intro/install/


Add Helm repo source, btw, what does repo source do ?
```shell
helm repo add stable https://kubernetes-charts.storage.googleapis.com
helm repo add aliyun https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts
helm repo add  apphub https://apphub.aliyuncs.com/

```

```shell
vz@vz:~$ sudo snap install helm

error: This revision of snap "helm" was published using classic confinement and thus may perform
       arbitrary system changes outside of the security sandbox that snaps are usually confined to,
       which may put your system at risk.

       If you understand and want to proceed repeat the command including --classic.
```


https://gitlab-docs.creationline.com/charts/installation/deployment.html

<hr>

Give it up temporarily



### K8S deploy gitlab 
refer to https://medium.com/@SergeyNuzhdin/how-to-easily-deploy-gitlab-on-kubernetes-75f5868cea78
failed !
```shell
$ kubectl create -f gitlab/redis-deployment.yml
error: resource mapping not found for name: "gitlab-redis" namespace: "gitlab" from "gitlab/redis-deployment.yml": no matches for kind "Deployment" in version "extensions/v1beta1"
ensure CRDs are installed first


solution: ↓
$ k version --short
Flag --short has been deprecated, and will be removed in the future. The --short output will become the default.
Client Version: v1.25.4
Kustomize Version: v4.5.7
Server Version: v1.25.2

$ k convert
error: unknown command "convert" for "kubectl"
----
command convert has removed from kubectl since 1.22 --- https://github.com/kubernetes/website/issues/28724
- install convert https://www.cnblogs.com/varden/p/15907141.html
  - $ curl -LO https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl-convert
  - $ sudo install -o root -g root -m 0755 kubectl-convert /usr/local/bin/kubectl-convert

-- convert usage
$ kubectl-convert -f gitlab-deployment.yaml --output-version apps/v1
$ kubectl-convert -f gitlab-ingress.yaml --output-version networking.k8s.io/v1  

## todo
online kubectl convert

```

- K8S的apiVersion该用哪个
https://segmentfault.com/a/1190000017134399


### Deploy gitlab on k8s --2   (not succeed)
refer to 
https://www.qikqiak.com/post/gitlab-install-on-k8s/

```shell
$ kubectl get pods -n kube-ops
NAME                          READY   STATUS             RESTARTS   AGE
gitlab-6cdc798c55-tdrjx       0/1     ImagePullBackOff   0          8m3s
postgresql-77cc99bc49-s8sjq   0/1     ImagePullBackOff   0          11m
redis-594bb69b45-8ds69        0/1     ImagePullBackOff   0          134m
```
