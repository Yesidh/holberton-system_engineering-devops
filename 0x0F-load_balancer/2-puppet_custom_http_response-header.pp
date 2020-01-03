#!usr/bin/env bash
# bash script that install nginx and configure http header

exec {'http header':
     command => "sudo apt-get -y update && sudo apt-get -y install nginx && sudo sed -i "21i add_header X-Served-By \$hostname;" /etc/nginx/nginx.conf && sudo service nginx restart",
     provider => shell,
}
