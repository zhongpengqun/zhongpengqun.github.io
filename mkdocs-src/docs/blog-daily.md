```shell
$ docker-compose up -d

...
ERROR: for nginx  Cannot start service nginx: driver failed programming external connectivity on endpoint hello_nginx_1 (769fdb4f19f704b9f838957b5601c7c54d7288ede933eff3d16a1ce72e74d096): Error starting userland proxy: listen tcp4 0.0.0.0:80: bind: address already in use
ERROR: Encountered errors while bringing up the project
```
Port 80 has been \#占用\#, let's have a look which process is using it.

```shell
$ netstat -tunlp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:9200            0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:9300            0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:8088            0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:15672           0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:8025            0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:8191            0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:1025            0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:5672            0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:34443         0.0.0.0:*               LISTEN      -
tcp6       0      0 :::111                  :::*                    LISTEN      -
tcp6       0      0 :::9200                 :::*                    LISTEN      -
tcp6       0      0 :::80                   :::*                    LISTEN      -
tcp6       0      0 :::9300                 :::*                    LISTEN      -
tcp6       0      0 :::22                   :::*                    LISTEN      -
tcp6       0      0 :::8088                 :::*                    LISTEN      -
tcp6       0      0 :::15672                :::*                    LISTEN      -
tcp6       0      0 :::8025                 :::*                    LISTEN      -
tcp6       0      0 :::1025                 :::*                    LISTEN      -
tcp6       0      0 :::5672                 :::*                    LISTEN      -
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -
udp        0      0 0.0.0.0:111             0.0.0.0:*                           -
udp        0      0 0.0.0.0:828             0.0.0.0:*                           -
udp6       0      0 :::111                  :::*                                -
udp6       0      0 :::828                  :::*
```
Field `PID/Program name` is blank, we should sudo execute cmd `netstat`

```shell
$ sudo netstat -tunlp
[sudo] password for vz:
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      652/rpcbind
tcp        0      0 0.0.0.0:9200            0.0.0.0:*               LISTEN      3887994/docker-prox
tcp        0      0 0.0.0.0:9300            0.0.0.0:*               LISTEN      3887918/docker-prox
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      751/systemd-resolve
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1081/sshd
tcp        0      0 0.0.0.0:8088            0.0.0.0:*               LISTEN      3888818/docker-prox
tcp        0      0 0.0.0.0:15672           0.0.0.0:*               LISTEN      3887898/docker-prox
tcp        0      0 0.0.0.0:8025            0.0.0.0:*               LISTEN      3887874/docker-prox
tcp        0      0 0.0.0.0:8191            0.0.0.0:*               LISTEN      18346/mongod
tcp        0      0 0.0.0.0:1025            0.0.0.0:*               LISTEN      3887937/docker-prox
tcp        0      0 0.0.0.0:5672            0.0.0.0:*               LISTEN      3887957/docker-prox
tcp        0      0 127.0.0.1:34443         0.0.0.0:*               LISTEN      976/containerd
tcp6       0      0 :::111                  :::*                    LISTEN      652/rpcbind
tcp6       0      0 :::9200                 :::*                    LISTEN      3888007/docker-prox
tcp6       0      0 :::80                   :::*                    LISTEN      3805375/apache2
tcp6       0      0 :::9300                 :::*                    LISTEN      3887924/docker-prox
tcp6       0      0 :::22                   :::*                    LISTEN      1081/sshd
tcp6       0      0 :::8088                 :::*                    LISTEN      3888851/docker-prox
tcp6       0      0 :::15672                :::*                    LISTEN      3887903/docker-prox
tcp6       0      0 :::8025                 :::*                    LISTEN      3887881/docker-prox
tcp6       0      0 :::1025                 :::*                    LISTEN      3887943/docker-prox
tcp6       0      0 :::5672                 :::*                    LISTEN      3887963/docker-prox
udp        0      0 127.0.0.53:53           0.0.0.0:*                           751/systemd-resolve
udp        0      0 0.0.0.0:111             0.0.0.0:*                           652/rpcbind
udp        0      0 0.0.0.0:828             0.0.0.0:*                           652/rpcbind
udp6       0      0 :::111                  :::*                                652/rpcbind
udp6       0      0 :::828                  :::*                                652/rpcbind
```
All right! Next stop apache2

```shell
sudo systemctl stop apache2
```