# Proxy Server Documentation

## Overview

The Proxy Server script creates a simple TCP proxy server in Python. It listens for incoming connections from clients, forwards their requests to a target server, and relays the responses back to the clients.

## How to Run

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your system. If not, you can download and install it from [python.org](https://www.python.org/).

2. **Install Required Libraries:**
   - Open a terminal or command prompt.
   - Run the following command to install the required libraries:

     ```bash
     pip install socket threading
     ```

3. **Open a Text Editor:**
   - Open a text editor or an integrated development environment (IDE).

4. **Copy the Script:**
   - Copy the provided Proxy Server script.

5. **Save and Run:**
   - Save the file with a `.py` extension (e.g., `proxy_server.py`).
   - Run the script using the command:

     ```bash
     python proxy_server.py
     ```

## User Inputs

1. **Proxy Server Host (IPv4 Address):**
   - The host address on which the proxy server will listen for incoming connections. Defaults to `127.0.0.1` (localhost).

2. **Proxy Server Port:**
   - The port on which the proxy server will listen for incoming connections. Defaults to `8888`.

3. **Target Server Host (e.g., www.example.com):**
   - The host address of the target server to which the proxy will forward client requests.

4. **Target Server Port:**
   - The port of the target server to which the proxy will forward client requests.

## Example Usage

1. Start the proxy server script.
2. Enter the user inputs as prompted.
3. The proxy server will listen for connections and forward client requests to the specified target server.

---

# Proxy Client with HTML Viewer Documentation

## Overview

The Proxy Client with HTML Viewer script allows users to send HTTP requests to a proxy server for a specified URL. The response from the proxy server is then parsed to extract HTML content, which is displayed in an HTML viewer using a graphical user interface (GUI) built with `tkinter`.

## How to Run

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your system. If not, you can download and install it from [python.org](https://www.python.org/).

2. **Install Required Libraries:**
   - Open a terminal or command prompt.
   - Run the following command to install the required libraries:

     ```bash
     pip install requests beautifulsoup4
     ```

3. **Open a Text Editor:**
   - Open a text editor or an integrated development environment (IDE).

4. **Copy the Script:**
   - Copy the provided Proxy Client with HTML Viewer script.

5. **Save and Run:**
   - Save the file with a `.py` extension (e.g., `proxy_client_gui.py`).
   - Run the script using the command:

     ```bash
     python proxy_client_gui.py
     ```

## User Inputs

1. **Proxy Server Host:**
   - The host address of the proxy server to which the client will connect. Defaults to `127.0.0.1` (localhost).

2. **Proxy Server Port:**
   - The port of the proxy server to which the client will connect. Defaults to `8888`.

3. **Target URL (e.g., /path/to/page):**
   - The URL path for the HTTP request, relative to the proxy server.

## Usage

1. Enter the Proxy Server Host, Proxy Server Port, and Target URL.
2. Click the "Send Request" button.
3. The HTML content of the requested URL is displayed in the HTML viewer.

## Notes

- The script uses the `requests` library for handling HTTP requests and the `BeautifulSoup` library for HTML parsing.
- This is a basic example and may not handle all edge cases or dynamic content on web pages.