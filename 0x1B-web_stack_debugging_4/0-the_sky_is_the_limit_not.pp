#PP script to increase ULIMIT

#Increase ULIMIT then restart
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx; sudo service nginx restart',
  path    => '/usr/local/bin/:/bin/'
}
