include sshkeys_core

ssh_config { 'default_ssh_config':
  host           => '*',
  identityfile   => '~/.ssh/school',
  passwordauthentication => 'no',
}
