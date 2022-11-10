# Fixes a file
exec {'sets file limit for nginx':
  command =>  'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
  path    =>  '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
