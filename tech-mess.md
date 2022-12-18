---
layout: default
title: Hello
description: Introduction about this site and me.
---

```shell
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.6' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.15' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.25' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.26' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.27' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.7' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.17' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.9' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.14' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.10' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.6' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.15' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.25' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.26' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.27' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.7' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.17' not found (required by /build/mts/release/sb-60321806/osspi-cli/build/python/lib/libpython3.10.so.1.0)
2022-10-19 00:58:27 gobuilds.Compile : build/python/bin/python3: /lib64/libc.so.6: version `GLIBC_2.9' not found

i met this error, root cause is i compiled python on a linux machine with high version glibc, but when i copy the compiled python to a lower glic version machine, it raised above error.
```

- [back](./)







