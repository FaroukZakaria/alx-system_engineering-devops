# Puppet Manifest: Kill the process named "killmenow" using pkill

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/bin',
  refreshonly => true,
  onlyif      => 'pgrep -f killmenow',
}
