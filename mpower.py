import paramiko, sys

#test if IP address is valid
def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


#Function to turn off Ports
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
  
  stdin, stdout, stderr = ssh.exec_command(cmd)
  
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

  stdin, stdout, stderr = ssh.exec_command(cmd)
  
  print "Port " + port + " has been turned up"
  
def main(hostname, port, status):

  #if we want to set to up
  if status == 'up':
    turnOnPort(hostname, port)
  elif status == 'down':
    turnOffPort(hostname, port)
  else:
    print "Acceptable arguments are either 'up or 'down'"
    sys.exit(0)


if __name__ == "__main__":

  hostname = sys.argv[1]
  port = sys.argv[2]
  status = sys.argv[3]


  if not validate_ip(hostname):
    print "Incorrect IP Address or Format"
    sys.exit(0)


  main(hostname, port, status)




