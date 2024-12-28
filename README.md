# SQL Injection Password Extractor

### Description

This Python script demonstrates a time-based SQL injection attack to extract a password from a vulnerable web application. The script is designed for educational purposes and is intended to help individuals learn about security vulnerabilities and their exploitation in a controlled environment, such as a lab.

WARNING: Unauthorized use of this script against systems you do not own or have explicit permission to test is illegal and unethical. The author is not responsible for any misuse or damage caused by this code.

### Features

Performs a time-based SQL injection to extract characters of a password one by one.

Uses response time to determine if the payload triggered the expected behavior.

Configurable parameters for target URL, cookies, charset, and password length.

### Requirements

- Python 3.x

- requests library

### Install the required library with:
```
pip install requests
```
### Configuration

Update the following configuration variables in the script:

- url: The target URL.

- cookie_name: The name of the cookie being exploited.

- cookies: Any required session cookies for authentication.

- charset: The character set to test (e.g., lowercase letters and digits).

- password_length: The length of the password to extract.

- tracking_id_template: The SQL payload template.

- proxies: (Optional) Set up for routing requests through a proxy, e.g., Burp Suite.

### Usage

1. Ensure you have permission to test the target application.

2. Update the configuration variables in the script.

3. Run the script:
```
python sql_injection_extractor.py
```
4. Monitor the output to view the extracted password.

### Legal Disclaimer

This script is provided for educational purposes only. The author does not condone the unauthorized use of this tool and is not responsible for any illegal activity or damages resulting from its use. Use this script only on systems you own or have explicit permission to test.
