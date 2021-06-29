# flare_common_libs.sig

```
$ ../venv/Scripts/python create_sig.py -d -e VS -s flare_common_libs.sig -n "FLARE Common Libraries 32/64 bit" -lr \\\$LN -lr label -li \\\$failure --tarballs-root data/ -- flare_common_libs
INFO:__main__:creating output directory flare_common_libs
INFO:__main__:collecting tarball paths
DEBUG:__main__: [-] skipping data/VS10\VS10.tar.gz
DEBUG:__main__: [-] skipping data/VS11\VS11.tar.gz
DEBUG:__main__: [-] skipping data/VS12\VS12.tar.gz
DEBUG:__main__: [-] skipping data/VS2015\compiler\14.0.tar.gz
DEBUG:__main__: [-] skipping data/VS2015\ucrt\10.0.10240.0.tar.gz
DEBUG:__main__: [-] skipping data/VS2017\compiler\14.16.27023.tar.gz
DEBUG:__main__: [-] skipping data/VS2017\ucrt\10.0.16299.0.tar.gz
DEBUG:__main__: [-] skipping data/VS2017\ucrt\10.0.17134.0.tar.gz
DEBUG:__main__: [-] skipping data/VS2017\ucrt\10.0.17763.0.tar.gz
DEBUG:__main__: [-] skipping data/VS2019\compiler\14.28.29910.tar.gz
DEBUG:__main__: [-] skipping data/VS2019\ucrt\10.0.18362.0.tar.gz
DEBUG:__main__: [-] skipping data/VS2019\ucrt\10.0.19041.0.tar.gz
DEBUG:__main__: [-] skipping data/VS6\VS6.tar.gz
DEBUG:__main__: [-] skipping data/VS8\VS8.tar.gz
DEBUG:__main__: [-] skipping data/VS9\VS9.tar.gz
DEBUG:__main__:extracting from data/libraries\cryptopp\x64-windows-static-v140.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-debug-lib-cryptopp-static.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-debug-lib-libcurl-d.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-debug-lib-zlibd.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-lib-cryptopp-static.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-lib-libcurl.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-lib-zlib.lib.pat
DEBUG:__main__:extracting from data/libraries\cryptopp\x64-windows-static-v141.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-debug-lib-cryptopp-static.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-lib-cryptopp-static.lib.pat
DEBUG:__main__:extracting from data/libraries\cryptopp\x64-windows-static-v142.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-debug-lib-cryptopp-static.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-lib-cryptopp-static.lib.pat
DEBUG:__main__:extracting from data/libraries\cryptopp\x86-windows-static-v140.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-debug-lib-cryptopp-static.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-lib-cryptopp-static.lib.pat
DEBUG:__main__:extracting from data/libraries\cryptopp\x86-windows-static-v141.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-debug-lib-cryptopp-static.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-lib-cryptopp-static.lib.pat
DEBUG:__main__:extracting from data/libraries\cryptopp\x86-windows-static-v142.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-debug-lib-cryptopp-static.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-lib-cryptopp-static.lib.pat
DEBUG:__main__:extracting from data/libraries\curl\x64-windows-static-v140.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-debug-lib-libcurl-d.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-debug-lib-zlibd.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-lib-libcurl.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-lib-zlib.lib.pat
DEBUG:__main__:extracting from data/libraries\curl\x64-windows-static-v141.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-debug-lib-libcurl-d.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-debug-lib-zlibd.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-lib-libcurl.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-lib-zlib.lib.pat
DEBUG:__main__:extracting from data/libraries\curl\x64-windows-static-v142.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-debug-lib-libcurl-d.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-debug-lib-zlibd.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-lib-libcurl.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-lib-zlib.lib.pat
DEBUG:__main__:extracting from data/libraries\curl\x86-windows-static-v140.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-debug-lib-libcurl-d.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-debug-lib-zlibd.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-lib-libcurl.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-lib-zlib.lib.pat
DEBUG:__main__:extracting from data/libraries\curl\x86-windows-static-v141.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-debug-lib-libcurl-d.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-debug-lib-zlibd.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-lib-libcurl.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-lib-zlib.lib.pat
DEBUG:__main__:extracting from data/libraries\curl\x86-windows-static-v142.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-debug-lib-libcurl-d.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-debug-lib-zlibd.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-lib-libcurl.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-lib-zlib.lib.pat
DEBUG:__main__:extracting from data/libraries\detours\x64-windows-static-v140.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-debug-lib-detours.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-lib-detours.lib.pat
DEBUG:__main__:extracting from data/libraries\detours\x64-windows-static-v141.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-debug-lib-detours.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-lib-detours.lib.pat
DEBUG:__main__:extracting from data/libraries\detours\x64-windows-static-v142.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-debug-lib-detours.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-lib-detours.lib.pat
DEBUG:__main__:extracting from data/libraries\detours\x86-windows-static-v140.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-debug-lib-detours.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-lib-detours.lib.pat
DEBUG:__main__:extracting from data/libraries\detours\x86-windows-static-v141.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-debug-lib-detours.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-lib-detours.lib.pat
DEBUG:__main__:extracting from data/libraries\detours\x86-windows-static-v142.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-debug-lib-detours.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-lib-detours.lib.pat
DEBUG:__main__:extracting from data/libraries\mbedtls\x64-windows-static-v140.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-debug-lib-mbedcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-debug-lib-mbedtls.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-debug-lib-mbedx509.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-lib-mbedcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-lib-mbedtls.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-lib-mbedx509.lib.pat
DEBUG:__main__:extracting from data/libraries\mbedtls\x64-windows-static-v141.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-debug-lib-mbedcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-debug-lib-mbedtls.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-debug-lib-mbedx509.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-lib-mbedcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-lib-mbedtls.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-lib-mbedx509.lib.pat
DEBUG:__main__:extracting from data/libraries\mbedtls\x64-windows-static-v142.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-debug-lib-mbedcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-debug-lib-mbedtls.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-debug-lib-mbedx509.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-lib-mbedcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-lib-mbedtls.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-lib-mbedx509.lib.pat
DEBUG:__main__:extracting from data/libraries\mbedtls\x86-windows-static-v140.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-debug-lib-mbedcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-debug-lib-mbedtls.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-debug-lib-mbedx509.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-lib-mbedcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-lib-mbedtls.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-lib-mbedx509.lib.pat
DEBUG:__main__:extracting from data/libraries\mbedtls\x86-windows-static-v141.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-debug-lib-mbedcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-debug-lib-mbedtls.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-debug-lib-mbedx509.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-lib-mbedcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-lib-mbedtls.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-lib-mbedx509.lib.pat
DEBUG:__main__:extracting from data/libraries\mbedtls\x86-windows-static-v142.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-debug-lib-mbedcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-debug-lib-mbedtls.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-debug-lib-mbedx509.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-lib-mbedcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-lib-mbedtls.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-lib-mbedx509.lib.pat
DEBUG:__main__:extracting from data/libraries\openssl\x64-windows-static-v140.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-debug-lib-libcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-debug-lib-libssl.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-lib-libcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-lib-libssl.lib.pat
DEBUG:__main__:extracting from data/libraries\openssl\x64-windows-static-v141.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-debug-lib-libcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-debug-lib-libssl.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-lib-libcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-lib-libssl.lib.pat
DEBUG:__main__:extracting from data/libraries\openssl\x64-windows-static-v142.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-debug-lib-libcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-debug-lib-libssl.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-lib-libcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-lib-libssl.lib.pat
DEBUG:__main__:extracting from data/libraries\openssl\x86-windows-static-v140.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-debug-lib-libcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-debug-lib-libssl.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-lib-libcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-lib-libssl.lib.pat
DEBUG:__main__:extracting from data/libraries\openssl\x86-windows-static-v141.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-debug-lib-libcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-debug-lib-libssl.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-lib-libcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-lib-libssl.lib.pat
DEBUG:__main__:extracting from data/libraries\openssl\x86-windows-static-v142.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-debug-lib-libcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-debug-lib-libssl.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-lib-libcrypto.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-lib-libssl.lib.pat
DEBUG:__main__:extracting from data/libraries\zlib\x64-windows-static-v140.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-debug-lib-zlibd.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v140-lib-zlib.lib.pat
DEBUG:__main__:extracting from data/libraries\zlib\x64-windows-static-v141.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-debug-lib-zlibd.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v141-lib-zlib.lib.pat
DEBUG:__main__:extracting from data/libraries\zlib\x64-windows-static-v142.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-debug-lib-zlibd.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x64-windows-static-v142-lib-zlib.lib.pat
DEBUG:__main__:extracting from data/libraries\zlib\x86-windows-static-v140.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-debug-lib-zlibd.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v140-lib-zlib.lib.pat
DEBUG:__main__:extracting from data/libraries\zlib\x86-windows-static-v141.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-debug-lib-zlibd.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v141-lib-zlib.lib.pat
DEBUG:__main__:extracting from data/libraries\zlib\x86-windows-static-v142.tar.gz
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-debug-lib-zlibd.lib.pat
DEBUG:__main__: writing flare_common_libs\.-x86-windows-static-v142-lib-zlib.lib.pat
INFO:__main__:creating sig file flare_common_libs.sig
DEBUG:__main__:running sigmake_patched.exe -v -v -n"FLARE Common Libraries 32/64 bit" -lr\$LN -lrlabel -li\$failure flare_common_libs\*.pat flare_common_libs\flare_common_libs.sig
DEBUG:__main__:running sigmake_patched.exe -v -v -n"FLARE Common Libraries 32/64 bit" -lr\$LN -lrlabel -li\$failure flare_common_libs\*.pat flare_common_libs\flare_common_libs.sig
INFO:__main__:zipping sig file flare_common_libs\flare_common_libs.sig
INFO:__main__:saving unzipped file as flare_common_libs\flare_common_libs.sig.bu
DEBUG:__main__:running zipsig.exe flare_common_libs\flare_common_libs.sig
```

```
$ tar czvf logs.tar.gz run1.log run2.log flare_common_libs.exc
run1.log
run2.log
flare_common_libs.exc
```
