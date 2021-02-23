#!/usr/bin/python3

import sys, getopt
import json

def AssemblingV2RayConfigObject(inbounds_port, socks_user, socks_pass):
    return json.dumps({
            "inbounds": [
                    {
                        "port": inbounds_port,
                        "listen": "0.0.0.0",
                        "tag": "socks-inbound",
                        "protocol": "socks",
                        "settings": {
                                "auth": "password",
                                "accounts": [
                                        {
                                            "user": socks_user,
                                            "pass": socks_pass
                                            }
                                    ],
                                "udp": False,
                                "ip": "127.0.0.1"
                            },
                        "sniffing": {
                            "enabled": True,
                            "destOverride": ["http", "tls"]
                            }
                        }
                ],
            "outbounds": [
                    {
                        "protocol": "freedom",
                        "settings": {},
                        "tag": "direct"
                        }
                ]
        }, indent=4)

if __name__ == "__main__":
    write_file_path = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hw:")
    except getopt.GetoptError:
        print("generate_v2ray_config_file.py -w <writefile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("generate_v2ray_config_file.py -w <writefile>")
            sys.exit()
        elif opt in ("-w"):
            write_file_path = arg
    if write_file_path == "":
        print("The following arguments are required: -w")
        sys.exit(2)
    # TODO: Obtains socks authenticate info
    v2ray_config_file_content = AssemblingV2RayConfigObject(1080, "user", "pass")
    with open(write_file_path, "w") as config_file:
        config_file.write(v2ray_config_file_content)
