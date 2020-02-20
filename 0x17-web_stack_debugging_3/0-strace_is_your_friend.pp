# makign debuggin

exec { 'debuggin':
     command => 'sed -i 's/phpp/php/' /var/www/html/wp-setting.php',
     path    => '/usr/bin:/usr/sbin:/bin'
}