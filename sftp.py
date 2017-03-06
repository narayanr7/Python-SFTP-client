import paramiko

localpath = ""
remotepath = ""
#-------------Commands-------------#
command = "mkdir lol"
#----------------------------------#
hostname = ""
username = ""
password = ""
port = 22
try:
    sshclient = paramiko.SSHClient()
    sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshclient.connect(hostname, username=username, password=password, timeout=5, allow_agent=False,look_for_keys=False)
    transport = paramiko.Transport((hostname, port))
    sftp = sshclient.open_sftp()
    sftp.put(localpath, remotepath)
    stdin, stdout, stderr = sshclient.exec_command(command)
    sshclient.close()
    sftp.close()
except Exception as e:
    print("Caught error: " + e)
print("Done transfering file!")
