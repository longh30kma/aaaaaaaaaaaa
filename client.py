import tkinter as tk
import socket
import threading
import secrets
from ccakem import *
from suportfun import *
import khoacung2
from Crypto.Hash import SHA3_256
import time
def sha3_256_hash(message):
    sha3 = SHA3_256.new()
    sha3.update(message)
    return sha3.digest()
def receive_data(conn):
    received_data = b""
    while True:
        chunk = conn.recv(1024)
        if chunk.endswith(b"END"):
            received_data += chunk[:-3]  # Remove the END marker
            break
        received_data += chunk
    return received_data


# Handle client connection
def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8888))
    client_address = client_socket.getpeername()
    ip, port = client_address
    status_label1.config(text=f"Đã kết nối",font=('UTM Avo',9))
    status_label2.config(text=f"Địa chỉ ip là: {ip}",font=('UTM Avo',9))
    status_label3.config(text=f"Cổng là: {port}",font=('UTM Avo',9))
    with open('pk1.txt', 'r') as file:
        Pk1 = file.read()
    Sk2= khoacung2.Sk2
    X = receive_data(client_socket)
    X=X.decode()
    C2,Pk = string_to_2tuples(X)
    text_box11.insert(tk.INSERT,tuple_to_hex_string(Pk))
    text_box12.insert(tk.INSERT,tuple_to_hex_string(C2))
    start_time1 = time.time()
    K2 = kem_decaps1024((Sk2),list(C2))
    text_box13.insert(tk.INSERT,tuple_to_hex_string(K2))
    text_box110.insert(tk.INSERT,tuple_to_hex_string(K2))
    end_time1 = time.time()
    execution_time1 = end_time1 - start_time1
    # status_label1.config(text=f"Thời gian: {format(execution_time1)}")

    

    start_time2 = time.time()
    K,C=kem_encaps1024(list(Pk))
    text_box14.insert(tk.INSERT,tuple_to_hex_string(K))
    text_box18.insert(tk.INSERT,tuple_to_hex_string(K))
    text_box15.insert(tk.INSERT,tuple_to_hex_string(C))
    end_time2 = time.time()
    execution_time2 = end_time2 - start_time2
    # status_label2.config(text=f"Thời gian: {format(execution_time2)}")

    start_time3 = time.time()
    K1,C1=kem_encaps1024(stringtotuple(Pk1))
    text_box16.insert(tk.INSERT,tuple_to_hex_string(K1))
    text_box19.insert(tk.INSERT,tuple_to_hex_string(K1))
    text_box17.insert(tk.INSERT,tuple_to_hex_string(C1))
    end_time3 = time.time()
    execution_time3 = end_time3 - start_time3
    # status_label3.config(text=f"Thời gian: {format(execution_time3)}")

    text_box13.insert(tk.INSERT,tuple_to_hex_string(K1))
    client_socket.sendall(str(C).encode())
    client_socket.sendall(str(C1).encode())
    client_socket.sendall(b"END")

    start_time4 = time.time()
    K3=K+K1+K2
    KK = sha3_256_hash(str(K3).encode())
    end_time4 = time.time()
    execution_time4 = end_time4 - start_time4
    # status_label4.config(text=f"Thời gian: {format(execution_time4)}")

    text_box111.insert(tk.INSERT,(KK).hex())
    client_socket.close()

# Start the server

# Create GUI using tkinter
def show_page(page):
        page.tkraise()

def switch_to_page1():
    show_page(page1)

def switch_to_page2():
    show_page(page2)

def switch_to_page3():
    show_page(page3)
# Create GUI using tkinter
root = tk.Tk()
root.title("Bob")
root.geometry("1350x800")  # Kích thước 800x800
pages = {}
#page1
page1 = tk.Frame(root)
page1.place(x=0, y=0, width=1350, height=800)
label1 = tk.Label(page1, text="MÔ PHỎNG TRAO ĐỔI KHOÁ KYBER",font=('UTM Avo',30))
label1.place(x=270, y=0)
label1 = tk.Label(page1, text="PHARSE 1:",font=('UTM Avo',15))
label1.place(x=590, y=110)
label1 = tk.Label(page1, text="Bước 1: Nhận được Pk và C2 từ bên đối diện",font=('UTM Avo',12))
label1.place(x=20, y=150)
label1 = tk.Label(page1, text="Pk:",font=('UTM Avo',12))
label1.place(x=20, y=180)
label1 = tk.Label(page1, text="C2:",font=('UTM Avo',12))
label1.place(x=20, y=430)
label1 = tk.Label(page1, text="K2:",font=('UTM Avo',12))
label1.place(x=20, y=680)
client_button = tk.Button(page1, text="BẮT ĐẦU KẾT NỐI VÀ TRAO ĐỔI KHOÁ", command=start_client)
client_button.place(width=240, height=51,x=990, y=20)
client_button = tk.Button(page1, text="Chuyển sang PHARSE 2", command=switch_to_page2)
client_button.place(width=240, height=51,x=990, y=80)
text_box11 = tk.Text(page1, wrap=tk.WORD)  # Sử dụng wrap=tk.WORD để tự động xuống dòng khi văn bản vượt quá khung
text_box11.place(width=1281, height=210, x=20,y=210)
text_box12 = tk.Text(page1, wrap=tk.WORD)  # Sử dụng wrap=tk.WORD để tự động xuống dòng khi văn bản vượt quá khung
text_box12.place(width=1281, height=210, x=20,y=460)
text_box13 = tk.Text(page1, wrap=tk.WORD)  # Sử dụng wrap=tk.WORD để tự động xuống dòng khi văn bản vượt quá khung
text_box13.place(width=1281, height=51, x=20,y=715)

