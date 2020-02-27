# change values in the file /etc/default/nginx/

exec {'concurrence_conections'
  command => "sudo sed -i 's/5/1000' /etc/default/nginx",
  command => 'sudo service nginx restart',
  provider => shell
  }