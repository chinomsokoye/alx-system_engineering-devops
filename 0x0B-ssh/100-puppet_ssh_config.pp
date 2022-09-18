# Set up a client SSH configuration file

include stdlib
file_line { 'Declare identity file':
  path    =>  '/etc/ssh/ssh_config',
  line    =>  '		IdentityFile ~/.ssh/school',
  replace =>  true,
}

file_line { 'Turn off passwd auth':
  path    =>  '/etc/ssh/ssh_config',
  line    =>  '		PasswordAuthentication no',
  replace =>  true,
}
