# Edit the ssh configuration
include stdlib

file_line { '/etc/ssh/ssh_config':
  ensure  => present,
  line    => "	AuthenticatePassword no",
  replace => true
}
file_line { '/etc/ssh/ssh_config':
  ensure  => present,
  line    => "	IdentityFile ~/.ssh/school",
  replace => true
}
