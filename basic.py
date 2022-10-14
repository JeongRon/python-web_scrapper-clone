from requests import get

websites = (
    "https://daum.net",
    "https://github.com",
    "twitter.com",
    "facebook.com",
    "naver.com",
)

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code >= 500:
        results[website] = "Server Error"
    elif response.status_code >= 400:
        results[website] = "Client Error Response"
    elif response.status_code >= 300:
        results[website] = "Redirection"
    elif response.status_code >= 200:
        results[website] = "Success"
    elif response.status_code >= 100:
        results[website] = "OK"
    else:
        results[website] = "FAILED"
print(results)
