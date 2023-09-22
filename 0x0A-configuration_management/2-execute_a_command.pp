# Puppet Manifest: Kill the process named "killmenow" using pkill

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/bin',
  refreshonly => true,
  subscribe   => File['/path/to/your/killmenow/script'],
  onlyif      => 'pgrep -f killmenow',
}
