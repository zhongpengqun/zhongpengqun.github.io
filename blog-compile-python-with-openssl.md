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



[back](./)
