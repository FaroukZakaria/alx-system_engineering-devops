# Increases the limit of Nginx traffic
# Increases the default's ULIMIT
exec { 'fix-for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin'],
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => ['/etc/init.d'],
}
