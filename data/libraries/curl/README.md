# curl 7.74.0#3

## vcpkg spec

```
curl[core,non-http,schannel,ssl,sspi,winssl]:x86-windows-static-v141 -> 7.74.0#3
curl[core,non-http,schannel,ssl,sspi,winssl]:x64-windows-static-v140 -> 7.74.0#3
curl[core,non-http,schannel,ssl,sspi,winssl]:x86-windows-static-v140 -> 7.74.0#3
curl[core,non-http,schannel,ssl,sspi,winssl]:x64-windows-static-v141 -> 7.74.0#3
curl[core,non-http,schannel,ssl,sspi,winssl]:x86-windows-static-v142 -> 7.74.0#3
curl[core,non-http,schannel,ssl,sspi,winssl]:x64-windows-static-v142 -> 7.74.0#3
```

## contents

```
-rwxrwxrwx 1 user user 7.7M Mar 24 09:33 x64-windows-static-v140.tar.gz
-rwxrwxrwx 1 user user 7.9M Mar 24 09:33 x64-windows-static-v141.tar.gz
-rwxrwxrwx 1 user user 6.4M Mar 24 09:33 x64-windows-static-v142.tar.gz
-rwxrwxrwx 1 user user 7.4M Mar 24 09:33 x86-windows-static-v140.tar.gz
-rwxrwxrwx 1 user user 7.5M Mar 24 09:34 x86-windows-static-v141.tar.gz
-rwxrwxrwx 1 user user 6.2M Mar 24 09:34 x86-windows-static-v142.tar.gz
x64-windows-static-v140.tar.gz
-rwxrwxrwx user/user  11255896 2021-03-24 08:20 ./x64-windows-static-v140/debug/lib/libcurl-d.lib
-rwxrwxrwx user/user   1489425 2021-03-24 09:33 ./x64-windows-static-v140/debug/lib/libcurl-d.lib.pat
-rwxrwxrwx user/user    363642 2021-03-24 08:18 ./x64-windows-static-v140/debug/lib/zlibd.lib
-rwxrwxrwx user/user    208358 2021-03-24 09:33 ./x64-windows-static-v140/debug/lib/zlibd.lib.pat
-rwxrwxrwx user/user  11971534 2021-03-24 08:21 ./x64-windows-static-v140/lib/libcurl.lib
-rwxrwxrwx user/user    961891 2021-03-24 09:33 ./x64-windows-static-v140/lib/libcurl.lib.pat
-rwxrwxrwx user/user    426326 2021-03-24 08:18 ./x64-windows-static-v140/lib/zlib.lib
-rwxrwxrwx user/user     93920 2021-03-24 09:33 ./x64-windows-static-v140/lib/zlib.lib.pat
x64-windows-static-v141.tar.gz
-rwxrwxrwx user/user  11257358 2021-03-24 08:24 ./x64-windows-static-v141/debug/lib/libcurl-d.lib
-rwxrwxrwx user/user   1489383 2021-03-24 09:33 ./x64-windows-static-v141/debug/lib/libcurl-d.lib.pat
-rwxrwxrwx user/user    365292 2021-03-24 08:21 ./x64-windows-static-v141/debug/lib/zlibd.lib
-rwxrwxrwx user/user    208382 2021-03-24 09:33 ./x64-windows-static-v141/debug/lib/zlibd.lib.pat
-rwxrwxrwx user/user  12147500 2021-03-24 08:24 ./x64-windows-static-v141/lib/libcurl.lib
-rwxrwxrwx user/user   1057802 2021-03-24 09:33 ./x64-windows-static-v141/lib/libcurl.lib.pat
-rwxrwxrwx user/user    427140 2021-03-24 08:21 ./x64-windows-static-v141/lib/zlib.lib
-rwxrwxrwx user/user     97051 2021-03-24 09:33 ./x64-windows-static-v141/lib/zlib.lib.pat
x64-windows-static-v142.tar.gz
-rwxrwxrwx user/user   8379914 2021-03-24 08:27 ./x64-windows-static-v142/debug/lib/libcurl-d.lib
-rwxrwxrwx user/user   1495061 2021-03-24 09:33 ./x64-windows-static-v142/debug/lib/libcurl-d.lib.pat
-rwxrwxrwx user/user    331192 2021-03-24 08:25 ./x64-windows-static-v142/debug/lib/zlibd.lib
-rwxrwxrwx user/user    208396 2021-03-24 09:33 ./x64-windows-static-v142/debug/lib/zlibd.lib.pat
-rwxrwxrwx user/user   9449228 2021-03-24 08:27 ./x64-windows-static-v142/lib/libcurl.lib
-rwxrwxrwx user/user   1073862 2021-03-24 09:33 ./x64-windows-static-v142/lib/libcurl.lib.pat
-rwxrwxrwx user/user    402952 2021-03-24 08:25 ./x64-windows-static-v142/lib/zlib.lib
-rwxrwxrwx user/user     98402 2021-03-24 09:33 ./x64-windows-static-v142/lib/zlib.lib.pat
x86-windows-static-v140.tar.gz
-rwxrwxrwx user/user  10768720 2021-03-24 08:30 ./x86-windows-static-v140/debug/lib/libcurl-d.lib
-rwxrwxrwx user/user   1239103 2021-03-24 09:33 ./x86-windows-static-v140/debug/lib/libcurl-d.lib.pat
-rwxrwxrwx user/user    323772 2021-03-24 08:28 ./x86-windows-static-v140/debug/lib/zlibd.lib
-rwxrwxrwx user/user    155147 2021-03-24 09:33 ./x86-windows-static-v140/debug/lib/zlibd.lib.pat
-rwxrwxrwx user/user  11554668 2021-03-24 08:30 ./x86-windows-static-v140/lib/libcurl.lib
-rwxrwxrwx user/user    899053 2021-03-24 09:33 ./x86-windows-static-v140/lib/libcurl.lib.pat
-rwxrwxrwx user/user    408716 2021-03-24 08:28 ./x86-windows-static-v140/lib/zlib.lib
-rwxrwxrwx user/user     86309 2021-03-24 09:33 ./x86-windows-static-v140/lib/zlib.lib.pat
x86-windows-static-v141.tar.gz
-rwxrwxrwx user/user  10766336 2021-03-24 08:34 ./x86-windows-static-v141/debug/lib/libcurl-d.lib
-rwxrwxrwx user/user   1238959 2021-03-24 09:33 ./x86-windows-static-v141/debug/lib/libcurl-d.lib.pat
-rwxrwxrwx user/user    324990 2021-03-24 08:31 ./x86-windows-static-v141/debug/lib/zlibd.lib
-rwxrwxrwx user/user    155171 2021-03-24 09:33 ./x86-windows-static-v141/debug/lib/zlibd.lib.pat
-rwxrwxrwx user/user  11732108 2021-03-24 08:35 ./x86-windows-static-v141/lib/libcurl.lib
-rwxrwxrwx user/user    989383 2021-03-24 09:34 ./x86-windows-static-v141/lib/libcurl.lib.pat
-rwxrwxrwx user/user    413614 2021-03-24 08:31 ./x86-windows-static-v141/lib/zlib.lib
-rwxrwxrwx user/user     91461 2021-03-24 09:34 ./x86-windows-static-v141/lib/zlib.lib.pat
x86-windows-static-v142.tar.gz
-rwxrwxrwx user/user   8066506 2021-03-24 08:38 ./x86-windows-static-v142/debug/lib/libcurl-d.lib
-rwxrwxrwx user/user   1240286 2021-03-24 09:34 ./x86-windows-static-v142/debug/lib/libcurl-d.lib.pat
-rwxrwxrwx user/user    291010 2021-03-24 08:35 ./x86-windows-static-v142/debug/lib/zlibd.lib
-rwxrwxrwx user/user    155145 2021-03-24 09:34 ./x86-windows-static-v142/debug/lib/zlibd.lib.pat
-rwxrwxrwx user/user   9208892 2021-03-24 08:38 ./x86-windows-static-v142/lib/libcurl.lib
-rwxrwxrwx user/user   1007122 2021-03-24 09:34 ./x86-windows-static-v142/lib/libcurl.lib.pat
-rwxrwxrwx user/user    386772 2021-03-24 08:35 ./x86-windows-static-v142/lib/zlib.lib
-rwxrwxrwx user/user     91046 2021-03-24 09:34 ./x86-windows-static-v142/lib/zlib.lib.pat
```

