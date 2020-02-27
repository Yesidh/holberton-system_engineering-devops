# change values in the file /etc/default/nginx/

exec {'concurrence_conections'
  command => "/usr/bin/sed -i 's/-n 15/-n 1000' /etc/default/nginx\
  service nginx restart"
  }