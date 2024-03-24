# Edit the ssh configuration
include stdlib

file_line { '/etc/ssh/ssh_config':
  ensure => present,
  line   => "	AuthenticatePassword no",
}
file_line { '/etc/ssh/ssh_config':
  ensure => present,
  line   => "	IdentityFile ~/.ssh/school",
}
