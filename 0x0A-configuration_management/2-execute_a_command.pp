# Create a manifest that kills a process named killmenow
# using exec and pkill

exec { 'killmenow':
  command  =>  '/usr/bin/pkill killmenow',
  provider =>  'shell',
  returns  =>  [0, 1],
}
