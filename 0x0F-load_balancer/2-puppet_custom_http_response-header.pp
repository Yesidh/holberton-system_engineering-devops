# install nginx and configure http header

exec { 'install nginx':
  command => 'sudo apt-get -y update && sudo apt-get -y install nginx',
  provider => shell,
     }

exec { 'http header':
  command => 'sudo sed -i "21i add_header X-Served-By \$hostname;" /etc/nginx/nginx.conf'
  provider => shell,
}

exec { 'restar nginx':
  command => 'sudo service nginx restart',
  provider => shell,
}
