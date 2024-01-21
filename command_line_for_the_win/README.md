In order to push the screenshots to the sandbox there are few steps to perform:
#Steps
1- From your local machine establish an SFTP session by issuing the following command:
`sftp mohammed@your_server_ip_or_remote_hostname
2- Navigate to the required directory: 
`cd /root/alx-system_engineering-devops/`

3- Create a new directory using the command:
`mkdir command_line_for_the_win`
4- To navigate inside your local machine to the place containing the screenshots use the command:
`lcd your_path`
5- Push the files to the to the remote system using the command:
`put localFile`

Once you are done with these steps you can push the screenshots to github from your sandbox.