status_label1 = tk.Label(page1, text="",font=('UTM Avo',12))
status_label1.place(x=20, y=35)
status_label2 = tk.Label(page1, text="",font=('UTM Avo',12))
status_label2.place(x=20, y=55)
status_label3 = tk.Label(page1, text="",font=('UTM Avo',12))
status_label3.place(x=20, y=75)
#page2
page2 = tk.Frame(root)
page2.place(x=0, y=0, width=1300, height=800)
label1 = tk.Label(page2, text="MÔ PHỎNG TRAO ĐỔI KHOÁ KYBER",font=('UTM Avo',30))
label1.place(x=270, y=0)
label1 = tk.Label(page2, text="PHARSE 2:",font=('UTM Avo',15))
label1.place(x=590, y=110)
label1 = tk.Label(page2, text="Bước 2: Sinh ngẫu nhiên K và K1 sau đó bọc lại bằng Pk và Pk1 để thu được C và C1",font=('UTM Avo',12))
label1.place(x=20, y=140)
label1 = tk.Label(page2, text="K được sinh ngẫu nhiên:",font=('UTM Avo',12))
label1.place(x=20, y=170)
label1 = tk.Label(page2, text="C thu được khi bọc K lại bằng Pk:",font=('UTM Avo',12))
label1.place(x=20, y=260)
label1 = tk.Label(page2, text="K1 được sinh ngẫu nhiên::",font=('UTM Avo',12))
label1.place(x=20, y=460)
label1 = tk.Label(page2, text="C1 thu được khi bọc K lại bằng Pk1",font=('UTM Avo',12))
label1.place(x=20, y=560)
client_button = tk.Button(page2, text="Chuyển sang PHARSE 3", command=switch_to_page3)
client_button.place(width=240, height=51,x=990, y=80)
text_box14 = tk.Text(page2, wrap=tk.WORD)  # Sử dụng wrap=tk.WORD để tự động xuống dòng khi văn bản vượt quá khung
text_box14.place(width=1281, height=51, x=20,y=200)
text_box15 = tk.Text(page2, wrap=tk.WORD)  # Sử dụng wrap=tk.WORD để tự động xuống dòng khi văn bản vượt quá khung
text_box15.place(width=1281, height=161, x=20,y=290)
text_box16 = tk.Text(page2, wrap=tk.WORD)  # Sử dụng wrap=tk.WORD để tự động xuống dòng khi văn bản vượt quá khung
text_box16.place(width=1281, height=51, x=20,y=490)
text_box17 = tk.Text(page2, wrap=tk.WORD)  # Sử dụng wrap=tk.WORD để tự động xuống dòng khi văn bản vượt quá khung
text_box17.place(width=1281, height=161, x=20,y=590)
#page3
page3 = tk.Frame(root)
page3.place(x=0, y=0, width=1300, height=800)
label1 = tk.Label(page3, text="MÔ PHỎNG TRAO ĐỔI KHOÁ KYBER",font=('UTM Avo',30))
label1.place(x=270, y=0)
label1 = tk.Label(page3, text="PHARSE 3:",font=('UTM Avo',15))
label1.place(x=600, y=110)
label1 = tk.Label(page3, text="Bước 4: Sử dụng hàm băm với đầu vào là 3 thông tin bí mật vừa trao đổi K2,K',K1' để thu được khoá bí mật chung cho phiên",font=('UTM Avo',12))
label1.place(x=20, y=150)
label1 = tk.Label(page3, text="K:",font=('UTM Avo',12))
label1.place(x=20, y=200)
label1 = tk.Label(page3, text="K1:",font=('UTM Avo',12))
label1.place(x=20, y=300)
label1 = tk.Label(page3, text="K2:",font=('UTM Avo',12))
label1.place(x=20, y=400)
label1 = tk.Label(page3, text="Key:",font=('UTM Avo',12))
label1.place(x=20, y=500)
text_box18 = tk.Text(page3, wrap=tk.WORD)  # Sử dụng wrap=tk.WORD để tự động xuống dòng khi văn bản vượt quá khung
text_box18.place(width=1281, height=61, x=20,y=230)
text_box19 = tk.Text(page3, wrap=tk.WORD)  # Sử dụng wrap=tk.WORD để tự động xuống dòng khi văn bản vượt quá khung
text_box19.place(width=1281, height=61, x=20,y=330)
text_box110 = tk.Text(page3, wrap=tk.WORD)  # Sử dụng wrap=tk.WORD để tự động xuống dòng khi văn bản vượt quá khung
text_box110.place(width=1281, height=61, x=20,y=430)
text_box111 = tk.Text(page3, wrap=tk.WORD)  # Sử dụng wrap=tk.WORD để tự động xuống dòng khi văn bản vượt quá khung
text_box111.place(width=1281, height=61, x=20,y=530)
client_button = tk.Button(page3, text="Chuyển sang PHARSE 1", command=switch_to_page1)
client_button.place(width=240, height=51,x=990, y=80)
show_page(page1)

root.mainloop()
