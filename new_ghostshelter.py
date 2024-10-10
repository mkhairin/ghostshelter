import socket
import whois
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime
from colorama import Fore, Style, init

init()

# Fungsi untuk memindai port
def scan_port(host, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = scanner.connect_ex((host, port))
    scanner.close()
    return result == 0

# Fungsi whois
def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return f"An error occurred: {e}"

# Fungsi whatweb
def get_website_info(url):
    try:
        response = requests.get(url)
        headers = response.headers

        info = {
            'URL': url,
            'Status Code': response.status_code,
            'Server': headers.get('Server', 'Not Available'),
            'Content-Type': headers.get('Content-Type', 'Not Available'),
            'X-Powered-By': headers.get('X-Powered-By', 'Not Available'),
            'X-Frame-Options': headers.get('X-Frame-Options', 'Not Available'),
            'X-Content-Type-Options': headers.get('X-Content-Type-Options', 'Not Available'),
        }

        return info

    except requests.RequestException as e:
        return {'Error': str(e)}

# Fungsi scanning analisis
port_services = {
    20: 'FTP Data',
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    26: 'SMTP Alternatif',
    27: 'NSW',
    53: 'DNS',
    67: 'DHCP Server',
    68: 'DHCP Client',
    69: 'TFTP',
    80: 'HTTP',
    81: 'HTTP-alt',
    82: 'HTTP-mgmt',
    83: 'HTTP',
    110: 'POP3',
    111: 'RPCbind',
    113: 'Ident',
    119: 'NNTP',
    123: 'NTP',
    135: 'MS RPC',
    137: 'NetBIOS Name Service',
    138: 'NetBIOS Datagram Service',
    139: 'NetBIOS Session Service',
    143: 'IMAP',
    161: 'SNMP',
    162: 'SNMP Trap',
    179: 'BGP',
    194: 'IRC',
    443: 'HTTPS',
    445: 'Microsoft-DS',
    464: 'Kerberos Change/Set Password',
    514: 'Syslog',
    515: 'Printer',
    543: 'Klogin',
    544: 'KShell',
    545: 'AppleTalk',
    554: 'RTSP',
    587: 'SMTP SSL',
    636: 'LDAPS',
    993: 'IMAPS',
    995: 'POP3S',
    1080: 'SOCKS Proxy',
    1433: 'MS SQL Server',
    1434: 'MS SQL Server',
    1521: 'Oracle',
    3306: 'MySQL',
    3389: 'RDP',
    5432: 'PostgreSQL',
    5900: 'VNC',
    8080: 'HTTP-alt',
    8443: 'HTTPS-alt',
    8888: 'HTTP-alt',
    9200: 'Elasticsearch',
    11211: 'Memcached'
}

def extract_host(url):
    parsed_url = urlparse(url)
    return parsed_url.hostname or url  # Return the URL if it's already an IP

def scan_ports(host, ports):
    open_ports = []
    closed_ports = []

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        service_name = port_services.get(port, 'Unknown Service')

        if result == 0:
            open_ports.append((port, service_name))
        else:
            closed_ports.append((port, service_name))

        sock.close()

    return open_ports, closed_ports

# Fungsi hidden files
hidden_files = [
    '.env', '.git/config', '.gitignore', '.htaccess', '.svn/entries', '.idea/',
    'admin/', 'backup/', 'config/', 'db/', 'logs/', 'temp/', 'uploads/',
    'config.php', 'web.config', 'wp-config.php', 'setup.php', 'admin.php', 'error.log',
    'sqlmap.log', 'debug.log', 'config.json', 'settings.py', 'db_config.php',
    'app/config.php', 'application/config.php', 'config.inc.php', 'private/', 'hidden/',
    'site/backup/', 'backup.sql', 'old/', 'tmp/', 'cache/', 'error/', 'log/', 'phpinfo.php',
    'index.php', 'README.md', 'CNAME', 'robots.txt', 'sitemap.xml', 'license.txt', 'composer.json',
    'composer.lock', 'package.json', 'yarn.lock', '.bash_history', '.mysql_history', '.python_history'
]

def check_hidden_files(url):
    for file in hidden_files:
        test_url = url.rstrip('/') + '/' + file
        try:
            response = requests.get(test_url)
            status_code = response.status_code
            if status_code == 200:
                print(f"{Fore.GREEN}File found (Status {status_code}): {test_url}{Style.RESET_ALL}")
            elif status_code == 403:
                print(f"{Fore.RED}Access denied (Status {status_code}): {test_url}{Style.RESET_ALL}")
            elif status_code == 404:
                print(f"File not found (Status {status_code}): {test_url}")
            else:
                print(f"Status {status_code} for {test_url}")
        except requests.RequestException as e:
            print(f"An error occurred while checking {test_url}: {e}")

# Fungsi utama
def main():
    # Menampilkan judul alat
    print(r"""
   ______ __                  __     _____  __           __ __             
  / ____// /_   ____   _____ / /_   / ___/ / /_   ___   / // /_ ___   _____
 / / __ / __ \ / __ \ / ___// __/   \__ \ / __ \ / _ \ / // __// _ \ / ___/
/ /_/ // / / // /_/ /(__  )/ /_    ___/ // / / //  __// // /_ /  __// /    
\____//_/ /_/ \____//____/ \__/   /____//_/ /_/ \___//_/ \__/ \___//_/  ver.0.0

by Muhammad Khairin""")
    print("---------------------------------------------------------------------")
    # Menu pemindaian
    print("Select The Tools Type: ")
    print("[1]. PortSpecter - Port Scanning")
    print("[2]. NameDiscoverer - Whois")
    print("[3]. WebReveal - Whatweb")
    print("[4]. ScanRaptor - Network Analysis")
    print("[5]. FileFinder - File Scanning")
    print("---------------------------------------------------------------------")
    choice = input("Enter options 1-5): ")

    if choice == "1":
        domain = input("Enter the domain or IP to scan: ")
        try:
            host_ip = socket.gethostbyname(domain)
        except socket.gaierror:
            host_ip = domain  # Treat as IP if domain resolution fails

        print(f"Starts a scan on the host: {host_ip}")

        # Memasukkan rentang port untuk dipindai
        start_port = int(input("Masukkan port awal: "))
        end_port = int(input("Masukkan port akhir: "))

        # Mencatat waktu mulai
        start_time = datetime.now()

        # Memindai port dalam rentang waktu tertentu
        for port in range(start_port, end_port + 1):
            if scan_port(host_ip, port):
                print(f"{Fore.GREEN}Port {port} open{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Port {port} close{Style.RESET_ALL}")

        # Mencatat waktu selesai
        end_time = datetime.now()
        total_time = end_time - start_time

        print(f"Pemindaian selesai dalam waktu: {total_time}")

    elif choice == "2":
        domain = input("Enter the domain name: ")
        info = get_whois_info(domain)
        print(f"{Fore.GREEN}{info}{Style.RESET_ALL}")

    elif choice == "3":
        url = input("Enter the website URL (e.g., http://example.com): ")
        info = get_website_info(url)
        for key, value in info.items():
            print(f"{key}: {value}")

    elif choice == "4":
        url = input("Enter the URL to scan (e.g., http://example.com): ")

        # Ekstrak hostname dari URL
        host = extract_host(url)

        if host:
            try:
                # Konversi domain ke IP jika diperlukan
                host_ip = socket.gethostbyname(host)
                print(f"Starting network analysis on {host_ip}...")

                # Daftar port umum untuk dipindai
                common_ports = [20, 21, 22, 23, 25, 53, 80, 443, 8080]
                open_ports, closed_ports = scan_ports(host_ip, common_ports)

                # Tampilkan hasil pemindaian
                print(f"Open Ports for {host_ip}:")
                for port, service in open_ports:
                    print(f"Port {port} ({service}) is open.")
                print(f"Closed Ports for {host_ip}:")
                for port, service in closed_ports:
                    print(f"Port {port} ({service}) is closed.")

            except socket.gaierror:
                print("Unable to resolve the host.")
        else:
            print("Invalid URL.")

    elif choice == "5":
        url = input("Enter the URL to scan for hidden files: ")
        check_hidden_files(url)

    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
