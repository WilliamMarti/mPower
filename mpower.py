def main(hostname, port, status):



  # display some lines


  print hostname
  print port
  print status


  username =  "vagrant";
  password =  "vagrant";


  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
  ssh.connect('127.0.0.1', username='vagrant',
    password='vagrant')


  stdin, stdout, stderr = ssh.exec_command(
    "uptime")

  stdin.flush()

  data = stdout.read().splitlines()
  for line in data:
    print line

  print "we got here"





if __name__ == "__main__":
  import sys
  import paramiko

  hostname = sys.argv[1]
  port = sys.argv[2]
  status = sys.argv[3]


  main(hostname, port, status)
