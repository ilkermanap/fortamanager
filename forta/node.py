import paramiko
import requests
import json
from datetime import datetime

FORTA_SLA="https://api.forta.network/stats/sla/scanner"


class Node:
    def __init__(self, server, user):
        self.address = None
        self.server = server
        self.server.set_user(user)
        self.server.connect()
        out = self.server.user.run_command("forta account address")
        self.address = out["stderr"].strip()

    def sla(self):        
        answer = requests.get(f"{FORTA_SLA}/{self.address}")
        if answer.status_code == 200:
            return json.loads(answer.text)
        else:
            return None

    def backup(self):
        datestr = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{self.address}_{datestr}.tar.gz"
        out = self.server.user.run_command("tar zcf forta.tar.gz .forta")
        self.server.user.copy_file("forta.tar.gz", filename)

    def status(self):
        out = self.server.user.run_command("forta status")
        return out
