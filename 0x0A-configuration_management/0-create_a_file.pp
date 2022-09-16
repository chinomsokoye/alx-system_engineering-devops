# Create a file in /tmp with specifications below

file { '/tmp/school':
  ensure  =>  file,
  path    =>  '/tmp/school',
  mode    =>  '0744',
  owner   =>  'www-data',
  group   =>  'www-data',
  content =>  'I love Puppet'
}
