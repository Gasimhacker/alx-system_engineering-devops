#!/usr/bin/env bash
# Configure haproxy to work as a load balancer for two servers
sudo apt-get install --no-install-recommends software-properties-common
sudo add-apt-repository -y ppa:vbernat/haproxy-2.8
sudo apt-get -y install haproxy=2.8.\*

backend="
backend web-backend
   balance roundrobin
   server 480531-web-01 100.24.240.126:80 check
   server 480531-web-02 54.157.134.215:80 check"
frontend="
frontend http
   bind *:80
   mode http

   default_backend web-backend"
sudo echo "ENABLED=1" >> /etc/default/haproxy
sudo echo "$frontend" >> /etc/haproxy/haproxy.cfg
sudo echo "$backend" >> /etc/haproxy/haproxy.cfg
sudo service haproxy restart
