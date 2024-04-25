sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo pip3 install https://github.com/shadowsocks/shadowsocks/archive/master.zip
sudo ssserver --version

filename = "/etc/shadowsocks.json"
sudo cat <<EOF > "$filename"
{
    "server":"0.0.0.0",
    "server_port":443,
    "local_port":1080,
    "password":"Beijing100",
    "timeout":300,
    "method":"aes-256-cfb"
}
EOF
sudo /usr/local/bin/ssserver -c /etc/shadowsocks.json -d start
