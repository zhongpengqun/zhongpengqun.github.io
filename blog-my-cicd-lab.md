---
layout: default
title: Journal
description: The main aim is to improve my English.
---

## Purpose
To run a complete project that life cycle managed by CI/CD.

## Prerequsites

#### Setup k8s cluster locally
you can use `minikube` to do it.

- Install minikube
```shell
$ curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube
$ sudo mv -v minikube /usr/local/bin
$ minikube version
```
- Install kubectl
https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

For me, ubuntu
```shell
snap install kubectl --classic
kubectl version --client
```

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

### Deploy gitlab by docker-compose (succeed !!!)
refer to https://www.czerniga.it/2021/11/14/how-to-install-gitlab-using-docker-compose/

```shell
mkdir gitlab
export GITLAB_HOME=$(pwd)/gitlab

cd gitlab

vim docker-compose.yml
-------------------------
version: '3.7'
services:
  web:
    image: 'gitlab/gitlab-ce:latest'
    restart: always
    hostname: 'localhost'
    container_name: gitlab-ce
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://localhost'
    ports:
      - '8080:80'
      - '8443:443'
    volumes:
      - '$GITLAB_HOME/config:/etc/gitlab'
      - '$GITLAB_HOME/logs:/var/log/gitlab'
      - '$GITLAB_HOME/data:/var/opt/gitlab'
    networks:
      - gitlab
  gitlab-runner:
    image: gitlab/gitlab-runner:alpine
    container_name: gitlab-runner    
    restart: always
    depends_on:
      - web
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - '$GITLAB_HOME/gitlab-runner:/etc/gitlab-runner'
    networks:
      - gitlab

networks:
  gitlab:
    name: gitlab-network
-------------------

docker-compose up -d
after about 2 minutes, when the pod startup successfully.
then access login page, e.g http://10.79.128.59:8080/users/sign_in

To get passwoed:
docker exec -it gitlab-ce /bin/sh
cat /etc/gitlab/initial_root_password


-------
vz@vz:~/gitlab$ docker exec -it gitlab-runner gitlab-runner register --url "http://gitlab-ce" --clone-url "http://gitlab-ce"
Runtime platform                                    arch=amd64 os=linux pid=16 revision=133d7e76 version=15.6.1
WARNING: The 'register' command has been deprecated in GitLab Runner 15.6 and will be replaced with a 'deploy' command. For more information, see https://gitlab.com/gitlab-org/gitlab/-/issues/380872 
Running in system-mode.                            
                                                   
Enter the GitLab instance URL (for example, https://gitlab.com/):
[http://gitlab-ce]: http://10.79.128.59:8080
Enter the registration token:
Ju7NhyV59_a93mvxeUuc
Enter a description for the runner:
[a9e996f49f79]: gitlab-runner
Enter tags for the runner (comma-separated):

Enter optional maintenance note for the runner:

Registering runner... succeeded                     runner=Ju7NhyV5
Enter an executor: docker+machine, instance, kubernetes, custom, docker-ssh, parallels, virtualbox, docker-ssh+machine, docker, shell, ssh:
docker
Enter the default Docker image (for example, ruby:2.7):

Enter the default Docker image (for example, ruby:2.7):
maven: latest
Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded!
 
Configuration (with the authentication token) was saved in "/etc/gitlab-runner/config.toml" 

↑ As we can see, config file(/etc/gitlab-runner/config.toml) has generated in runner container. let's check it

/ # cat /etc/gitlab-runner/config.toml
concurrent = 1
check_interval = 0
shutdown_timeout = 0

[session_server]
  session_timeout = 1800

[[runners]]
  name = "gitlab-runner"
  url = "http://10.79.128.59:8080"
  id = 1
  token = "A8tE7CQMxuMVLzRkqGGa"
  token_obtained_at = 2022-11-27T09:45:23Z
  token_expires_at = 0001-01-01T00:00:00Z
  executor = "docker"
  clone_url = "http://gitlab-ce"
  [runners.custom_build_dir]
  [runners.cache]
    MaxUploadedArchiveSize = 0
    [runners.cache.s3]
    [runners.cache.gcs]
    [runners.cache.azure]
  [runners.docker]
    tls_verify = false
    image = "maven: latest"
    privileged = false
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = false
    volumes = ["/cache"]
    shm_size = 0
```

Example of file `.gitlab-ci.yml`
```shell
image: maven:latest

stages:
  - build
  - test

build-job:
  stage: build
  script:
    - echo "Compiling the code..."
    - mvn clean package
    - echo "Compile complete."
  artifacts:    # https://meigit.readthedocs.io/en/latest/gitlab_ci_.gitlab-ci.yml_detail.html#artifacts
    paths:
    - target   

test-job:
  stage: test
  dependencies: 
    - build-job  
  script:
    - ls -al
    - echo "Running tests"
    - java -cp target/helloworld-1.1.jar com.coveros.demo.helloworld.HelloWorld
```

### TODO, concourse with gitlab
##### concourse
- Adventage
  - Config file is complete yaml, so it can be managed by git or other version controller.
- Short-coming
  - Yaml file too long.
  - Is there any thing can generate concourse yaml file?



### Jira
- Is it free ?
- How to deploy Jira use docker ?
```shell
docker run --detach --publish 8080:8080 cptactionhank/atlassian-jira:latest
```

### kustomize
- Why Kustomize ?
```shell
xx
```
- Kustomize VS Helm
- Helm DSL syntax ?

### concourse
- deploy

```shell
vz@vz:~/kubernetes-gitlab/another-try$ helm repo add bitnami https://charts.bitnami.com/bitnami
"bitnami" already exists with the same configuration, skipping
vz@vz:~/kubernetes-gitlab/another-try$ helm install my-release bitnami/concourse
NAME: my-release
LAST DEPLOYED: Wed Nov 23 15:52:21 2022
NAMESPACE: kube-ops
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: concourse
CHART VERSION: 2.0.0
APP VERSION: 7.8.3

** Please be patient while the chart is being deployed **
###############################################################################
### ERROR: You did not provide an external host in your 'helm install' call ###
###############################################################################

This deployment will be incomplete until you configure Concourse with a resolvable
host. To configure Concourse with the URL of your service:

1. Get the Concourse URL by running:

  NOTE: It may take a few minutes for the LoadBalancer IP to be available.
        Watch the status with: 'kubectl get svc --namespace kube-ops -w my-release-concourse-web'

    export APP_HOST=$(kubectl get svc --namespace kube-ops my-release-concourse-web --template "{{ range (index .status.loadBalancer.ingress 0) }}{{ . }}{{ end }}")

2. Complete your Concourse deployment by running:
    export LOCAL_USERS=$(kubectl get secret --namespace "kube-ops" my-release-concourse-web -o jsonpath="{.data.local_users}" | base64 -d)
    helm upgrade --namespace kube-ops my-release my-repo/concourse \
      --set secrets.localUsers=$LOCAL_USERS \
      --set service.web.type=LoadBalancer \
      --set web.externalUrl=$APP_HOST
```

[back](./)
