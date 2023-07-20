import requests
import sys
import re

print('''

 ▄█     █▄   ▄█  ███▄▄▄▄       ███        ▄████████  ▄█       
███     ███ ███  ███▀▀▀██▄ ▀█████████▄   ███    ███ ███       
███     ███ ███▌ ███   ███    ▀███▀▀██   ███    █▀  ███       
███     ███ ███▌ ███   ███     ███   ▀  ▄███▄▄▄     ███       
███     ███ ███▌ ███   ███     ███     ▀▀███▀▀▀     ███       
███     ███ ███  ███   ███     ███       ███    █▄  ███       
███ ▄█▄ ███ ███  ███   ███     ███       ███    ███ ███▌    ▄ 
 ▀███▀███▀  █▀    ▀█   █▀     ▄████▀     ██████████ █████▄▄██ 
is a Whois Intelligence Tool

Developed by Th3 BlackHol3
https://twitter.com/Th3BlackHol3_
https://www.linkedin.com/in/th3blackhol3/
''')

def fetch_whois_data(domain):
    base_url = "https://www.whoxy.com/"
    url = f"{base_url}/{domain}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.text
        pattern = r'<pre>(.*?)</pre>'
        result = re.search(pattern, data, re.DOTALL)
        if result:
            whois_data = result.group(1)
            cleaned_data = re.sub(r'<.*?>', '', whois_data)
            return cleaned_data.strip()
        else:
            return "No data found for the domain."
    else:
        return "Error fetching data."

def main():
    if len(sys.argv) != 2:
        print("Usage: python wintel.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    result = fetch_whois_data(domain)
    print(result)

if __name__ == "__main__":
    main()
