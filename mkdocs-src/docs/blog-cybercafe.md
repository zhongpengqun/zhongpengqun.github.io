When in cybercafe i feel relax


### NFS server
- My OS
  ```shell
  $cat /proc/version
  Linux version 4.15.0-135-generic (buildd@lgw01-amd64-005) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #139-Ubuntu SMP Mon Jan 18 17:38:24 UTC 2021
  ```

```shell
reference: https://blog.csdn.net/iriczhao/article/details/126149918

$ sudo apt-get install nfs-kernel-server
$ mkdir /home/nfs/
$ /etc/init.d/rpcbind restart
$ /etc/init.d/nfs-kernel-server restart
$ showmount -e
```


##### Windows connect ubuntu NFS server
reference: https://blog.csdn.net/SanShuiGeGe/article/details/125030065
```shell
mount 139.196.39.92:/home/nfs Z:
```