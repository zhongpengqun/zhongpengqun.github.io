#### TODO
- 写成docker-compose

#### Run a k8s cluster
First of all, have to start a k8s cluster, can use `minikube` to do it.

- Install minikube
```shell
$ curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube
$ sudo mv -v minikube /usr/local/bin
$ minikube version
```
- Install kubectl， https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

For me, ubuntu OS

```
snap install kubectl --classic
kubectl version --client
```

Start cluster.
```
minikube start --nodes 2 --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 2 --kubernetes-version=v1.23.1 --memory=12000
```

#### Concourse

`docker-compose.yaml`

```
version: '3'

services:
  concourse-db:
    image: postgres
    environment:
      POSTGRES_DB: concourse
      POSTGRES_PASSWORD: concourse_pass
      POSTGRES_USER: concourse_user
      PGDATA: /database

  concourse:
    image: concourse/concourse
    command: quickstart
    privileged: true
    depends_on: [concourse-db]
    ports: ["8081:8080"]
    environment:
      CONCOURSE_POSTGRES_HOST: concourse-db
      CONCOURSE_POSTGRES_USER: concourse_user
      CONCOURSE_POSTGRES_PASSWORD: concourse_pass
      CONCOURSE_POSTGRES_DATABASE: concourse
      #CONCOURSE_EXTERNAL_URL: http://localhost:8081
      CONCOURSE_EXTERNAL_URL: http://121.40.207.10:8081
      CONCOURSE_ADD_LOCAL_USER: test:test
      CONCOURSE_MAIN_TEAM_LOCAL_USER: test
      # instead of relying on the default "detect"
      #CONCOURSE_WORKER_BAGGAGECLAIM_DRIVER: overlay
      CONCOURSE_CLIENT_SECRET: Y29uY291cnNlLXdlYgo=
      CONCOURSE_TSA_CLIENT_SECRET: Y29uY291cnNlLXdvcmtlcgo=
      CONCOURSE_X_FRAME_OPTIONS: allow
      CONCOURSE_CONTENT_SECURITY_POLICY: "*"
      CONCOURSE_CLUSTER_NAME: tutorial
      CONCOURSE_WORKER_CONTAINERD_DNS_SERVER: "8.8.8.8"
      CONCOURSE_WORKER_RUNTIME: "containerd"
```

Deploy it by cmd `docker-compose up -d`

username: `test`
pwd: `test`

#### Gitlab

There are 2 ways to deploy a Gitlab, i tried, all succeed !

**1.**

```
mkdir -p /home/gitlab/etc/gitlab	
mkdir -p /home/gitlab/var/log
mkdir -p /home/gitlab/var/opt

docker run -d -h gitlab -p 443:443 -p 8090:80  -p 8022:22  --name gitlab  --restart  always   -v /root/data/gitlab/config:/etc/gitlab  -v /root/data/gitlab/logs:/var/log/gitlab -v  /root/data/gitlab/data:/var/opt/gitlab  public.ecr.aws/y5z1i2v3/zhongpengqun:gitlab-ce
```

PS: it will take minutes to finish starting, during these minutes, the gitlab dashboard will keep showing 502, so be patient.


Username is `root`, and password is in `/etc/gitlab/initial_root_password`, you can run command:
```
docker exec -it $(docker ps |grep "gitlab/gitlab-ce" | awk '{ print $1 }') cat /etc/gitlab/initial_root_password
```
to get it.

Next, we need to register a Runner to gitlab, GitLab Runner is the open source project that is used to run your jobs and send the results back to GitLab.

Refer to: https://docs.gitlab.com/runner/install/docker.html#option-1-use-local-system-volume-mounts-to-start-the-runner-container

Run Runner container

```
docker run -d --name gitlab-runner --restart always \
  -v /srv/gitlab-runner/config:/etc/gitlab-runner \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:latest
```

Register runner to gitlab




**2.**

Refer to `https://www.czerniga.it/2021/11/14/how-to-install-gitlab-using-docker-compose/`

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


------- Register Runner
$ docker exec -it gitlab-runner gitlab-runner register --url "http://gitlab-ce" --clone-url "http://gitlab-ce"
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









#### JFrog
Use cloud trial edition, https://nonezhong.jfrog.io/ui/repos/tree/General/docker


#### Concourse
- Installation


#### Trigger Concourse Pipeline when Commit Gitlab MR or Merge Request.
xx


#### Jenkins
- Installation
```
docker run --name jenkins-blueocean --restart=on-failure --detach \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8082:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  public.ecr.aws/y5z1i2v3/zhongpengqun:jenkins-lts-jdk11
```
  - admin zpq123456

- 我的gitlab为什么没有network settings ？
  - 直接 /admin 进入page

#### Gitlab触发Jenkins
  - 配置gitlab的webhook
  - Gitlab配置Webhooks时Secret Token从Jenkins获取方法
    - https://blog.csdn.net/BUG_88/article/details/108365817



[back](./)
