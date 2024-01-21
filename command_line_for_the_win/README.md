# SFTP

FTP, the File Transfer Protocol, was a popular, unencrypted method of transferring files between two remote systems. As of 2022, it has been deprecated by most modern software due to a lack of security, and can mostly only be used in legacy applications.

SFTP, which stands for Secure File Transfer Protocol, is a separate protocol packaged built into SSH that can implement FTP commands over a secure connection. Typically, it can act as a drop-in replacement in any contexts where an FTP server is still needed.

In almost all cases, SFTP is preferable to FTP because of its underlying security features and ability to piggy-back on an SSH connection. FTP is an insecure protocol that should only be used in limited cases or on networks you trust.

In order to push the screenshots to the sandbox using SFTP there are few steps to perform:
## Steps

- From your local machine establish an SFTP session by issuing the following command:
`$ sftp mohammed@your_server_ip_or_remote_hostname
- Navigate to the required directory: 
`$ cd /root/alx-system_engineering-devops/`

- Create a new directory using the command:
`$ mkdir command_line_for_the_win`
- To navigate inside your local machine to the place containing the screenshots use the command:
`$ lcd your_path`
- Push the files to the to the remote system using the command:
`$ put localFile`

Once you are done with these steps you can push the screenshots to github from your sandbox.
