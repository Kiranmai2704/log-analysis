import re
from collections import Counter
import csv

# Function to parse the log file and extract required data
def parse_log_file(file_path):
    ip_requests = Counter()
    endpoint_requests = Counter()
    failed_logins = Counter()

    with open(file_path, 'r') as log_file:
        for line in log_file:
            # Extract IP address
            ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                ip = ip_match.group(1)
                ip_requests[ip] += 1

            # Extract endpoint
            endpoint_match = re.search(r'"[A-Z]+\s(\/\S*)\sHTTP', line)
            if endpoint_match:
                endpoint = endpoint_match.group(1)
                endpoint_requests[endpoint] += 1

            # Detect failed logins
            if '401' in line or "Invalid credentials" in line:
                if ip_match:
                    failed_logins[ip] += 1

    return ip_requests, endpoint_requests, failed_logins

# Function to save results to a CSV file
def save_to_csv(ip_requests, most_accessed, failed_logins, output_file='log_analysis_results.csv'):
    with open(output_file, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Save Requests per IP
        writer.writerow(["IP Address", "Request Count"])
        for ip, count in ip_requests.most_common():
            writer.writerow([ip, count])

        # Save Most Accessed Endpoint
        writer.writerow([])
        writer.writerow(["Most Frequently Accessed Endpoint", "Access Count"])
        writer.writerow([most_accessed[0], most_accessed[1]])

        # Save Suspicious Activity
        writer.writerow([])
        writer.writerow(["IP Address", "Failed Login Count"])
        for ip, count in failed_logins.items():
            if count > 10:  # Configurable threshold
                writer.writerow([ip, count])

# Main function to execute the analysis
def main():
    log_file = "sample.log"  # Update with your log file path
    ip_requests, endpoint_requests, failed_logins = parse_log_file(log_file)

    # Get the most accessed endpoint
    most_accessed = endpoint_requests.most_common(1)[0]

    # Display results in the terminal
    print("\nIP Address Request Counts:")
    print(f"{'IP Address':<20}{'Request Count':<15}")
    for ip, count in ip_requests.most_common():
        print(f"{ip:<20}{count:<15}")

    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed[0]} (Accessed {most_accessed[1]} times)")

    print("\nSuspicious Activity Detected:")
    print(f"{'IP Address':<20}{'Failed Login Attempts':<15}")
    for ip, count in failed_logins.items():
        if count > 10:  # Configurable threshold
            print(f"{ip:<20}{count:<15}")

    # Save results to CSV
    save_to_csv(ip_requests, most_accessed, failed_logins)

    print("\nResults have been saved to 'log_analysis_results.csv'.")

if __name__ == "__main__":
    main()
