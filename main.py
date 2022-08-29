from forta import Node, User, Server

u = User(username="forta", keyfile="/home/ilker/.ssh/id_rsa")
s = Server("192.168.1.240")
n = Node(s,u)

print(n.sla()["statistics"])

n.backup()
print(n.status())
