# Puppet Manifest: Kill the process named "killmenow" using pkill

exec { 'killmenow':
  command     => '/usr/bin/pkill -TERM killmenow',
}
