import nmap

def vulnerability_scan(ip):
    scanner = nmap.PortScanner()
    print(f"Scanning {ip} for vulnerabilities...")
    scanner.scan(ip, '1-1024', '-sV')  # Scans ports 1-1024 and detects versions

    for host in scanner.all_hosts():
        print(f"Host: {host} ({scanner[host].hostname()})")
        print(f"State: {scanner[host].state()}")
        for proto in scanner[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = scanner[host][proto].keys()
            for port in ports:
                print(f"Port: {port}\tState: {scanner[host][proto][port]['state']}")
                print(f"Service: {scanner[host][proto][port]['product']}, Version: {scanner[host][proto][port]['version']}")

# Example usage
target_ip = input("Enter IP address to scan: ")
vulnerability_scan(target_ip)
