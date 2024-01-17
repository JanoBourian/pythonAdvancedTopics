import urllib.request
import time

with urllib.request.urlopen("https://flagicons.lipis.dev/") as response:
    html = response.read()
    html_string = html.decode()
    print(f"HTML: {html_string}")
    print(f"LEN(HTML): {len(html_string)}")
    # for line in html_string:
    #     print(line)
    #     time.sleep(0.2)