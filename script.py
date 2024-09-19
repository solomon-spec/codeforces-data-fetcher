import cloudscraper
from bs4 import BeautifulSoup
import json

def fetch_last_page_number(base_url):
    """
    Fetch the last page number from the Codeforces problemset pagination.
    """
    scraper = cloudscraper.create_scraper()
    response = scraper.get(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        pagination_div = soup.find('div', class_='pagination')

        if pagination_div:
            page_numbers = pagination_div.find_all('span', class_='page-index')
            if page_numbers:
                last_page = page_numbers[-1].get_text(strip=True)
                print(last_page)
                return int(last_page)
            else:
                print('No page numbers found in pagination.')
        else:
            print('Pagination div not found.')
    else:
        print(f'Failed to retrieve the page. Status code: {response.status_code}')

    return 0

def fetch_problem_data(page_number):
    """
    Fetch problem data from a specific page of the Codeforces problemset.
    """
    page_url = f'https://codeforces.com/problemset/page/{page_number}?list=9453965cd32f77f49eb00a1a463deccb'
    problems = []

    scraper = cloudscraper.create_scraper()
    response = scraper.get(page_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        problems_table = soup.find('table', class_='problems')

        if problems_table:
            rows = problems_table.find_all('tr')[1:]  # Skip header row

            for row in rows:
                columns = row.find_all('td')
                if len(columns) >= 5:
                    problem_id = columns[0].find('a').get_text(strip=True)
                    solved_tried = columns[4].find('span', class_='small notice')

                    if solved_tried:
                        solved, tried = solved_tried.get_text(strip=True).split('/')
                    else:
                        solved, tried = "0", "0"  # Default to 0 if not available

                    problem_info = {
                        'Problem ID': problem_id,
                        'Solved by': f'{solved}',
                        'Attempted by': f'{tried}'
                    }
                    problems.append(problem_info)
        else:
            print('Problems table not found.')
    else:
        print(f'Failed to retrieve the page. Status code: {response.status_code}')
    print(page_number)
    return problems

def main():
    base_url = 'https://codeforces.com/problemset'
    last_page_number = fetch_last_page_number(base_url)
    last_page_number = 5

    all_problems = []
    for page in range(1, last_page_number + 1):
        problems = fetch_problem_data(page)
        all_problems.extend(problems)

    with open('data.txt', 'w') as file:
        file.write(json.dumps(all_problems, indent=4))


if __name__ == '__main__':
    main()
