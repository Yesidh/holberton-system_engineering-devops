# changing values hard and soft in the file limits.conf

exex {'soft_hard_feature':
  command => "/bin/sed -i 's/holberton hard nofile 5/holberton hard nofile 50' /etc/security/limits.conf";
  command => "/bin/sed -i 's/holberton soft nofile 4/holberton soft nofile 40' /etc/security/limint.conf";
}