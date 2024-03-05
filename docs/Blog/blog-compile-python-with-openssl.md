---
layout: default
title: Hello
description: ..
---
This blog is a tutorial of how to compile `python 3.10.6` with `openssl 3.0.5` module on `Ubuntu 18.04` and `mac os`.

### Questions
- Python默认是没装ssl的吗？

### ↓ On Ubuntu 18.04

Steps:

- [Prepare ubuntu container](#prepare)
- [Compile openssl](#openssl)
- [Compile python](#python)

Further:
- [Issues encountered in the process](#issues)
- [References](#references)


### ↓ On Mac OS

Steps:

- [Prepare Mac OS](#prepare_mac)
- [Compile openssl](#openssl)
- [Compile python](#python)

Further:
- [References](#mac_references)

### ↓ On Centos5.8

Steps:
# todo


### ↓ On Macos EI Capitan
# todo

## <a name='prepare'>Run Ubuntu container and install required packages</a>

I will demo it in Ubuntu docker container.

So first of all, run a ubuntu container there is no python installed.

```shell
docker run -it ubuntu:bionic /bin/bash
```

As you can see, python is not installed

```shell
$ python
bash: python: command not found

$ python3
bash: python3: command not found
```

↓ OS info

```shell
$ cat /etc/os-release
NAME="Ubuntu"
VERSION="18.04.6 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.6 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
```

#### Install packages

Below packages are required for compilation, otherwise will raise various errors during process.

```shell
apt-get update
apt-get install vim -y

$ vim install-pkgs.sh

#!/bin/sh
apt-get install wget -y
apt-get install make -y
apt-get install perl -y
apt-get install gcc -y
apt-get install make -y
apt-get install tcl-dev -y
apt-get install tk-dev -y
apt-get install tk -y
apt-get install libffi-dev -y
apt-get install libreadline-dev -y
apt-get install readline-devel -y
apt-get install libbz2-dev -y
apt-get install python3-tk -y
apt-get install libgdbm-dev -y
apt-get install libncurses* -y
apt-get install libgdbm-compat-dev -y
apt-get install libreadline6-dev -y
apt-get install uuid-dev -y
apt-get install lzma-dev -y
apt-get install liblzma-dev -y
```

Install packages
```shell
chmod 777 install-pkgs.sh
./install-pkgs.sh
```

#### Compile sqlite beforehand
```shell
wget https://www.sqlite.org/2018/sqlite-autoconf-3240000.tar.gz
tar -xvzf sqlite-autoconf-3240000.tar.gz
cd sqlite-autoconf-3240000
./configure
make 
make install
```

if not compile sqlite, will get below issue when compile python.

```shell

The necessary bits to build these optional modules were not found:
_sqlite3

```


## <a name='openssl'>Compile openssl<a>

##### <a name='download_openssl'>Download openssl</a>

Download latest openssl

Go to github <a href="https://github.com/openssl/openssl/tags">openssl tags</a>, select the latest openssl version.
```shell
wget https://github.com/openssl/openssl/archive/refs/tags/openssl-3.0.5.tar.gz
tar -xvzf openssl-3.0.5.tar.gz
```

##### Config

```shell
mkdir /usr/local/openssl-3.0.5

$ ./config --prefix=/usr/local/openssl-3.0.5 --openssldir=/usr/local/openssl-3.0.5
Configuring OpenSSL version 3.0.5 for target linux-x86_64
Using os-specific seed configuration
Created configdata.pm
Running configdata.pm
Created Makefile.in
Created Makefile
Created include/openssl/configuration.h

**********************************************************************
***                                                                ***
***   OpenSSL has been successfully configured                     ***
***                                                                ***
***   If you encounter a problem while building, please open an    ***
***   issue on GitHub <https://github.com/openssl/openssl/issues>  ***
***   and include the output from the following command:           ***
***                                                                ***
***       perl configdata.pm --dump                                ***
***                                                                ***
***   (If you are new to OpenSSL, you might want to consult the    ***
***   'Troubleshooting' section in the INSTALL.md file first)      ***
***                                                                ***
**********************************************************************
```

config successfully





##### Make & install
It will take several minutes

```shell
make

------------ log ---------------
...
/usr/bin/perl "-I." -Mconfigdata "util/dofile.pl" \
    "-oMakefile" util/shlib_wrap.sh.in > "util/shlib_wrap.sh"
chmod a+x util/shlib_wrap.sh
rm -f "util/wrap.pl"
/usr/bin/perl "-I." -Mconfigdata "util/dofile.pl" \
    "-oMakefile" util/wrap.pl.in > "util/wrap.pl"
chmod a+x util/wrap.pl
make[1]: Leaving directory '/home/openssl-openssl-3.0.5'
```

```shell
make install

------------- log --------------
...
install doc/html/man7/provider-signature.html -> /usr/local/openssl-3.0.5/share/doc/openssl/html/man7/provider-signature.html
install doc/html/man7/provider-storemgmt.html -> /usr/local/openssl-3.0.5/share/doc/openssl/html/man7/provider-storemgmt.html
install doc/html/man7/provider.html -> /usr/local/openssl-3.0.5/share/doc/openssl/html/man7/provider.html
install doc/html/man7/proxy-certificates.html -> /usr/local/openssl-3.0.5/share/doc/openssl/html/man7/proxy-certificates.html
install doc/html/man7/ssl.html -> /usr/local/openssl-3.0.5/share/doc/openssl/html/man7/ssl.html
install doc/html/man7/x509.html -> /usr/local/openssl-3.0.5/share/doc/openssl/html/man7/x509.html
```

When installation done, you will find these compiled files under `/usr/local/openssl-3.0.5`, for you config it as `--prefix`

```shell
ls /usr/local/openssl-3.0.5

bin  certs  ct_log_list.cnf  ct_log_list.cnf.dist  include  lib64  misc  openssl.cnf  openssl.cnf.dist  private  share
```



## <a name='python'>Compile Python</a>

##### Download latest python

```shell
wget https://www.python.org/ftp/python/3.10.6/Python-3.10.6.tgz
tar -xvzf Python-3.10.6.tgz
cd Python-3.10.6
```


##### Edit Setup

edit `Modules/Setup`, some python version might be `Modules/Setup.dist`, but this version, this is `Modules/Setup`

```shell
vim Modules/Setup

```
Below is what i changed, at about line 207


```shell
_socket socketmodule.c

# Socket module helper for SSL support; you must comment out the other
# socket line above, and edit the OPENSSL variable:
OPENSSL=/usr/local/openssl-3.0.5
# _ssl _ssl.c \
#     -I$(OPENSSL)/include -L$(OPENSSL)/lib \
#     -lssl -lcrypto
#_hashlib _hashopenssl.c \
#     -I$(OPENSSL)/include -L$(OPENSSL)/lib \
#     -lcrypto

# To statically link OpenSSL:
_ssl _ssl.c \
     -I$(OPENSSL)/include -L$(OPENSSL)/lib64 \
     -l:libssl.a -Wl,--exclude-libs,libssl.a \
     -l:libcrypto.a -Wl,--exclude-libs,libcrypto.a
_hashlib _hashopenssl.c \
     -I$(OPENSSL)/include -L$(OPENSSL)/lib64 \
     -l:libcrypto.a -Wl,--exclude-libs,libcrypto.a
```

##### Config

```shell
export LD_RUN_PATH=/usr/local/openssl-3.0.5/lib64
./configure --prefix=/usr/local/python-3.10.6-with-openssl-3.0.5 --with-openssl=/usr/local/openssl-3.0.5/ --enable-shared

----------- log ------------
...
config.status: creating pyconfig.h
creating Modules/Setup.local
creating Makefile


If you want a release build with all stable optimizations active (PGO, etc),
please run ./configure --enable-optimizations
```

##### Install

It will take several minutes

```shell
make

-------------- log ------------
...
gcc -pthread -shared build/temp.linux-x86_64-3.10/home/Python-3.10.6/Modules/_sqlite/cache.o build/temp.linux-x86_64-3.10/home/Python-3.10.6/Modules/_sqlite/connection.o build/temp.linux-x86_64-3.10/home/Python-3.10.6/Modules/_sqlite/cursor.o build/temp.linux-x86_64-3.10/home/Python-3.10.6/Modules/_sqlite/microprotocols.o build/temp.linux-x86_64-3.10/home/Python-3.10.6/Modules/_sqlite/module.o build/temp.linux-x86_64-3.10/home/Python-3.10.6/Modules/_sqlite/prepare_protocol.o build/temp.linux-x86_64-3.10/home/Python-3.10.6/Modules/_sqlite/row.o build/temp.linux-x86_64-3.10/home/Python-3.10.6/Modules/_sqlite/statement.o build/temp.linux-x86_64-3.10/home/Python-3.10.6/Modules/_sqlite/util.o -L/usr/lib/x86_64-linux-gnu -L/usr/local/lib -lsqlite3 -o build/lib.linux-x86_64-3.10/_sqlite3.cpython-310-x86_64-linux-gnu.so

The following modules found by detect_modules() in setup.py, have been
built by the Makefile instead, as configured by the Setup files:
_abc                  _hashlib              _socket
_ssl                  pwd                   time

running build_scripts
copying and adjusting /home/Python-3.10.6/Tools/scripts/pydoc3 -> build/scripts-3.10
copying and adjusting /home/Python-3.10.6/Tools/scripts/idle3 -> build/scripts-3.10
copying and adjusting /home/Python-3.10.6/Tools/scripts/2to3 -> build/scripts-3.10
changing mode of build/scripts-3.10/pydoc3 from 644 to 755
changing mode of build/scripts-3.10/idle3 from 644 to 755
changing mode of build/scripts-3.10/2to3 from 644 to 755
renaming build/scripts-3.10/pydoc3 to build/scripts-3.10/pydoc3.10
renaming build/scripts-3.10/idle3 to build/scripts-3.10/idle3.10
renaming build/scripts-3.10/2to3 to build/scripts-3.10/2to3-3.10
gcc -pthread     -Xlinker -export-dynamic -o Programs/_testembed Programs/_testembed.o libpython3.10.a -lcrypt -lpthread -ldl  -lutil -lm -L/usr/local/openssl/lib64 -l:libssl.a -Wl,--exclude-libs,libssl.a -l:libcrypto.a -Wl,--exclude-libs,libcrypto.a  -L/usr/local/openssl/lib64 -l:libcrypto.a -Wl,--exclude-libs,libcrypto.a   -lm
sed -e "s,@EXENAME@,/usr/local/python-3.10.6-with-openssl-3.0.5/bin/python3.10," < ./Misc/python-config.in >python-config.py
LC_ALL=C sed -e 's,\$(\([A-Za-z0-9_]*\)),\$\{\1\},g' < Misc/python-config.sh >python-config
```
make successfully!

At last, install python.
```shell
make install

--------------- log --------------
...
rm -f /usr/local/python-3.10.6-with-openssl-3.0.5/bin/2to3
(cd /usr/local/python-3.10.6-with-openssl-3.0.5/bin; ln -s 2to3-3.10 2to3)
if test "x" != "x" ; then \
	rm -f /usr/local/python-3.10.6-with-openssl-3.0.5/bin/python3-32; \
	(cd /usr/local/python-3.10.6-with-openssl-3.0.5/bin; ln -s python3.10-32 python3-32) \
fi
if test "x" != "x" ; then \
	rm -f /usr/local/python-3.10.6-with-openssl-3.0.5/bin/python3-intel64; \
	(cd /usr/local/python-3.10.6-with-openssl-3.0.5/bin; ln -s python3.10-intel64 python3-intel64) \
fi
rm -f /usr/local/python-3.10.6-with-openssl-3.0.5/share/man/man1/python3.1
(cd /usr/local/python-3.10.6-with-openssl-3.0.5/share/man/man1; ln -s python3.10.1 python3.1)
if test "xupgrade" != "xno"  ; then \
	case upgrade in \
		upgrade) ensurepip="--upgrade" ;; \
		install|*) ensurepip="" ;; \
	esac; \
	 ./python -E -m ensurepip \
		$ensurepip --root=/ ; \
fi
Looking in links: /tmp/tmpetpcoecz
Processing /tmp/tmpetpcoecz/setuptools-63.2.0-py3-none-any.whl
Processing /tmp/tmpetpcoecz/pip-22.2.1-py3-none-any.whl
Installing collected packages: setuptools, pip
  WARNING: The scripts pip3 and pip3.10 are installed in '/usr/local/python-3.10.6-with-openssl-3.0.5/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pip-22.2.1 setuptools-63.2.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
```
Though the log is not perfect, but looks like has no impact on the result.

```shell
$ ls /usr/local/python-3.10.6-with-openssl-3.0.5/
bin  include  lib  share
```

Validate python

```shell
root@41892223057e:~/Python-3.10.6# /usr/local/python-3.10.6-with-openssl-3.0.5/bin/python3 -v
/usr/local/python-3.10.6-with-openssl-3.0.5/bin/python3: error while loading shared libraries: libpython3.10.so.1.0: cannot open shared object file: No such file or directory
```

export LD_LIBRARY_PATH

```shell
export LD_LIBRARY_PATH=/usr/local/python-3.10.6-with-openssl-3.0.5/lib/
```

```python
$ # /usr/local/python-3.10.6-with-openssl-3.0.5/bin/python3
Python 3.10.6 (main, Oct  7 2022, 23:04:55) [GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import ssl
>>> ssl.OPENSSL_VERSION
'OpenSSL 3.0.5 5 Jul 2022'
>>>
```
Python compiled successfully!!

-----------------------

## <a name='issues'>Issues encountered</a>

##### <span style="color:Red">Configured incorrectly in Module/Setup</span>

```shell
# Socket module helper for SSL support; you must comment out the other
# socket line above, and edit the OPENSSL variable:
OPENSSL=/usr/local/openssl-3.0.5
_ssl _ssl.c \
     -I$(OPENSSL)/include -L$(OPENSSL)/lib64 \
     -lssl -lcrypto
_hashlib _hashopenssl.c \
     -I$(OPENSSL)/include -L$(OPENSSL)/lib64 \
     -lcrypto

# To statically link OpenSSL:
_ssl _ssl.c \
     -I$(OPENSSL)/include -L$(OPENSSL)/lib64 \
     -l:libssl.a -Wl,--exclude-libs,libssl.a \
     -l:libcrypto.a -Wl,--exclude-libs,libcrypto.a
_hashlib _hashopenssl.c \
     -I$(OPENSSL)/include -L$(OPENSSL)/lib64 \
     -l:libcrypto.a -Wl,--exclude-libs,libcrypto.a
```

I guess the upper part ( line4 to line9 ) is for dynamic compiling, and lower part is for static compiling.
So if comment out them simultaneously, will cause an error ( shown as below ) when compile python.

```shell
Modules/_ssl.o: In function `PyInit__ssl':
/home/Python-3.10.6/./Modules/_ssl.c:6242: multiple definition of `PyInit__ssl'
Modules/_ssl.o:/home/Python-3.10.6/./Modules/_ssl.c:6242: first defined here
Modules/_hashopenssl.o:/home/Python-3.10.6/./Modules/_hashopenssl.c:1822: multiple definition of `HMACtype_spec'
Modules/_hashopenssl.o:/home/Python-3.10.6/./Modules/_hashopenssl.c:1822: first defined here
Modules/_hashopenssl.o: In function `PyInit__hashlib':
/home/Python-3.10.6/./Modules/_hashopenssl.c:2286: multiple definition of `PyInit__hashlib'
Modules/_hashopenssl.o:/home/Python-3.10.6/./Modules/_hashopenssl.c:2286: first defined here
collect2: error: ld returned 1 exit status
ln: failed to access 'libpython3.10.so.1.0': No such file or directory
Makefile:656: recipe for target 'libpython3.10.so' failed
make: *** [libpython3.10.so] Error 1
```

PS:

If you encounter other issues, it's very likely due to you not install the packages ( listed in step 1 ) properly.

e.g. below issue is because `gcc` is not installed. 

````shell
$ ./config --prefix=/usr/local/openssl --openssldir=/usr/local/openssl

Failure!  build file wasn't produced.
Please read INSTALL.md and associated NOTES-* files.  You may also have to
look over your available compiler tool chain or change your configuration.

ERROR!
No C compiler found, please specify one with the environment variable CC,
or configure with an explicit configuration target.
````

For there are so many similar issues during my compilation, i not paste them here one by one, i resolved them by installing step 1 packages. 

## <a name='references'>References</a>

- <a href='https://techglimpse.com/install-python-openssl-support-tutorial/'>https://techglimpse.com/install-python-openssl-support-tutorial/</a>
- <a href='http://blog.lujianxin.com/x/art/s538bgptom7o'>http://blog.lujianxin.com/x/art/s538bgptom7o</a>


<hr>
<hr>

Compile on Mac.


## <a name="prepare_mac">Preparation</a>
##### Check your architecture of your Mac

Here is mine.

```shell
$ set | grep "MACHTYPE"
MACHTYPE=x86_64-apple-darwin20
```

##### Download openssl tar ball. 

It's same as <a href='#download_openssl'>above process</a>

##### Configure

```shell
$ ./configure --prefix=/Users/vzhong/Documents/compile-target/python-3.10.6 --with-openssl=/Users/vzhong/Documents/compile-target/openssl-3.0.5 --enable-optimizations --enable-shared

Configuring OpenSSL version 3.0.5 for target darwin64-x86_64-cc
Using os-specific seed configuration
Created configdata.pm
Running configdata.pm
Created Makefile.in
Created Makefile

**********************************************************************
***                                                                ***
***   OpenSSL has been successfully configured                     ***
***                                                                ***
***   If you encounter a problem while building, please open an    ***
***   issue on GitHub <https://github.com/openssl/openssl/issues>  ***
***   and include the output from the following command:           ***
***                                                                ***
***       perl configdata.pm --dump                                ***
***                                                                ***
***   (If you are new to OpenSSL, you might want to consult the    ***
***   'Troubleshooting' section in the INSTALL.md file first)      ***
***                                                                ***
**********************************************************************
```


##### Make & Install

```shell
$ make

---------- log ------------
...
The necessary bits to build these optional modules were not found:
ossaudiodev           spwd
To find the necessary bits, look in setup.py in detect_modules() for the module's name.


The following modules found by detect_modules() in setup.py, have been
built by the Makefile instead, as configured by the Setup files:
_abc                  pwd                   time

running build_scripts
copying and adjusting /Users/vzhong/Documents/mac-compile/Python-3.10.6/Tools/scripts/pydoc3 -> build/scripts-3.10
copying and adjusting /Users/vzhong/Documents/mac-compile/Python-3.10.6/Tools/scripts/idle3 -> build/scripts-3.10
copying and adjusting /Users/vzhong/Documents/mac-compile/Python-3.10.6/Tools/scripts/2to3 -> build/scripts-3.10
changing mode of build/scripts-3.10/pydoc3 from 644 to 755
changing mode of build/scripts-3.10/idle3 from 644 to 755
changing mode of build/scripts-3.10/2to3 from 644 to 755
renaming build/scripts-3.10/pydoc3 to build/scripts-3.10/pydoc3.10
renaming build/scripts-3.10/idle3 to build/scripts-3.10/idle3.10
renaming build/scripts-3.10/2to3 to build/scripts-3.10/2to3-3.10
gcc -c -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall    -fno-semantic-interposition -std=c99 -Wextra -Wno-unused-result -Wno-unused-parameter -Wno-missing-field-initializers -Wstrict-prototypes -Werror=implicit-function-declaration -fvisibility=hidden -fprofile-instr-use=code.profclangd -I./Include/internal  -I. -I./Include    -DPy_BUILD_CORE -o Programs/_testembed.o ./Programs/_testembed.c
clang: warning: argument unused during compilation: '-fno-semantic-interposition' [-Wunused-command-line-argument]
gcc   -fno-semantic-interposition  -Wl,-stack_size,1000000  -framework CoreFoundation -o Programs/_testembed Programs/_testembed.o libpython3.10.a -lintl -ldl   -framework CoreFoundation

```

```shell
$ make install

---------- log ------------
...
if test "xupgrade" != "xno"  ; then \
		case upgrade in \
			upgrade) ensurepip="--upgrade" ;; \
			install|*) ensurepip="" ;; \
		esac; \
		DYLD_LIBRARY_PATH=/Users/vzhong/Documents/mac-compile/Python-3.10.6 ./python.exe -E -m ensurepip \
			$ensurepip --root=/ ; \
	fi
Looking in links: /var/folders/x3/qp_d__rn70x5hml9z4ygtvv80000gr/T/tmpp4r0himi
Requirement already satisfied: setuptools in /Users/vzhong/Documents/compile-target/python-3.10.6/lib/python3.10/site-packages (63.2.0)
Requirement already satisfied: pip in /Users/vzhong/Documents/compile-target/python-3.10.6/lib/python3.10/site-packages (22.2.1)
```

Validate if the compilation is successful.

```python
$ ~/Documents/compile-target/python-3.10.6/bin/python3
Python 3.10.6 (main, Oct 10 2022, 15:34:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import ssl
>>> ssl.OPENSSL_VERSION
'OpenSSL 3.0.5 5 Jul 2022'
```

Ok, succeed!


## <a name='mac_references'>References</a>

- <a href='https://www.youtube.com/watch?v=15zJ0acT4NQ'>[ Youtube ] Compile Python 3.7 on macOS from scratch</a>

The end, hope it helps!

<hr>
<hr>
<hr>



## On CentOS 5.8

#### Setup a docker container

There is no centos5.8 in centos dockerhub official repos, i find out one provided by a dockerhub user.

```shell
docker pull muratayusuke/centos5.8

docker run -it muratayusuke/centos5.8:latest /bin/sh


$ 
head -n 1 /etc/issue

CentOS release 5.8 (Final)
```

As we can see, this version has a very low version glibc. ↓

```shell
getconf GNU_LIBC_VERSION

glibc 2.5
```

you will encounter this error when `yum update`

```shell
sh-3.2# yum update
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
YumRepo Error: All mirror URLs are not using ftp, http[s] or file.
 Eg. Invalid release/repo/arch combination/
removing mirrorlist with no valid mirrors: /var/cache/yum/base/mirrorlist.txt
Error: Cannot find a valid baseurl for repo: base
```

solution ↓

```shell
cp /etc/yum/pluginconf.d/fastestmirror.conf /etc/yum/pluginconf.d/fastestmirror.conf.bak
sed -i "s|enabled=1|enabled=0|g" /etc/yum/pluginconf.d/fastestmirror.conf


cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak

echo '' > /etc/yum.repos.d/CentOS-Base.repo

vi /etc/yum.repos.d/CentOS-Base.repo

# CentOS-Base.repo
#
# The mirror system uses the connecting IP address of the client and the
# update status of each mirror to pick mirrors that are updated to and
# geographically close to the client.  You should use this for CentOS updates
# unless you are manually picking other mirrors.
#
# If the mirrorlist= does not work for you, as a fall back you can try the
# remarked out baseurl= line instead.
#
#

[base]
name=CentOS-$releasever - Base
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os&infra=$infra
#baseurl=http://mirror.centos.org/centos/$releasever/os/$basearch/
baseurl=https://vault.centos.org/6.10/os/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6

#released updates
[updates]
name=CentOS-$releasever - Updates
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=updates&infra=$infra
#baseurl=http://mirror.centos.org/centos/$releasever/updates/$basearch/
baseurl=https://vault.centos.org/6.10/updates/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6

#additional packages that may be useful
[extras]
name=CentOS-$releasever - Extras
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras&infra=$infra
#baseurl=http://mirror.centos.org/centos/$releasever/extras/$basearch/
baseurl=https://vault.centos.org/6.10/extras/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6
```

Then may encounter another error.

```shell
sh-3.2# yum update

Traceback (most recent call last):
  File "/usr/bin/yum", line 29, in ?
    yummain.user_main(sys.argv[1:], exit_code=True)
  File "/usr/share/yum-cli/yummain.py", line 309, in user_main
    errcode = main(args)
  File "/usr/share/yum-cli/yummain.py", line 178, in main
    result, resultmsgs = base.doCommands()
  File "/usr/share/yum-cli/cli.py", line 345, in doCommands
    self._getTs(needTsRemove)
  File "/usr/lib/python2.4/site-packages/yum/depsolve.py", line 101, in _getTs
    self._getTsInfo(remove_only)
  File "/usr/lib/python2.4/site-packages/yum/depsolve.py", line 112, in _getTsInfo
    pkgSack = self.pkgSack
  File "/usr/lib/python2.4/site-packages/yum/__init__.py", line 662, in <lambda>
    pkgSack = property(fget=lambda self: self._getSacks(),
  File "/usr/lib/python2.4/site-packages/yum/__init__.py", line 502, in _getSacks
    self.repos.populateSack(which=repos)
  File "/usr/lib/python2.4/site-packages/yum/repos.py", line 260, in populateSack
    sack.populate(repo, mdtype, callback, cacheonly)
  File "/usr/lib/python2.4/site-packages/yum/yumRepo.py", line 168, in populate
    if self._check_db_version(repo, mydbtype):
  File "/usr/lib/python2.4/site-packages/yum/yumRepo.py", line 226, in _check_db_version
    return repo._check_db_version(mdtype)
  File "/usr/lib/python2.4/site-packages/yum/yumRepo.py", line 1226, in _check_db_version
    repoXML = self.repoXML
  File "/usr/lib/python2.4/site-packages/yum/yumRepo.py", line 1399, in <lambda>
    repoXML = property(fget=lambda self: self._getRepoXML(),
  File "/usr/lib/python2.4/site-packages/yum/yumRepo.py", line 1391, in _getRepoXML
    self._loadRepoXML(text=self)
  File "/usr/lib/python2.4/site-packages/yum/yumRepo.py", line 1381, in _loadRepoXML
    return self._groupLoadRepoXML(text, ["primary"])
  File "/usr/lib/python2.4/site-packages/yum/yumRepo.py", line 1365, in _groupLoadRepoXML
    if self._commonLoadRepoXML(text):
  File "/usr/lib/python2.4/site-packages/yum/yumRepo.py", line 1201, in _commonLoadRepoXML
    result = self._getFileRepoXML(local, text)
  File "/usr/lib/python2.4/site-packages/yum/yumRepo.py", line 974, in _getFileRepoXML
    cache=self.http_caching == 'all')
  File "/usr/lib/python2.4/site-packages/yum/yumRepo.py", line 811, in _getFile
    http_headers=headers,
  File "/usr/lib/python2.4/site-packages/urlgrabber/mirror.py", line 412, in urlgrab
    return self._mirror_try(func, url, kw)
  File "/usr/lib/python2.4/site-packages/urlgrabber/mirror.py", line 398, in _mirror_try
    return func_ref( *(fullurl,), **kwargs )
  File "/usr/lib/python2.4/site-packages/urlgrabber/grabber.py", line 936, in urlgrab
    return self._retry(opts, retryfunc, url, filename)
  File "/usr/lib/python2.4/site-packages/urlgrabber/grabber.py", line 854, in _retry
    r = apply(func, (opts,) + args, {})
  File "/usr/lib/python2.4/site-packages/urlgrabber/grabber.py", line 922, in retryfunc
    fo = URLGrabberFileObject(url, filename, opts)
  File "/usr/lib/python2.4/site-packages/urlgrabber/grabber.py", line 1010, in __init__
    self._do_open()
  File "/usr/lib/python2.4/site-packages/urlgrabber/grabber.py", line 1093, in _do_open
    fo, hdr = self._make_request(req, opener)
  File "/usr/lib/python2.4/site-packages/urlgrabber/grabber.py", line 1202, in _make_request
    fo = opener.open(req)
  File "/usr/lib64/python2.4/urllib2.py", line 364, in open
    response = meth(req, response)
  File "/usr/lib64/python2.4/urllib2.py", line 471, in http_response
    response = self.parent.error(
  File "/usr/lib64/python2.4/urllib2.py", line 396, in error
    result = self._call_chain(*args)
  File "/usr/lib64/python2.4/urllib2.py", line 337, in _call_chain
    result = func(*args)
  File "/usr/lib64/python2.4/urllib2.py", line 565, in http_error_302
    return self.parent.open(new)
  File "/usr/lib64/python2.4/urllib2.py", line 358, in open
    response = self._open(req, data)
  File "/usr/lib64/python2.4/urllib2.py", line 376, in _open
    '_open', req)
  File "/usr/lib64/python2.4/urllib2.py", line 337, in _call_chain
    result = func(*args)
  File "/usr/lib64/python2.4/site-packages/M2Crypto/m2urllib2.py", line 82, in https_open
    h.request(req.get_method(), req.get_selector(), req.data, headers)
  File "/usr/lib64/python2.4/httplib.py", line 810, in request
    self._send_request(method, url, body, headers)
  File "/usr/lib64/python2.4/httplib.py", line 833, in _send_request
    self.endheaders()
  File "/usr/lib64/python2.4/httplib.py", line 804, in endheaders
    self._send_output()
  File "/usr/lib64/python2.4/httplib.py", line 685, in _send_output
    self.send(msg)
  File "/usr/lib64/python2.4/httplib.py", line 652, in send
    self.connect()
  File "/usr/lib64/python2.4/site-packages/M2Crypto/httpslib.py", line 55, in connect
    sock.connect((self.host, self.port))
  File "/usr/lib64/python2.4/site-packages/M2Crypto/SSL/Connection.py", line 174, in connect
    ret = self.connect_ssl()
  File "/usr/lib64/python2.4/site-packages/M2Crypto/SSL/Connection.py", line 167, in connect_ssl
    return m2.ssl_connect(self.ssl, self._timeout)
M2Crypto.SSL.SSLError: unknown protocol
```
solution (refer to <a href="https://www.modb.pro/db/451337">here</a> ) ↓

```shell
rm -rf etc/yum.repos.d/*
touch etc/yum.repos.d/Bento-Vault.repo




vi /etc/yum.repos.d/Bento-Vault.repo

#BENTO-BEGIN

[C5.8-base]

name=CentOS-5.8 - Base

#baseurl=http://vault.centos.org/5.8/os/$basearch/

baseurl=http://archive.kernel.org/centos-vault/5.8/os/$basearch/

gpgcheck=1

gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-5

enabled=1

[C5.8-updates]

name=CentOS-5.8 - Updates

#baseurl=http://vault.centos.org/5.8/updates/$basearch/

baseurl=http://archive.kernel.org/centos-vault/5.8/updates/$basearch/

gpgcheck=1

gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-5

enabled=1

[C5.8-extras]

name=CentOS-5.8 - Extras

#baseurl=http://vault.centos.org/5.8/extras/$basearch/

baseurl=http://archive.kernel.org/centos-vault/5.8/extras/$basearch/

gpgcheck=1

gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-5

enabled=1

[C5.8-centosplus]

name=CentOS-5.8 - Plus

#baseurl=http://vault.centos.org/5.8/centosplus/$basearch/

baseurl=http://archive.kernel.org/centos-vault/5.8/centosplus/$basearch/

gpgcheck=1

gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-5

enabled=1

#BENTO-END
```

`yum update` succeed ↓

```shell
# yum update
Failed to set locale, defaulting to C
C5.8-base                                                                                                       | 1.1 kB     00:00     
C5.8-base/primary                                                                                               | 1.2 MB     00:00     
C5.8-base                                                                                                                    3591/3591
C5.8-centosplus                                                                                                 | 1.9 kB     00:00     
C5.8-centosplus/primary_db                                                                                      |  89 kB     00:00     
C5.8-extras                                                                                                     | 2.1 kB     00:00     
C5.8-extras/primary_db                                                                                          | 207 kB     00:00     
C5.8-updates                                                                                                    | 1.9 kB     00:00     
C5.8-updates/primary_db                                                                                         | 1.0 MB     00:00     
Setting up Update Process
No Packages marked for Update
```

Let's install vim

```shell
yum install vim-enhanced -y
```

#### Compile openssl

```shell
Supposed to be wget, but actually wget not works
wget https://github.com/openssl/openssl/archive/refs/tags/openssl-3.0.5.tar.gz


--2022-10-20 09:51:09--  https://github.com/openssl/openssl/archive/refs/tags/openssl-3.0.5.tar.gz
Resolving github.com... 192.30.255.113
Connecting to github.com|192.30.255.113|:443... connected.
OpenSSL: error:1407742E:SSL routines:SSL23_GET_SERVER_HELLO:tlsv1 alert protocol version
Unable to establish SSL connection.


-------(′ꈍᴗꈍ‵)-------------
Above error i have tried varity of approches, but not solve it,
so my workaround is to download this tarball on my host, then docker cp to this container.
```

Uncompress openssl tarball.

```shell
$ 
tar -xvzf openssl-3.0.5.tar.gz

tar: bzip2: Cannot exec: No such file or directory
tar: Error is not recoverable: exiting now
tar: Child returned status 2
tar: Error exit delayed from previous errors
```

Solution ↓
```shell
$ 
yum install bzip2

$
tar -xvzf openssl-3.0.5.tar.gz
```

configure openssl

```
$
cd openssl-openssl-3.0.5

$
./config --prefix=/usr/local/openssl-3.0.5 --openssldir=/usr/local/openssl-3.0.5
Perl v5.10.0 required--this is only v5.8.8, stopped at /openssl-openssl-3.0.5/Configure line 12.
BEGIN failed--compilation aborted at /openssl-openssl-3.0.5/Configure line 12.
```

Solution  ↓

Upgrade perl version, basically, i referred to <a href="https://blog.csdn.net/GUI1259802368/article/details/84935290">here</a>, but a bit different.

I downloaded `perl-5.26.3.tar.gz`(http://www.cpan.org/authors/id/S/SH/SHAY/perl-5.26.3.tar.gz)

```shell
cd perl-5.26.3

./Configure -des -Dprefix=/usr/local/perl -Dusethreads -Uversiononly -Dcc=gcc
```
Above `Configure` cmd is sightly different from what article demos.

```shell
make
make install
```

After installed, then

```shell
mv /usr/bin/perl /usr/bin/perl.bak
ln -s /usr/local/perl/bin/perl /usr/bin/perl

# perl -v
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "C.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").

This is perl 5, version 26, subversion 3 (v5.26.3) built for x86_64-linux-thread-multi

Copyright 1987-2018, Larry Wall

Perl may be copied only under the terms of either the Artistic License or the
GNU General Public License, which may be found in the Perl 5 source kit.

Complete documentation for Perl, including FAQ lists, should be found on
this system using "man perl" or "perldoc perl".  If you have access to the
Internet, point your browser at http://www.perl.org/, the Perl Home Page.
```

##### upgrade wget

I gave up it after a painful struggle.


##### Upgrade ld
If you encounter below error. Try to upgrade `ld`
```shell
/usr/bin/ld: cannot find -l:libssl.a
collect2: ld returned 1 exit status
ln: accessing `libpython3.10.so.1.0': No such file or directory
```

#### upgrade gcc
gcc version on this machine is very low.

```shell
sh-3.2# gcc -v
Using built-in specs.
Target: x86_64-redhat-linux6E
Configured with: ../configure --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=http://bugzilla.redhat.com/bugzilla --enable-bootstrap --enable-shared --enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --disable-gnu-unique-object --with-as=/usr/libexec/binutils220/as --enable-languages=c,c++,fortran --disable-libgcj --with-mpfr=/builddir/build/BUILD/gcc-4.4.7-20120601/obj-x86_64-redhat-linux6E/mpfr-install/ --with-ppl=/builddir/build/BUILD/gcc-4.4.7-20120601/obj-x86_64-redhat-linux6E/ppl-install --with-cloog=/builddir/build/BUILD/gcc-4.4.7-20120601/obj-x86_64-redhat-linux6E/cloog-install --with-tune=generic --with-arch_32=i586 --build=x86_64-redhat-linux6E
Thread model: posix
gcc version 4.4.7 20120313 (Red Hat 4.4.7-1) (GCC) 


Error:

configure: error: in `/tmp/gcc-12.2.0/host-x86_64-pc-linux-gnu/gcc':
configure: error: C++ preprocessor "/lib/cpp" fails sanity check
See `config.log' for more details
make[2]: *** [configure-stage1-gcc] Error 1
make[2]: Leaving directory `/tmp/gcc-12.2.0'
make[1]: *** [stage1-bubble] Error 2
make[1]: Leaving directory `/tmp/gcc-12.2.0'
make: *** [all] Error 2

solution:↓
download gcc-8.2.0, https://ftp.gnu.org/gnu/gcc/gcc-8.2.0/gcc-8.2.0.tar.gz
then recompile
be patient, it will take a long long time..

reconfigure: got error

/tmp/downs/gcc-8.2.0/host-x86_64-pc-linux-gnu/gcc/cc1: error while loading shared libraries: libmpc.so.3: cannot open shared object file: No such file or directory
make[3]: *** [s-selftest-c] Error 1
rm gcc.pod
make[3]: Leaving directory `/tmp/downs/gcc-8.2.0/host-x86_64-pc-linux-gnu/gcc'
make[2]: *** [all-stage1-gcc] Error 2
make[2]: Leaving directory `/tmp/downs/gcc-8.2.0'
make[1]: *** [stage1-bubble] Error 2
make[1]: Leaving directory `/tmp/downs/gcc-8.2.0'
make: *** [all] Error 2

-- refer to: https://blog.csdn.net/CouragelDesire/article/details/116462607

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/mpc/lib:/usr/local/gmp/lib:/usr/local/mpfr/lib
then reconfigure
```

As prerequisite, we must install below 3 libs before install gcc.

- Install `gmp`

I downloaded `gmp-6.1.2.tar.xz` (https://gmplib.org/download/gmp/gmp-6.1.2.tar.xz)

```shell
yum install xz
```

```shell
unxz gmp-6.1.2.tar.xz
tar -xf gmp-6.1.2.tar

cd gmp-6.1.2

./configure --prefix=/usr/local/gmp
make
make install
```

- Install `mpfr` (https://www.mpfr.org/mpfr-current/mpfr-4.1.1.tar.gz)

```shell
tar -xvzf mpfr-4.1.1.tar.gz
cd mpfr-4.1.1

./configure --prefix=/usr/local/mpfr --with-gmp-include=/usr/local/gmp/include/ --with-gmp-lib=/usr/local/gmp/lib/

make
make install
```

- Install `mpc` (https://ftp.gnu.org/gnu/mpc/mpc-1.2.0.tar.gz, it's different from above article, i encounter a error in 1.0.3, as below shows)

```shell
cd mpc-1.0.3

./configure --prefix=/usr/local/mpc --with-gmp=/usr/local/gmp --with-mpfr=/usr/local/mpfr

make

mul.c:175: error: conflicting types for 'mpfr_fmma'
/usr/local/mpfr/include/mpfr.h:765: note: previous declaration of 'mpfr_fmma' was here
make[2]: *** [mul.lo] Error 1
make[2]: Leaving directory `/mpc-1.0.3/mpc-1.0.3/src'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/mpc-1.0.3/mpc-1.0.3'
make: *** [all] Error

----------------

Then i change install version as `1.2.0` (https://ftp.gnu.org/gnu/mpc/mpc-1.2.0.tar.gz), works

tar -xvzf mpc-1.2.0.tar.gz
cd mpc-1.2.0

./configure --prefix=/usr/local/mpc --with-gmp=/usr/local/gmp --with-mpfr=/usr/local/mpfr

make
make install
```


- upgrade gcc

I choose the latest version of gcc (https://ftp.gnu.org/gnu/gcc/gcc-12.2.0/gcc-12.2.0.tar.gz)
but failed, so i change version as `gcc-8.2.0`
```shell
./configure --prefix=/usr/local/gcc --enable-threads=posix --disable-checking --disable-multilib --enable-languages=c,c++ --with-gmp=/usr/local/gmp --with-mpfr=/usr/local/mpfr --with-mpc=/usr/local/mpc
make
make install
```


https://www.quora.com/How-can-I-upgrade-GCC-on-CentOS-7
+ https://blog.csdn.net/springlustre/article/details/101123238

```shell
checking for objdir... .libs
checking for the correct version of gmp.h... no
configure: error: Building GCC requires GMP 4.2+, MPFR 2.4.0+ and MPC 0.8.0+.
Try the --with-gmp, --with-mpfr and/or --with-mpc options to specify
their locations.  Source code for these libraries can be found at
their respective hosting sites as well as at
ftp://gcc.gnu.org/pub/gcc/infrastructure/.  See also
http://gcc.gnu.org/install/prerequisites.html for additional info.  If
you obtained GMP, MPFR and/or MPC from a vendor distribution package,
make sure that you have installed both the libraries and the header
files.  They may be located in separate packages.
```

```shell

  198  pwd
  199  ls
  200  cd ..
  201  ls
  202  cd gmp-6.1.0
  203  ./configure
  204  ./configure --prefix=/usr/local/gmp
  205  make
  206  make install
  207  cd ../mpfr-3.1.4
  208  ./configure --prefix=/usr/local/mpfr
  209  make
  210  make install
  211  ls
  212  pwd
  213  cd ..
  214  ls
  215  cd mpc-1.0.3
  216  pwd
  217  pwd
  218  ./configure --prefix=/usr/local/mpc --with-gmp=/usr/local/gmp --with-mpfr=/usr/local/mpfr
  219  make
  220  make install
  221  history
```

make

```shell
-----log------

store_16_.o cas_16_.o exch_16_.o fadd_16_.o fsub_16_.o fand_16_.o fior_16_.o fxor_16_.o fnand_16_.o tas_16_.o
libtool: link: ranlib .libs/libatomic.a
libtool: link: ( cd ".libs" && rm -f "libatomic.la" && ln -s "../libatomic.la" "libatomic.la" )
true  DO=all multi-do # make
make[4]: Leaving directory `/gcc-8.2.0/x86_64-pc-linux-gnu/libatomic'
make[3]: Leaving directory `/gcc-8.2.0/x86_64-pc-linux-gnu/libatomic'
make[2]: Leaving directory `/gcc-8.2.0/x86_64-pc-linux-gnu/libatomic'
make[1]: Leaving directory `/gcc-8.2.0'
```

gcc, install
```shell
make install

----------------------------------------------------------------------
Libraries have been installed in:
   /usr/local/gcc/lib/../lib64

If you ever happen to want to link against installed libraries
in a given directory, LIBDIR, you must either use libtool, and
specify the full pathname of the library, or use the `-LLIBDIR'
flag during linking and do at least one of the following:
   - add LIBDIR to the `LD_LIBRARY_PATH' environment variable
     during execution
   - add LIBDIR to the `LD_RUN_PATH' environment variable
     during linking
   - use the `-Wl,-rpath -Wl,LIBDIR' linker flag
   - have your system administrator add LIBDIR to `/etc/ld.so.conf'

See any operating system documentation about shared libraries for
more information, such as the ld(1) and ld.so(8) manual pages.
----------------------------------------------------------------------
make[4]: Nothing to be done for `install-data-am'.
make[4]: Leaving directory `/gcc-8.2.0/x86_64-pc-linux-gnu/libatomic'
make[3]: Leaving directory `/gcc-8.2.0/x86_64-pc-linux-gnu/libatomic'
make[2]: Leaving directory `/gcc-8.2.0/x86_64-pc-linux-gnu/libatomic'
make[1]: Leaving directory `/gcc-8.2.0'
```

```shell
# /usr/local/gcc/bin/gcc -v

Using built-in specs.
COLLECT_GCC=/usr/local/gcc/bin/gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc/libexec/gcc/x86_64-pc-linux-gnu/8.2.0/lto-wrapper
Target: x86_64-pc-linux-gnu
Configured with: 
./configure --prefix=/usr/local/gcc --enable-threads=posix --disable-checking --disable-multilib --enable-languages=c,c++ --with-gmp=/usr/local/gmp --with-mpfr=/usr/local/mpfr --with-mpc=/usr/local/mpc
Thread model: posix
gcc version 8.2.0 (GCC)
```

```shell
# ln -s /usr/local/gcc/bin/gcc /usr/bin/gcc

# ls -lha /usr/bin/gcc
lrwxrwxrwx 1 root root 22 Oct 27 21:53 /usr/bin/gcc -> /usr/local/gcc/bin/gcc

# gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc/libexec/gcc/x86_64-pc-linux-gnu/8.2.0/lto-wrapper
Target: x86_64-pc-linux-gnu
Configured with: ./configure --prefix=/usr/local/gcc --enable-threads=posix --disable-checking --disable-multilib --enable-languages=c,c++ --with-gmp=/usr/local/gmp --with-mpfr=/usr/local/mpfr --with-mpc=/usr/local/mpc
Thread model: posix
gcc version 8.2.0 (GCC)
```

compile python

```shell
# ./configure --prefix=/usr/local/python-3.10.6-with-openssl-3.0.5 --with-openssl=/usr/local/openssl-3.0.5/ --enable-shared

checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-pc-linux-gnu
checking for python3.10... no
checking for python3... no
checking for python... python
checking for --enable-universalsdk... no
checking for --with-universal-archs... no
checking MACHDEP... "linux"
checking for gcc... gcc
checking whether the C compiler works... no
configure: error: in `/Python-3.10.6':
configure: error: C compiler cannot create executables
See `config.log' for more details



solution: ↓

```

##### Upgrade ld


```shell
sh-3.2# export LD_LIBRARY_PATH=/usr/local/python-3.10.6-with-openssl-3.0.5/lib
sh-3.2# /usr/local/python-3.10.6-with-openssl-3.0.5/bin/python3
Python 3.10.6 (main, Oct 28 2022, 03:26:08) [GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import _ctypes
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named '_ctypes'
```

```shell
compile libffi erro

configure:3823: gcc -V >&5
gcc: error: unrecognized command line option '-V'
gcc: fatal error: no input files
compilation terminated.
configure:3834: $? = 1
configure:3823: gcc -qversion >&5
gcc: error: unrecognized command line option '-qversion'; did you mean '--version'?
gcc: fatal error: no input files
compilation terminated.
configure:3834: $? = 1
configure:3854: checking whether the C compiler works
configure:3876: gcc    conftest.c  >&5
/usr/local/gcc/libexec/gcc/x86_64-pc-linux-gnu/8.2.0/cc1: error while loading shared libraries: libmpc.so.3: cannot open shared object file: No such file or directory

$
export LD_LIBRARY_PATH=/usr/local/mpc/lib/:/usr/local/mpfr/lib/:/usr/local/gmp/lib/



export LD_LIBRARY_PATH=/usr/local/mpc/lib/:/usr/local/mpfr/lib/:/usr/local/gmp/lib/:/usr/local/libffi/3_2_1/lib/
then recompile python

got error

/Python-3.10.6/Modules/_ctypes/_ctypes.c:107:10: fatal error: ffi.h: No such file or directory
 #include <ffi.h>
          ^~~~~~~
compilation terminated.

The necessary bits to build these optional modules were not found:
_bz2                  _curses               _curses_panel      
_dbm                  _gdbm                 _lzma              
_sqlite3              _tkinter              _uuid              
readline                                                       
To find the necessary bits, look in setup.py in detect_modules() for the module's name.


The following modules found by detect_modules() in setup.py, have been
built by the Makefile instead, as configured by the Setup files:
_abc                  _hashlib              _socket            
_ssl                  pwd                   time               


Failed to build these modules:
_ctypes      

shit, i need to compile all the lib not found. then id do below

## sqlite same as in ubuntu
## yum install -y xz-devel
## yum -y install tcl-devel tk-devel


The necessary bits to build these optional modules were not found:
_bz2                  _curses               _curses_panel      
_dbm                  _gdbm                 _tkinter           
_uuid                 readline                                 
To find the necessary bits, look in setup.py in detect_modules() for the module's name.


The following modules found by detect_modules() in setup.py, have been
built by the Makefile instead, as configured by the Setup files:
_abc                  _hashlib              _socket            
_ssl                  pwd                   time               


Failed to build these modules:
_ctypes  



## yum install gdbm-devel tk-devel readline-devel bzip2-devel ncurses-devel zlib-devel

/Python-3.10.6/Modules/_ctypes/_ctypes.c:107:10: fatal error: ffi.h: No such file or directory
 #include <ffi.h>
          ^~~~~~~
compilation terminated.
*** WARNING: renaming "_sqlite3" since importing it failed: /Python-3.10.6/build/lib.linux-x86_64-3.10/_sqlite3.cpython-310-x86_64-linux-gnu.so: undefined symbol: sqlite3_backup_remaining

The necessary bits to build these optional modules were not found:
_uuid                                                          
To find the necessary bits, look in setup.py in detect_modules() for the module's name.


The following modules found by detect_modules() in setup.py, have been
built by the Makefile instead, as configured by the Setup files:
_abc                  _hashlib              _socket            
_ssl                  pwd                   time               


Failed to build these modules:
_ctypes                                                        


Following modules built successfully but were removed because they could not be imported:
_sqlite3                                                       

```


```shell
CORE_MODULE
/Python-3.10.6/Modules/_ctypes/_ctypes.c:107:10: fatal error: ffi.h: No such file or directory
 #include <ffi.h>
          ^~~~~~~
compilation terminated.
```



```shell
/python-3.10.6-with-openssl-3.0.5/lib -L/usr/local/lib -ldl -o build/lib.linux-x86_64-3.10/_ctypes.cpython-310-x86_64-linux-gnu.so
*** WARNING: renaming "_sqlite3" since importing it failed: /Python-3.10.6/build/lib.linux-x86_64-3.10/_sqlite3.cpython-310-x86_64-linux-gnu.so: undefined symbol: sqlite3_backup_remaining
*** WARNING: renaming "_ctypes" since importing it failed: /Python-3.10.6/build/lib.linux-x86_64-3.10/_ctypes.cpython-310-x86_64-linux-gnu.so: undefined symbol: ffi_prep_cif

The necessary bits to build these optional modules were not found:
_uuid                                                          
To find the necessary bits, look in setup.py in detect_modules() for the module's name.


The following modules found by detect_modules() in setup.py, have been
built by the Makefile instead, as configured by the Setup files:
_abc                  _hashlib              _socket            
_ssl                  pwd                   time               


Following modules built successfully but were removed because they could not be imported:
_ctypes               _sqlite3  


solution ↓

```

##### install libffi-devel

##### install pkg-config
https://blog.csdn.net/u012897401/article/details/88994933

but i use pkg-config-0.29.2
wget https://pkg-config.freedesktop.org/releases/pkg-config-0.29.2.tar.gz


```shell
sh-3.2# ./autogen.sh 
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "C.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
Can't exec "aclocal": No such file or directory at /usr/bin/autoreconf line 174.
Use of uninitialized value in pattern match (m//) at /usr/bin/autoreconf line 174.
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: aclocal -I m4 --output=aclocal.m4t
Can't exec "aclocal": No such file or directory at /usr/share/autoconf/Autom4te/FileUtils.pm line 288.
autoreconf: failed to run aclocal: No such file or directory
sh-3.2# 

solution:
sh-3.2# yum install automake libtool



```

_ctypes solution: https://bugs.python.org/issue14527


```shell
sh-3.2# /usr/local/python-3.10.6-with-openssl-3.0.5/bin/python3
/usr/local/python-3.10.6-with-openssl-3.0.5/bin/python3: error while loading shared libraries: libpython3.10.so.1.0: cannot open shared object file: No such file or directory
```

Questions:
- $(PWD) is '/' when root runs


references:
https://www.cnblogs.com/god-of-death/p/12767113.html


OPENSSL_ARTIFACTORY = http://10.79.128.59:8000/openssl-3.0.5.tar.gz
PYTHON_ARTIFACTORY = http://10.79.128.59:8000/python-3.10.6-with-openssl-3.0.5.tar.gz


#### x
Create docker image from iso image
https://wiki.metacentrum.cz/wiki/Creating_Docker_Image_from_.iso_File

### Install MacOS in virtualBox
https://appuals.com/this-copy-of-the-install-os-x-el-capitan-application-cant-be-verified/
https://www.youtube.com/watch?v=-TGtkAGgzBg


https://bugs.python.org/issue14527

黑苹果 https://zhuanlan.zhihu.com/p/20248815

## On Macos Capitan

```shell
cat /System/Library/CoreServices/SystemVersion.plist

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>ProductBuildVersion</key>
        <string>15F34</string>
        <key>ProductCopyright</key>
        <string>1983-2016 Apple Inc.</string>
        <key>ProductName</key>
        <string>Mac OS X</string>
        <key>ProductUserVisibleVersion</key>
        <string>10.11.5</string>
        <key>ProductVersion</key>
        <string>10.11.5</string>
    </dict>
</plist>
```

VMware Remote Console download:
https://pagalba.balt.net/index.php/Download_Vmware_Remote_Console_(VMRC)_HTML5


Install Capitan on Fusion:
http://cn.tipsandtricks.tech/%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8VMware-Fusion%E5%AE%89%E8%A3%85Mac-OS-X


```shell
crypto/bn/rsaz-avx512.s:859:2: error: instruction requires: AVX-512 ISA AVX-512 VL ISA
 vmovdqu64 %ymm3,96(%rdi)
 ^
crypto/bn/rsaz-avx512.s:860:2: error: instruction requires: AVX-512 ISA AVX-512 VL ISA
 vmovdqu64 %ymm4,128(%rdi)
 ^
make[1]: *** [crypto/bn/libcrypto-lib-rsaz-avx512.o] Error 1
make: *** [build_sw] Error 2




mentioned at page https://github.com/openssl/openssl/issues/15937


solution ↓
change version to 3.0.7

make

---------log----------
rm -f "util/shlib_wrap.sh"
perl "-I." -Mconfigdata "util/dofile.pl" \
	    "-oMakefile" util/shlib_wrap.sh.in > "util/shlib_wrap.sh"
chmod a+x util/shlib_wrap.sh
rm -f "util/wrap.pl"
perl "-I." -Mconfigdata "util/dofile.pl" \
	    "-oMakefile" util/wrap.pl.in > "util/wrap.pl"
chmod a+x util/wrap.pl




make

----------log---------------

gcc     -Wl,-stack_size,1000000  -framework CoreFoundation -o python.exe Programs/python.o -L. -lpython3.10 -ldl   -framework CoreFoundation -L/tmp/openssl-3.0.7/lib -l:libssl.a -Wl,--exclude-libs,libssl.a -l:libcrypto.a -Wl,--exclude-libs,libcrypto.a  -L/tmp/openssl-3.0.7/lib -l:libcrypto.a -Wl,--exclude-libs,libcrypto.a
ld: library not found for -l:libssl.a
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [python.exe] Error 1


solution:

./configure --prefix=/usr/local/python-3.10.6-with-openssl-3.0.5 --with-openssl=/usr/local/openssl-3.0.5/ --enable-shared CPPFLAGS="-I/usr/local/openssl-3.0.5/include" LDFLAGS="-L/usr/local/openssl-3.0.5/lib"
```


```shell
The necessary bits to build these optional modules were not found:
_tkinter
To find the necessary bits, look in configure.ac and config.log.

Checked 109 modules (30 built-in, 76 shared, 2 n/a on macosx-10.11-x86_64, 0 disabled, 1 missing, 0 failed on import)
```

```shell
Error: python-tk@3.10: Failed to download resource "gdbm"

solution：
https://www.jianshu.com/p/f028e184a25f
```

```shell
ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.

$ pip install --upgrade pip --user
```

```shell
$ pip install PyInstaller==4.10
WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.
Please see https://github.com/pypa/pip/issues/5599 for advice on fixing the underlying issue.
To avoid this problem you can invoke Python with '-m pip' instead of running pip directly.
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.
Defaulting to user installation because normal site-packages is not writeable
ERROR: Could not find a version that satisfies the requirement PyInstaller==4.10 (from versions: 2.0, 2.1, 3.0, 3.1, 3.1.1, 3.2, 3.2.1, 3.3, 3.3.1, 3.4, 3.5, 3.6, 4.0, 4.1)
ERROR: No matching distribution found for PyInstaller==4.10
```


```shell
$ ./configure --prefix=/tmp/compiled-Python-3.10.6/ --with-openssl=/tmp/openssl-3.0.7/ --enable-shared CPPFLAGS="-I/tmp/openssl-3.0.7/include" LDFLAGS="-L/tmp/openssl-3.0.7/lib"

The necessary bits to build these optional modules were not found:
ossaudiodev           spwd
To find the necessary bits, look in setup.py in detect_modules() for the module's name.


The following modules found by detect_modules() in setup.py, have been
built by the Makefile instead, as configured by the Setup files:
_abc                  pwd                   time

running build_scripts





```

```shell
  File "/private/tmp/osspi-cli/virtualenv/lib/python3.10/site-packages/PyInstaller/utils/osx.py", line 337, in remove_signature_from_binary
    raise SystemError(f"codesign command ({cmd_args}) failed with error code {p.returncode}!\noutput: {p.stdout}")
SystemError: codesign command (['codesign', '--remove', '--all-architectures', '/private/tmp/osspi-cli/build/osspi/osspi']) failed with error code 1!
output: /private/tmp/osspi-cli/build/osspi/osspi: invalid or unsupported format for signature

make: *** [all] Error 1


为什么不能用户brew安装的python ?
```

```shell
when copy compiled python from EI Capitan to my mac

$ build/python/bin/python3
dyld: Library not loaded: /tmp/compiled-Python-3.10.6/lib/libpython3.10.dylib
  Referenced from: /Users/vzhong/ttt/build/python/bin/python3
  Reason: image not found
Abort trap: 6
```


#### Compile on EI Capitan

```
    1  ping 10.110.124.158
    2  ping 10.110.124.158
    3  ls
    4  ls
    5  cd compile-python-openssl/
    6  l
    7  ls
    8  cd openssl-openssl-3.0.5/
    9  ls
   10  ./config --prefix=/usr/local/openssl-3.0.5 --openssldir=/usr/local/openssl-3.0.5
   11  make
   12  cd ..
   13  ls
   14  tar -xvzf openssl-3.0.7.tar.gz
   15  cd openssl-openssl-3.0.7/
   16  ls
   17  ./config --prefix=/usr/local/openssl-3.0.7 --openssldir=/usr/local/openssl-3.0.7
   18  make
   19  pwd
   20  ls
   21  ls /usr/local/
   22  make install
   23  mkdir /usr/local/openssl-3.0.7
   24  sudo mkdir /usr/local/openssl-3.0.7
   25  chmod 777 /usr/local/openssl-3.0.7
   26  sudo chmod 777 /usr/local/openssl-3.0.7
   27  make install
   28  pwd
   29  cd ..
   30  ls
   31  cd Python-3.10.6
   32  ls
   33  ls
   34  ls /usr/local/openssl-3.0.5
   35  ls /usr/local/
   36  ls /usr/local/openssl-3.0.7
   37  pwd
   38  ./configure --prefix=/usr/local/python-3.10.6-with-openssl-3.0.7 --with-openssl=/usr/local/openssl-3.0.7/ --enable-shared CPPFLAGS="-I/usr/local/openssl-3.0.7/include" LDFLAGS="-L/usr/local/openssl-3.0.7/lib"
   39  make
   40  history
   41  make install
   42  ls /usr/local/
   43  mkdir /usr/local/python-3.10.6-with-openssl-3.0.7
   44  sudo mkdir /usr/local/python-3.10.6-with-openssl-3.0.7
   45  sudo chmod 777 /usr/local/python-3.10.6-with-openssl-3.0.7
   46  make install
   47  history
```


[back](./)



Extra story:

```shell
vzhong-a01:test-capitan vzhong$ pip install PyInstaller==4.10
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.
Defaulting to user installation because normal site-packages is not writeable
ERROR: Could not find a version that satisfies the requirement PyInstaller==4.10 (from versions: 2.0, 2.1, 3.0, 3.1, 3.1.1, 3.2, 3.2.1, 3.3, 3.3.1, 3.4, 3.5, 3.6, 4.0, 4.1)
ERROR: No matching distribution found for PyInstaller==4.10


solution: ↓
$ pip3 install PyInstaller==4.10
```


./configure LDFLAGS="-L/usr/local/mpc/lib" --prefix=/usr/local/gcc --enable-threads=posix --disable-checking --disable-multilib --enable-languages=c,c++ --with-gmp=/usr/local/gmp --with-mpfr=/usr/local/mpfr --with-mpc=/usr/local/mpc
