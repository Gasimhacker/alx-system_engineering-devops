# Edit the ssh configuration
include stdlib

file_line { 'Only key_pairs':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true
}
file_line { 'Change the location of the private_key':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '     IdentityFile ~/.ssh/school',
  replace => true
}
