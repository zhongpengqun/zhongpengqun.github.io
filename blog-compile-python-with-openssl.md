---
layout: default
title: Hello
description: ..
---
This blog is a tutorial of how to compile `python 3.10.6` with `openssl 3.0.5` module on `Ubuntu 18.04` and `mac os`.

↓ On `Ubuntu 18.04`

Steps:

- [Prepare ubuntu container](#prepare)
- [Compile openssl](#openssl)
- [Compile python](#python)

Further:
- [Issues encountered in the process](#issues)
- [References](#references)


↓ On `Mac OS`

Steps:

- [Prepare Mac OS](#prepare_mac)
- [Compile openssl](#openssl)
- [Compile python](#python)

Further:
- [References](#mac_references)

↓ On `Centos5.11`

Steps:
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



## CentOS 5.11

```shell
sh-3.2# head -n 1 /etc/issue
CentOS release 5.11 (Final)
```

```shell
sh-3.2# yum update
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
YumRepo Error: All mirror URLs are not using ftp, http[s] or file.
 Eg. Invalid release/repo/arch combination/
removing mirrorlist with no valid mirrors: /var/cache/yum/base/mirrorlist.txt
Error: Cannot find a valid baseurl for repo: base
```
```shell
sh-3.2# yum install vim-enhanced -y 
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
YumRepo Error: All mirror URLs are not using ftp, http[s] or file.
 Eg. Invalid release/repo/arch combination/
removing mirrorlist with no valid mirrors: /var/cache/yum/base/mirrorlist.txt
Error: Cannot find a valid baseurl for repo: base
sh-3.2# 
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
solution
https://www.modb.pro/db/451337

```shell
# yum update
C5.8-base                                                                                         | 1.1 kB     00:00     
C5.8-base/primary                                                                                 | 1.2 MB     00:00     
C5.8-base                                                                                                      3591/3591
C5.8-centosplus                                                                                   | 1.9 kB     00:00     
C5.8-centosplus/primary_db                                                                        |  89 kB     00:00     
C5.8-extras                                                                                       | 2.1 kB     00:00     
C5.8-extras/primary_db                                                                            | 207 kB     00:00     
C5.8-updates                                                                                      | 1.9 kB     00:00     
C5.8-updates/primary_db                                                                           | 1.0 MB     00:00     
Setting up Update Process
No Packages marked for Update
```

```shell
yum install vim-enhanced -y
```

```shell
sh-3.2# wget https://github.com/openssl/openssl/archive/refs/tags/openssl-3.0.5.tar.gz
--2022-10-20 09:51:09--  https://github.com/openssl/openssl/archive/refs/tags/openssl-3.0.5.tar.gz
Resolving github.com... 192.30.255.113
Connecting to github.com|192.30.255.113|:443... connected.
OpenSSL: error:1407742E:SSL routines:SSL23_GET_SERVER_HELLO:tlsv1 alert protocol version
Unable to establish SSL connection.
sh-3.2# 
```

```shell
sh-3.2# wget --secure-protocol=TLSv1 https://github.com/openssl/openssl/archive/refs/tags/openssl-3.0.5.tar.gz
--2022-10-20 09:54:03--  https://github.com/openssl/openssl/archive/refs/tags/openssl-3.0.5.tar.gz
Resolving github.com... 192.30.255.113
Connecting to github.com|192.30.255.113|:443... connected.
OpenSSL: error:1409442E:SSL routines:SSL3_READ_BYTES:tlsv1 alert protocol version
Unable to establish SSL connection.
```


```shell
# tar -xvjf openssl-3.0.5.tar.gz
tar: bzip2: Cannot exec: No such file or directory
tar: Error is not recoverable: exiting now
tar: Child returned status 2
tar: Error exit delayed from previous errors


# yum install bzip2

# tar -xvjf openssl-3.0.5.tar.gz

bzip2: Compressed file ends unexpectedly;
        perhaps it is corrupted?  *Possible* reason follows.
bzip2: Inappropriate ioctl for device
        Input file = (stdin), output file = (stdout)

It is possible that the compressed file(s) have become corrupted.
You can use the -tvv option to test integrity of such files.

You can use the `bzip2recover' program to attempt to recover
data from undamaged sections of corrupted files.

tar: Child returned status 2
tar: Error exit delayed from previous errors
```

```shell
# ./config --prefix=/usr/local/openssl-3.0.5 --openssldir=/usr/local/openssl-3.0.5
Perl v5.10.0 required--this is only v5.8.8, stopped at /openssl-openssl-3.0.5/Configure line 12.
BEGIN failed--compilation aborted at /openssl-openssl-3.0.5/Configure line 12.
```

```shell
sh-3.2# getconf GNU_LIBC_VERSION
```

Create docker image from iso image

https://wiki.metacentrum.cz/wiki/Creating_Docker_Image_from_.iso_File


### muratayusuke/centos5.8

```shell
docker pull muratayusuke/centos5.8

docker exec -it muratayusuke/centos5.8:latest /bin/sh



# head -n 1 /etc/issue
CentOS release 5.8 (Final)
```

```shell
wget https://github.com/openssl/openssl/archive/refs/tags/openssl-3.0.5.tar.gz

--2022-10-26 00:05:29--  https://github.com/openssl/openssl/archive/refs/tags/openssl-3.0.5.tar.gz
Resolving github.com... 192.30.255.112
Connecting to github.com|192.30.255.112|:443... connected.
OpenSSL: error:1407742E:SSL routines:SSL23_GET_SERVER_HELLO:tlsv1 alert protocol version
Unable to establish SSL connection.
sh-3.2# 
sh-3.2# 
sh-3.2# wget http://github.com/openssl/openssl/archive/refs/tags/openssl-3.0.5.tar.gz
--2022-10-26 00:06:06--  http://github.com/openssl/openssl/archive/refs/tags/openssl-3.0.5.tar.gz
Resolving github.com... 140.82.112.4
Connecting to github.com|140.82.112.4|:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://github.com/openssl/openssl/archive/refs/tags/openssl-3.0.5.tar.gz [following]
--2022-10-26 00:06:21--  https://github.com/openssl/openssl/archive/refs/tags/openssl-3.0.5.tar.gz
Connecting to github.com|140.82.112.4|:443... connected.
OpenSSL: error:1407742E:SSL routines:SSL23_GET_SERVER_HELLO:tlsv1 alert protocol version
Unable to establish SSL connection.
```

##### upgrade perl version

I referred to this article `https://blog.csdn.net/GUI1259802368/article/details/84935290`
but a bit different.

```shell
./Configure -des -Dprefix=/usr/local/perl -Dusethreads -Uversiononly -Dcc=gcc
```
after installed

```shell
ln -s /usr/local/perl/bin/perl /usr/bin/perl

# perl -v
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
	LANGUAGE = (unset),
	LC_ALL = (unset),
	LANG = "C.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").

This is perl 5, version 36, subversion 0 (v5.36.0) built for x86_64-linux-thread-multi

Copyright 1987-2022, Larry Wall

Perl may be copied only under the terms of either the Artistic License or the
GNU General Public License, which may be found in the Perl 5 source kit.

Complete documentation for Perl, including FAQ lists, should be found on
this system using "man perl" or "perldoc perl".  If you have access to the
Internet, point your browser at https://www.perl.org/, the Perl Home Page.
```

##### upgrade openssl
https://cloud.tencent.com/developer/article/1602967


##### upgrade wget

```shell
sh-3.2# ./configure --with-ssl=openssl

configure: error: The pkg-config script could not be found or is too old.  Make sure it
is in your PATH or set the PKG_CONFIG environment variable to the full
path to pkg-config.
```
solution ↓
```shell
yum install -y pkgconfig
```

yum install gnutls-devel

```shell
checking for GNUTLS... no
configure: error: Package requirements (gnutls) were not met:

No package 'gnutls' found

Consider adjusting the PKG_CONFIG_PATH environment variable if you
installed software in a non-standard prefix.

Alternatively, you may set the environment variables GNUTLS_CFLAGS
and GNUTLS_LIBS to avoid the need to call pkg-config.
See the pkg-config man page for more details.
```

configure succeed ?

```shell
sh-3.2# ./configure --with-openssl

config.status: creating gnulib_po/Makefile
configure: Summary of build options:

  Version:           1.21
  Host OS:           linux-gnu
  Install prefix:    /usr/local
  Compiler:          gcc
  CFlags:              -DHAVE_LIBGNUTLS -DNDEBUG -g -O2
  LDFlags:
  Libs:              -lgnutls   -lz
  SSL:               gnutls
  Zlib:              yes
  PSL:               no
  PCRE:              no
  Digest:            yes
  NTLM:              auto
  OPIE:              yes
  POSIX xattr:       yes
  Debugging:         yes
  Assertions:        no
  Valgrind:          Valgrind testing not enabled
  Metalink:          no
  Resolver:          libc, --bind-dns-address and --dns-servers not available
  GPGME:             no
  IRI:               no
  Fuzzing build:     no,
```

```shell
make


  CC       sys_socket.o
  CC       tempname.o
tempname.c: In function 'try_tempname_len':
tempname.c:288: error: 'for' loop initial declarations are only allowed in C99 mode
tempname.c:288: note: use option -std=c99 or -std=gnu99 to compile your code
make[3]: *** [tempname.o] Error 1
make[3]: Leaving directory `/wget-1.21/lib'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/wget-1.21/lib'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/wget-1.21'
make: *** [all] Error 2
```


How to set =99

[back](./)
