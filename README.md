# override-hostname

Override `gethostname()` using `LD_PRELOAD`.

```text
$ LD_PRELOAD=/usr/lib64/override-hostname/liboverride-hostname.so HOSTNAME=test123 hostname
test123
```
