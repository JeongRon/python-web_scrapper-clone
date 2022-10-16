from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.find_all("section", class_="jobs"))

"""
Keyword Arguments / 개념 설명
1. 함수의 arguments 들은 순서에 알맞게 들어가야 함
2. 하지만, keyword를 넣으면, 순서에 알맞지 않고도 들어갈 수 있다. 
ex) say_hello(age=27, name="nico") == say_hello("nico", 27)
따라서 위 코드와 같은 class_=  : keyword Arguments 라는 것을 이해 하기
"""
