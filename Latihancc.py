# membuat SSH pada Cloud computing
import paramiko

def ssh_connect(host, port, username, password, command):
    try:
        # Membuat SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Auto accept host key
        client.connect(hostname=host, port=port, username=username, password=password)

        print(f"Terhubung ke {host}")

        # Eksekusi perintah
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        print("Output:")
        print(output)

        if error:
            print("Error:")
            print(error)

        client.close()
    except Exception as e:
        print(f"Gagal terhubung: {e}")

# Contoh pemakaian
if __name__ == "__main__":
    host = "192.168.1.10"      # Ganti dengan IP/hostname server SSH Anda
    port = 22
    username = "useranda"
    password = "passwordanda"
    command = "ls -l"          # Perintah yang ingin dijalankan di remote server

    ssh_connect(host, port, username, password, command)
