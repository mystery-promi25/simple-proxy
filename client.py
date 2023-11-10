import socket
import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

def send_request():
    proxy_host = entry_proxy_host.get()
    proxy_port = int(entry_proxy_port.get())
    target_url = entry_target_url.get()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((proxy_host, proxy_port))

    # Send a GET request for the specified URL
    request = f"GET {target_url} HTTP/1.1\r\nHost: {proxy_host}\r\n\r\n"
    client_socket.send(request.encode())

    # Receive and parse the response
    response = client_socket.recv(4096)
    html_content = extract_html_content(response.decode())

    # Display the HTML content in the viewer
    text_html_content.config(state=tk.NORMAL)
    text_html_content.delete("1.0", tk.END)
    text_html_content.insert(tk.END, html_content)
    text_html_content.config(state=tk.DISABLED)

    client_socket.close()

def extract_html_content(response_text):
    # Extract HTML content from the response
    soup = BeautifulSoup(response_text, 'html.parser')
    html_content = soup.prettify()
    return html_content

# GUI setup
root = tk.Tk()
root.title("Proxy Client with HTML Viewer")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Proxy Server Host
ttk.Label(frame, text="Proxy Server Host:").grid(row=0, column=0, sticky=tk.W)
entry_proxy_host = ttk.Entry(frame)
entry_proxy_host.grid(row=0, column=1, sticky=(tk.W, tk.E))
entry_proxy_host.insert(tk.END, "127.0.0.1")

# Proxy Server Port
ttk.Label(frame, text="Proxy Server Port:").grid(row=1, column=0, sticky=tk.W)
entry_proxy_port = ttk.Entry(frame)
entry_proxy_port.grid(row=1, column=1, sticky=(tk.W, tk.E))
entry_proxy_port.insert(tk.END, "8888")

# Target URL
ttk.Label(frame, text="Target URL (e.g., /path/to/page):").grid(row=2, column=0, sticky=tk.W)
entry_target_url = ttk.Entry(frame)
entry_target_url.grid(row=2, column=1, sticky=(tk.W, tk.E))
entry_target_url.insert(tk.END, "/")

# Send Request Button
btn_send_request = ttk.Button(frame, text="Send Request", command=send_request)
btn_send_request.grid(row=3, column=0, columnspan=2, pady=10)

# HTML Viewer
ttk.Label(frame, text="HTML Content:").grid(row=4, column=0, sticky=tk.W)
text_html_content = tk.Text(frame, height=15, width=80, state=tk.DISABLED)
text_html_content.grid(row=4, column=1, sticky=tk.W)

root.mainloop()