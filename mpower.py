import paramiko, sys

def turnOffPort(hostname,port):

  user = "vagrant"
  password =  "vagrant"
  tcpport = 22

  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(hostname,tcpport,user,password)

  port = '/dev/output' + port
  cmd = 'echo 0 > ' + port
  print cmd
  #using uptime for testing atm
  stdin, stdout, stderr = ssh.exec_command("uptime")
  #stdin, stdout, stderr = ssh.exec_command(cmd)
  
  print "Port " + port + " has been shutoff"

def turnOnPort(hostname,port):

  user = "vagrant"
  password =  "vagrant"
  tcpport = 22

  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(hostname,tcpport,user,password)

  port = '/dev/output' + port
  cmd = 'echo 1 > ' + port 

  #using uptime for testing atm
  stdin, stdout, stderr = ssh.exec_command("uptime")
  #stdin, stdout, stderr = ssh.exec_command(cmd)
  
  print "Port " + port + " has been turned up"
  
def main(hostname, port, status):

  #if we want to set to up
  if status == 'up':
    turnOnPort(hostname, port)
  else:
    turnOffPort(hostname, port)

if __name__ == "__main__":

  hostname = sys.argv[1]
  port = sys.argv[2]
  status = sys.argv[3]


  main(hostname, port, status)




