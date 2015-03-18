def main(hostname, port, status):



  # display some lines


  print hostname
  print port
  print status
  
  #ssh connection info
  #vagrant for dev environment
  user =  "vagrant";
  password =  "vagrant";
  tcpport = 22;

  #connect to a particular host
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
  ssh.connect(hostname,tcpport,user,password)


  #'ports' are really just files with a 0 or 1 value
  port = '/dev/output' + port

  #if we want to set to up
  if status == 'up':
    stdin, stdout, stderr = ssh.exec_command(
      "echo 1 >" + port)
  else:
    stdin, stdout, stderr = ssh.exec_command(
      "echo 0 >" + port)
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