## .pat

```
x64-windows-static-v140/debug/lib/libcurl-d.lib: skipped 0, total 152
x64-windows-static-v140/debug/lib/zlibd.lib: skipped 0, total 20
x64-windows-static-v140/lib/libcurl.lib: skipped 36, total 1339
x64-windows-static-v140/lib/zlib.lib: skipped 1, total 154
x64-windows-static-v141/debug/lib/libcurl-d.lib: skipped 0, total 152
x64-windows-static-v141/debug/lib/zlibd.lib: skipped 0, total 20
x64-windows-static-v141/lib/libcurl.lib: skipped 35, total 1339
x64-windows-static-v141/lib/zlib.lib: skipped 1, total 154
x64-windows-static-v142/debug/lib/libcurl-d.lib: skipped 0, total 152
x64-windows-static-v142/debug/lib/zlibd.lib: skipped 0, total 20
x64-windows-static-v142/lib/libcurl.lib: skipped 35, total 1339
x64-windows-static-v142/lib/zlib.lib: skipped 1, total 154
x86-windows-static-v140/debug/lib/libcurl-d.lib: skipped 0, total 151
x86-windows-static-v140/debug/lib/zlibd.lib: skipped 0, total 20
x86-windows-static-v140/lib/libcurl.lib: skipped 21, total 1338
x86-windows-static-v140/lib/zlib.lib: skipped 1, total 154
x86-windows-static-v141/debug/lib/libcurl-d.lib: skipped 0, total 151
x86-windows-static-v141/debug/lib/zlibd.lib: skipped 0, total 20
x86-windows-static-v141/lib/libcurl.lib: skipped 21, total 1338
x86-windows-static-v141/lib/zlib.lib: skipped 1, total 154
x86-windows-static-v142/debug/lib/libcurl-d.lib: skipped 0, total 151
x86-windows-static-v142/debug/lib/zlibd.lib: skipped 0, total 20
x86-windows-static-v142/lib/libcurl.lib: skipped 21, total 1338
x86-windows-static-v142/lib/zlib.lib: skipped 1, total 154
```