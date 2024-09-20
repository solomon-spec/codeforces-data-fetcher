import cloudscraper
from bs4 import BeautifulSoup
import time
from data import get_random_proxy, list_ids
# from concurrent.futures import ThreadPoolExecutor, as_completed



def fetch_problem_data(page_number, list_id):
    """
    Fetch problem data from a specific page and list of the Codeforces problemset.
    """
    page_url = f'https://codeforces.com/problemset/page/{page_number}?list={list_ids[list_id]}'
    problems = {}
    scraper = cloudscraper.create_scraper()
    connect_timeout = 10  
    read_timeout = 30  
    for attempt in range(2):
        response = scraper.get(page_url,proxies=get_random_proxy(page_number))


        if response.status_code == 403:
            print("403 Forbidden, retrying after 15 seconds...")
            time.sleep(15)
            continue

        if response.status_code == 200:
            request_end_time = time.time()
            parsing_start_time = time.time()
            soup = BeautifulSoup(response.text, 'html.parser')
            problems_table = soup.find('table', class_='problems')

            if problems_table:
                rows = problems_table.find_all('tr')[1:]

                for row in rows:
                    columns = row.find_all('td')
                    if len(columns) >= 5:
                        problem_id = columns[0].find('a').get_text(strip=True)
                        solved_tried = columns[4].find('span', class_='small notice')

                        if solved_tried:
                            solved, tried = map(int,solved_tried.get_text(strip=True).split('/'))
                        else:
                            solved, tried = 0, 0  # Default to 0 if not available

                        problems[problem_id] = {
                            'PID': problem_id,
                            'Stats': [{
                                'id': list_id,
                                'S': solved,
                                'A': tried
                            }]
                        }
            else:
                print('Problems table not found.')
        else:
            print(f'Failed to retrieve the page for list {list_id}. Status code: {response.status_code}')
        print(page_number, list_id)
        return problems


def fetch_last_page_number(base_url):
    """
    Fetch the last page number from the Codeforces problemset pagination.
    """
    scraper = cloudscraper.create_scraper() 
    for attempt in range(2):
        response = scraper.get(base_url,proxies = get_random_proxy(7))
        if response.status_code == 403:
            print("403 Forbidden, retrying after 15 seconds...")
            time.sleep(15)
            continue

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            pagination_div = soup.find('div', class_='pagination')

            if pagination_div:
                page_numbers = pagination_div.find_all('span', class_='page-index')
                if page_numbers:
                    last_page = page_numbers[-1].get_text(strip=True)
                    print(f"Last page for {base_url}: {last_page}")
                    return int(last_page)
                else:
                    print('No page numbers found in pagination.')
            else:
                print('Pagination div not found.')
        else:
            print(f'Failed to retrieve the page. Status code: {response.status_code}')

        return 0
