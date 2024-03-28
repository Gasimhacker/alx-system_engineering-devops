#!/usr/bin/env bash
redirection_rule="\n\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}"
old_string="server_name _";
sed -i "/$old_string/a \ $redirection_rule" /etc/nginx/sites-available/default
