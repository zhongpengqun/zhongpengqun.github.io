- 为什么我在oxxpi 上 apply了 oxxpi-splunk.yml, 但是却看不到 fluentd 的 daemonset ？

```
$ cat oxxpi-splunk.yml
apiVersion: logs.vdp.vmware.com/v1beta1
kind: FluentdConfig
metadata:
  name: fluentd-config
spec:
  fluentconf: |
    <match **>
      @type splunk_hec
      hec_host xxxe.com
      hec_port 8088
      hec_token exxx-fdsaf-adgdas-dddddx
      insecure_ssl true
    </match>
```

```
$ kubectl get daemonset
No resources found in vela-build-audit-core namespace.
```