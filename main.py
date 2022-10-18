from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

options = Options()

browser = webdriver.Chrome(options=options)

browser.get("https://kr.indeed.com/jobs?q=python&limit=50")

soup = BeautifulSoup(browser.page_source, "html.parser")
