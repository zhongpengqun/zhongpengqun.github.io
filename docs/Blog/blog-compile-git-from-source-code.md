yum install wget

```
# make configure
GIT_VERSION = 2.41.GIT
    GEN configure
/bin/sh: autoconf: command not found

soulution:
yum install install autoconf automake libtool
```

then
```
make configure
./configure --prefix=/usr/local

make all
make install
```

```
# make prefix=/usr/local/git all
    CC oss-fuzz/fuzz-commit-graph.o
In file included from oss-fuzz/fuzz-commit-graph.c:1:0:
./git-compat-util.h:14:2: error: #error "Required C99 support is in a test phase.  Please see git-compat-util.h for more details."
 #error "Required C99 support is in a test phase.  Please see git-compat-util.h for more details."
  ^
make: *** [oss-fuzz/fuzz-commit-graph.o] Error 1


solution: success
https://blog.csdn.net/qq_46311811/article/details/122273064

then
$ make prefix=/usr/local/git all

    CC http.o
In file included from http.c:2:0:
http.h:6:10: fatal error: curl/curl.h: No such file or directory
 #include <curl/curl.h>
          ^~~~~~~~~~~~~
compilation terminated.
Makefile:2121: recipe for target 'http.o' failed
make: *** [http.o] Error 1


git pull raise error:
fatal: Unable to find remote helper for 'https'

reason:
 happen when compiling git on a machine which doesn't have all the dependencies available. Most likely one of libcurl-gnutls or libgnutls is missing on your system.

solution:
$ export PATH=$PATH:/tmp/git/libexec/git-core

but another raised:

/tmp/git/libexec/git-core/git-remote-https: error while loading shared libraries: libcurl.so.4: cannot open shared object file: No such file or directory
```


References:
- https://www.jiweichengzhu.com/article/eec6ae191bcd44428bc5b2d49baae31c
