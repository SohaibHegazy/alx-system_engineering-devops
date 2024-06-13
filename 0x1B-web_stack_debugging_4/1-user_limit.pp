#configuration so that it is possible to login with the holberton user and open a file

#Fix soft files limit
exec {'set soft files limit'
  command => 'sed -i "/holberton soft/s/4/9000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

#Fix hard files limit
exec {'set soft files limit'
  command => 'sed -i "/holberton hard/s/5/10000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
