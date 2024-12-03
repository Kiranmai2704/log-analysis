Log Analysis Script

This repository contains a Python script designed to analyze server log files. The script processes the log data to extract and display key insights, including:
- The number of requests made by each IP address.
- The most frequently accessed endpoint.
- Suspicious activity related to failed login attempts.

This analysis is valuable for cybersecurity-related tasks such as detecting potential brute-force attacks and monitoring server traffic.

Key Features
1. Count Requests per IP Address: The script counts how many requests were made by each IP address and displays the results in descending order.
2. Identify the Most Frequently Accessed Endpoint: It identifies the most frequently accessed endpoint (e.g., `/home`, `/login`) in the log file.
3. Detect Suspicious Activity: The script detects IP addresses that have made multiple failed login attempts, which may indicate a brute-force attack.

Requirements
- Python 3.x
- Required Libraries:
  - `re` (for regular expressions)
  - `collections` (for counting occurrences)
  - `csv` (for saving results in CSV format)

How to Run

1. Clone the Repository
Clone the repository to your local machine using the following command:
```bash
git clone https://github.com/Kiranmai2704/log-analysis.git
```
2. Navigate to the Project Directory
Once the repository is cloned, navigate into the project directory:
```bash
cd log-analysis
```
3. Run the Script
Execute the Python script to analyze the log file:
```bash
python log_analysis.py
```
4. Results
The script will display the analysis results in the terminal and save them in a CSV file named `log_analysis_results.csv`. The results will include:
- Requests per IP Address
- Most Accessed Endpoint
- Suspicious Activity (failed login attempts)

Example Output

Requests per IP Address:
```
IP Address           Request Count
192.168.1.1          234
203.0.113.5          187
10.0.0.2             92
```

Most Frequently Accessed Endpoint:
```
Most Frequently Accessed Endpoint:
/home (Accessed 403 times)
```

Suspicious Activity:
```
Suspicious Activity Detected:
IP Address           Failed Login Attempts
192.168.1.100        56
203.0.113.34         12
```
Technologies Used:
- Python: For writing the log processing script.
- Regular Expressions (`re`): For extracting relevant log information (IP addresses, endpoints, status codes, etc.).
- Collections (`Counter`): For counting and sorting IP address requests and endpoints.
- CSV: For saving the results in CSV format.

License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
