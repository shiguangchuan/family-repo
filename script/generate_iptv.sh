#!/bin/bash

set -e
set -o pipefail
set -x

function transform() {
    curl --silent --fail --insecure "${1}" \
    | awk '{
        if ($0 ~ /^rtp:\/\//) {
            gsub(/:\/\//, "/");
#            gsub(/\:\/\//, "/");
            print "http://192.168.10.1:8686/"$0;
        } else {
            print $0;
        }
    }' > "${2}"
}

mkdir -p ./iptv

transform "https://raw.githubusercontent.com/qwerttvv/Beijing-IPTV/master/IPTV-Unicom-Multicast.m3u" "./iptv/bjuc_iptv.m3u"
transform "https://iptv.im2k.com/tjuc.m3u" "./iptv/tjuc_iptv.m3u"

ls -l ./iptv/

