import tkinter as tk
import socket
import threading
import secrets

# Diffie-Hellman key exchange functions
def generate_private_key():
    return secrets.randbelow(999)

def generate_public_key(private_key, g, p):
    return pow(g, private_key, p)

def generate_shared_secret(private_key, other_public_key, p):
    return pow(other_public_key, private_key, p)

# Connect to the server and initiate Diffie-Hellman key exchange
def connect_to_server():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8888))
    status_label.config(text="Đã kết nối")
    exchange_button.config(state=tk.NORMAL)

# Perform Diffie-Hellman key exchange
def perform_key_exchange():
    # Wait for user to press the button
    status_label.config(text="Đang chờ trao đổi khoá...")
    exchange_button.config(state=tk.DISABLED)
    
    # Diffie-Hellman key exchange
    client_private_key = generate_private_key()
    client_public_key = generate_public_key(client_private_key, g, p)

    client_socket.sendall(str(client_public_key).encode())
    server_public_key = int(client_socket.recv(1024).decode())

    shared_secret = generate_shared_secret(client_private_key, server_public_key, p)

    status_label.config(text=f"Shared secret: {shared_secret}")
    
    client_socket.close()

# Diffie-Hellman parameters
g = 5  # Base
p = 23  # Prime modulus

# Create GUI using tkinter
root = tk.Tk()
root.title("Client")
root.geometry("800x800")  # Kích thước 800x800

# Create labels and buttons
status_label = tk.Label(root, text="Trạng thái: Chưa kết nối")
status_label.place(x=20, y=20)

connect_button = tk.Button(root, text="Kết nối", command=connect_to_server)
connect_button.place(x=20, y=50)

exchange_button = tk.Button(root, text="Trao đổi khoá", command=perform_key_exchange, state=tk.DISABLED)
exchange_button.place(x=20, y=80)

root.mainloop()
