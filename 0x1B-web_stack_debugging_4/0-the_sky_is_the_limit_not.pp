# change values in the file /etc/default/nginx/

exec {'concurrence_conections'
  command  => "sudo sed -i \'s/15/1000/\' /etc/default/nginx && sudo service nginx restart",
  provider => shell,
}