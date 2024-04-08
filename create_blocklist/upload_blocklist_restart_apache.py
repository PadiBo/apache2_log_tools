import paramiko

def upload_and_restart_apache(hostname, port, username, password, local_path, remote_path):
    try:
        # Set up SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the server
        ssh_client.connect(hostname, port=port, username=username, password=password)

        # Set up SFTP client
        sftp_client = ssh_client.open_sftp()

        # Upload the file
        sftp_client.put(local_path, remote_path)

        # Close SFTP connection
        sftp_client.close()

        # Restart Apache server
        stdin, stdout, stderr = ssh_client.exec_command('sudo systemctl restart apache2')
        
        # Print output of the command
        print(stdout.read().decode('utf-8'))

        # Close SSH connection
        ssh_client.close()

        print("File uploaded successfully and Apache server restarted.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    hostname = "ip"
    port = 22  # Default SSH port
    username = "username"
    password = "password"
    local_path = "ip_ranges.conf"
    remote_path = "/etc/apache2/blocker/ip_ranges.conf"

    upload_and_restart_apache(hostname, port, username, password, local_path, remote_path)
