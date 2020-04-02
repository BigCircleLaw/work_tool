'''
@Author: your name
@Date: 2020-04-02 11:12:04
@LastEditTime: 2020-04-02 13:25:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /wonderbits_tool/work_tool/upload.py
'''
import sys
import os
import paramiko

remote_base_path = "/data/mfe-home/py-bin/lib"


def uploadFile(remote_folder, local_file_path):
    ssh = paramiko.SSHClient()
    # 第一次登录的认证信息
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(
        hostname='52.80.96.153',
        port=22,
        username='liuziyuan',
        password='liuziyuan250')

    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    local_file_name = os.path.basename(local_file_path)
    try:
        sftp.put(
            local_file_path, '{}/{}/{}'.format(remote_base_path, remote_folder,
                                               local_file_name))
    except Exception as e:
        raise e


if __name__ == '__main__':
    valid_remote_paths = [
        "mPython", "wb_mPython", "wb_mPython_v2", "wonderbits"
    ]
    if len(sys.argv) != 3:
        raise ValueError(
            "参数错误，第一个参数为{}其中任何一个，第二个参数为本地文件路径".format(valid_remote_paths))
    remote_folder = sys.argv[1]
    if remote_folder.startswith("/") \
            or remote_folder.endswith("/") \
            or remote_folder not in valid_remote_paths:
        raise ValueError("参数错误，远端路径只能为{}其中任何一个".format(valid_remote_paths))
    local_file_path = sys.argv[2]
    uploadFile(remote_folder, local_file_path)
