import paramiko


class SshClient():

    def __init__(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def ssh_login(self, ip, username, password):
        """
        远程连接到ecs服务器
        @param ip: 服务器ip
        @param username: 用户名
        @param password: 密码
        @return:
        """
        try:
            self.ssh_client.connect(ip,port=22,username=username,password=password)
        except paramiko.AuthenticationException:
            return 1001
        except paramiko.ssh_exception.NoValidConnectionsError:
            return 1002
        except:
            return 1004
        return 1000

    def upload_file(self,file,remote_path):
        """
        上传文件
        @param file: 文件,本地文件路径 ， './peter.jpg'
        @param remote_path: 远程路径  /home/peter.jpg
        @return:
        """
        t = self.ssh_client.get_transport()
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(file,remote_path)

    def download_file(self,remote_path,file):
        """
        下载文件
        @param remote_path: 远程路径
        @param file: 文件
        @return:
        """
        t = self.ssh_client.get_transport()
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(remote_path,file)

    def execute_command(self,command):
        """
        执行命令
        @param command: 命令
        @return:
        """
        stdin, stdout, stderr = self.ssh_client.exec_command(command, get_pty=True)
        return stdin, stdout, stderr

    def ssh_logout(self):
        """
        关闭连接
        @return:
        """
        self.ssh_client.close()
