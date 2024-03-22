# Install flask
file { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
}
file { 'werkzeug':
  ensure   => '2.1.0',
  provider => pip3,
}
