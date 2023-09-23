file { '/home/ubuntu/.ssh/config':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "IdentityFile ~/.ssh/school\nPasswordAuthentication no\n",
  require => File['~/.ssh/school'],
}
