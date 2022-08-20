import paramiko


"""

import paramiko

command = "df"

# Update the next three lines with your
# server's information

host = "YOUR_IP_ADDRESS"
username = "YOUR_LIMITED_USER_ACCOUNT"
password = "YOUR_PASSWORD"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command("df")
print(stdout.read().decode())
client.close()




def key_based_connect(server):
     host = "192.0.2.0"
     special_account = "user1"
 pkey = paramiko.RSAKey.from_private_key_file("./id_rsa")
 client = paramiko.SSHClient()
     policy = paramiko.AutoAddPolicy()
          client.set_missing_host_key_policy(policy)
 client.connect(host, username=special_account, pkey=pkey)
 return client

"""


class User:
    def __init__(self, username=None, password=None, keyfile=None):
        self.username = username
        self.password = password
        self.keyfile = keyfile
        self.client = None
        self.connected = False

    def key_based_connect(self, server):
        if self.keyfile is not None:
            host = server.ipaddr
            pkey = paramiko.RSAKey.from_private_key_file(self.keyfile)
            self.client = paramiko.SSHClient()
            policy = paramiko.AutoAddPolicy()
            self.client.set_missing_host_key_policy(policy)
            self.client.connect(host, username=self.username, pkey=pkey)
            self.connected = True
            return (True, "connected")
        else:
            self.connected = False
            return (False, "problem with connecting with the provided key file")

    def sshclient(self, server):
        state = False
        if self.keyfile is not None:
            state,  msg = self.key_based_connect(server)
        if state is False:
            if self.password is not None:
                self.client = paramiko.client.SSHClient()
                self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.client.connect(server.ipaddr, username=self.username, password=self.password)
                self.connected = True
      
            else:
                return (False, None, "No password provided")

    
    def run_command(self, cmd):
        out = {}
        if self.connected:
            _stdin, _stdout,_stderr = self.client.exec_command(cmd)
            out["stdout"] = _stdout.read().decode() 
            out["stderr"] = _stderr.read().decode()
        return out
            
            
class Server:
    def __init__(self, ipaddr):
        self.ipaddr = ipaddr
        self.user = None

    def set_user(self, user):
        self.user = user

    def connect(self):
        self.user.sshclient(self)
        
class Node:
    def __init__(self, server, user):
        self.address = None
        self.server = server
        self.server.user = user
        self.server.connect()
        out = self.server.user.run_command("forta account address")
        self.address = out["stderr"].strip()
