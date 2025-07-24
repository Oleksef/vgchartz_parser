import pandas as pd
import requests
from lxml import html
import csv


PER_PAGE = 200
BASE_URL = "https://www.vgchartz.com"
URL_TAIL = f"/games/games.php?region=All&boxart=Both&banner=Both&ownership=Both&showmultiplat=Yes&results={PER_PAGE}&showtotalsales=1&showpublisher=1&showvgchartzscore=1&shownasales=1&showdeveloper=1&showcriticscore=1&showpalsales=1&showreleasedate=1&showuserscore=1&showjapansales=1&showlastupdate=1&showothersales=1&showshipped=1"


def run(start_url):
    """
    Makes a request to vgchartz.com and parses HTML. Transfers the content to process_gamelist()
    :param start_url: page with game list.
    """
    page = 1
    url = start_url
    session = requests.Session()
    while url:
        try:
            print(f"Fetching page {page}...")
            resp = session.get(url)
            tree = html.fromstring(resp.content)
            process_gamelist(tree)

            last_page = tree.xpath('//div[@id="generalBody"]//tr[contains(., "Results")]//span[a[contains(@href, "page")]][last()]//@href')
            if last_page:
                last_page = int(last_page[0].split('page=')[-1].split('&')[0])
                page += 1
                url = BASE_URL + URL_TAIL + f"&page={page}" if page <= last_page else None

        except Exception as e:
            print(e)


def process_gamelist(data):
    """
    Processes HTML content, collecting a games data. Recursively moves through pages to the last one.
    :param data: raw HTML content of the current page with game list.
    """
    games = data.xpath('//div[@id="generalBody"]//tr[td[a]]')
    print(f'Processing {len(games)} games...')
    for game in games:
        item = dict(
            name = game.xpath('td/a/text()')[0],
            platform = game.xpath('td/img[contains(@src,"/console")]/@alt')[0],
            publisher = game.xpath('td[5]/text()')[0],
            developer = game.xpath('td[6]/text()')[0],
            vgs_score = game.xpath('td[7]/text()')[0],
            critic_score = game.xpath('td[8]/text()')[0],
            user_score = game.xpath('td[9]/text()')[0],
            total_shipped = game.xpath('td[10]/text()')[0],
            total_sales = game.xpath('td[11]/text()')[0],
            na_sales = game.xpath('td[12]/text()')[0],
            pal_sales = game.xpath('td[13]/text()')[0],
            jp_sales = game.xpath('td[14]/text()')[0],
            other_sales = game.xpath('td[15]/text()')[0],
            release_date = game.xpath('td[16]/text()')[0]
        )

        game_list.append(item)


if __name__ == "__main__":
    game_list = []
    full_url = BASE_URL + URL_TAIL
    run(full_url)

    if game_list:
        df = pd.DataFrame(game_list)
        df.to_csv("games.csv", index=False, quoting=csv.QUOTE_ALL)