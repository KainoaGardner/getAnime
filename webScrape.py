import nest_asyncio; nest_asyncio.apply()
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


airingToday = {}

url = "https://www.livechart.me/schedule"
with sync_playwright() as pw:
    browser = pw.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    # page.wait_for_selector("div[data-target=directory-first-item]")

        
    soup = BeautifulSoup(page.content(),'html.parser')
    parsed = []

    s = soup.find("div",class_="lc-timetable-day lc-today")
    content = s.find_all("div",class_="lc-timetable-anime-block")

    for block in content:
        links = block.find_all("a")
        
        title = links[0].get_text() 
        episode = links[1].get_text().split()

        episode = episode[0]

        episodeDict = {"ep":episode}
        
        airingToday.update({title:episodeDict})



