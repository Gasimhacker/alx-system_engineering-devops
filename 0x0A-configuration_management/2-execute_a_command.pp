# Install flask
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
