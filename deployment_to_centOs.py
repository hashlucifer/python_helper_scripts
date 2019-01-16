import paramiko,os
import time
ip='mango.abc.com'
port=22
username='ctier'
password='ctier'
cmd='pwd'
remove_automation_deploy = "rm -rf /opt/ctier/automationDeploy/*"
source = 'src'
target = '/opt/ctier/automationDeploy'
sudo_pass = "ctier"
remove_tomcat_root_cmd = "rm -rf /opt/tomcat3/apache-tomcat-8.0.47/webapps/ROOT/*"
copy_cmd = "cp -r /opt/ctier/automationDeploy/* /opt/tomcat3/apache-tomcat-8.0.47/webapps/ROOT"


def command_executer (cmd) :
    print "Executing" , cmd
    stdin, stdout, stderr = ssh.exec_command(cmd)
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    print("Response: ", resp)
    print "Success", cmd


def command_executer_sudo (cmd,sudo_pass) :
    actual_command = "sudo -S -p '' "+cmd
    print "Executing" , actual_command
    stdin, stdout, stderr = ssh.exec_command(actual_command)
    stdin.write(sudo_pass + "\n")
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    print("Response: ", resp)
    print "Success", actual_command


ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)
print ("connected successfully!")

command_executer(cmd)
command_executer(remove_automation_deploy)

sftp = ssh.open_sftp()
print sftp
def put_dir(source,target,sftp):
    for item in os.listdir(source):
        print('%s/%s' % (source, item), '%s/%s' % (target, item))
        if os.path.isfile('%s/%s' % (source, item)):
            sftp.put('%s/%s' % (source, item), '%s/%s' % (target, item))
        else:
            print ('making dir start','%s/%s' % (target, item))
            try:
                sftp.chdir('%s/%s' % (target, item))  # Test if remote_path exists
            except IOError:
                sftp.mkdir('%s/%s' % (target, item),mode=511)  # Create remote_path
                put_dir('%s/%s' % (source, item), '%s/%s' % (target, item), sftp)

            print 'making dir success'
put_dir(source,target,sftp)
print "copied successfully!"
sftp.close()


command_executer_sudo(remove_tomcat_root_cmd,sudo_pass)
command_executer_sudo(copy_cmd,sudo_pass)


