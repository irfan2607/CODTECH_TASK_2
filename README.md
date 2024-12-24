**NAME:** SHAIK MOHAMMAD IRFAN  
**COMPANY:** CODTECH IT SOLUTIONS  
**ID:** CT08DS395  
**DOMAIN:** Cyber Security and Ethical Hacking  
**Duration:** December 2024 to January 2025  


# Vulnerability Scanning Tool

## Description
This tool scans a network or website for common security vulnerabilities. It identifies open ports, 
outdated software versions, and potential misconfigurations. It is lightweight yet powerful, 
with detailed output and report generation capabilities.

---

## Features
1. **Network Scanning**:
   - Scans specified IP ranges for open ports.
   - Detects running services and their versions.

2. **Web Scanning**:
   - Analyzes HTTP headers for potential security misconfigurations.
   - Supports integration with third-party tools for advanced detection.

3. **Reporting**:
   - Generates detailed vulnerability reports in CSV format.
   - Displays scan results in the terminal for quick insights.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `socket` - For low-level network communication.
  - `nmap` - For advanced port and service scanning.
  - `csv` - For generating output reports.

---

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd vulnerability-scanning-tool
   ```

2. **Install Dependencies**:
   Install required libraries using `pip`:
   ```bash
   pip install python-nmap
   ```

3. **Run the Script**:
   ```bash
   python vulnerability_scanner.py
   ```

4. **Features**:
   - Enter the target IP address or website to start the scan.
   - View open ports, services, and version details.
   - Save the scan results to a CSV file for documentation.

---

## File Structure
- `vulnerability_scanner.py`: Main script for scanning vulnerabilities.
- `README.md`: Documentation for the project.

---

## Sample Output
### Terminal Output:
```plaintext
Scanning 192.168.1.1 for vulnerabilities...
Host: 192.168.1.1
State: Up
Protocol: TCP
Port: 22    State: open    Service: ssh    Version: OpenSSH 7.9
Port: 80    State: open    Service: http   Version: Apache 2.4.41
```

### CSV Output:
```
Port,State,Service,Version
22,open,ssh,OpenSSH 7.9
80,open,http,Apache 2.4.41
```

---

## Future Enhancements
- Add a graphical user interface (GUI) for easier interaction.
- Extend scanning capabilities to include web application vulnerabilities (e.g., SQLi, XSS).
- Integrate a database for storing historical scan data.

---

## References
- [Nmap Documentation](https://nmap.org)
- [Python-Nmap Library](https://pypi.org/project/python-nmap/)

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author
[SHAIK MOHAMMAD IRFAN](https://github.com/irfan2607)
