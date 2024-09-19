import cloudscraper
from bs4 import BeautifulSoup
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import random
import requests



proxies = ['Tikursew:Letmeknow@89.40.223.8:6044', 'Tikursew:Letmeknow@103.75.229.130:5878', 'Tikursew:Letmeknow@23.236.222.216:7247', 'Tikursew:Letmeknow@64.137.70.78:5629', 'Tikursew:Letmeknow@64.137.31.27:6641', 'Tikursew:Letmeknow@64.137.31.61:6675', 'Tikursew:Letmeknow@185.118.6.31:5747', 'Tikursew:Letmeknow@64.137.96.206:6773', 'Tikursew:Letmeknow@104.238.7.145:6072', 'Tikursew:Letmeknow@64.137.106.77:6570', 'Tikursew:Letmeknow@103.37.180.224:6618', 'Tikursew:Letmeknow@103.101.90.3:6268', 'Tikursew:Letmeknow@104.239.90.74:6465', 'Tikursew:Letmeknow@64.137.66.208:5793', 'Tikursew:Letmeknow@64.137.49.132:6673', 'Tikursew:Letmeknow@104.239.0.234:5935', 'Tikursew:Letmeknow@102.212.88.180:6177', 'Tikursew:Letmeknow@172.84.183.177:5737', 'Tikursew:Letmeknow@64.137.121.144:6399', 'Tikursew:Letmeknow@103.75.229.37:5785', 'Tikursew:Letmeknow@89.40.222.95:6471', 'Tikursew:Letmeknow@64.137.14.212:5878', 'Tikursew:Letmeknow@91.123.9.208:6750', 'Tikursew:Letmeknow@91.212.74.152:6518', 'Tikursew:Letmeknow@45.252.58.153:6782', 'Tikursew:Letmeknow@45.131.102.151:5803', 'Tikursew:Letmeknow@103.80.10.244:6522', 'Tikursew:Letmeknow@104.250.200.178:6428', 'Tikursew:Letmeknow@64.137.126.6:6614', 'Tikursew:Letmeknow@104.239.5.8:6662', 'Tikursew:Letmeknow@64.137.126.62:6670', 'Tikursew:Letmeknow@91.217.72.136:6865', 'Tikursew:Letmeknow@104.239.86.130:6040', 'Tikursew:Letmeknow@45.252.57.75:6520', 'Tikursew:Letmeknow@84.33.210.139:6073', 'Tikursew:Letmeknow@89.43.32.113:5941', 'Tikursew:Letmeknow@138.128.145.159:6078', 'Tikursew:Letmeknow@45.41.169.79:6740', 'Tikursew:Letmeknow@92.112.228.54:6135', 'Tikursew:Letmeknow@45.41.172.133:5876', 'Tikursew:Letmeknow@216.158.205.79:6307', 'Tikursew:Letmeknow@104.222.167.36:6438', 'Tikursew:Letmeknow@43.228.237.144:6090', 'Tikursew:Letmeknow@64.137.93.87:6544', 'Tikursew:Letmeknow@104.239.53.53:7471', 'Tikursew:Letmeknow@23.229.126.171:7700', 'Tikursew:Letmeknow@64.137.108.48:5641', 'Tikursew:Letmeknow@104.239.7.110:6514', 'Tikursew:Letmeknow@104.239.19.126:6803', 'Tikursew:Letmeknow@85.198.45.70:5994', 'Tikursew:Letmeknow@216.173.79.16:6422', 'Tikursew:Letmeknow@89.35.80.151:6806', 'Tikursew:Letmeknow@209.99.134.249:5945', 'Tikursew:Letmeknow@103.75.229.221:5969', 'Tikursew:Letmeknow@104.239.10.158:5829', 'Tikursew:Letmeknow@103.114.58.132:6553', 'Tikursew:Letmeknow@104.233.19.38:5710', 'Tikursew:Letmeknow@94.101.99.2:5551', 'Tikursew:Letmeknow@91.123.11.100:6366', 'Tikursew:Letmeknow@92.119.182.17:6662', 'Tikursew:Letmeknow@64.137.121.7:6262', 'Tikursew:Letmeknow@104.143.244.113:6061', 'Tikursew:Letmeknow@45.41.173.85:6452', 'Tikursew:Letmeknow@104.239.19.125:6802', 'Tikursew:Letmeknow@107.181.142.83:5676', 'Tikursew:Letmeknow@92.112.228.38:6119', 'Tikursew:Letmeknow@91.123.9.20:6562', 'Tikursew:Letmeknow@198.105.111.11:6689', 'Tikursew:Letmeknow@23.109.219.93:6317', 'Tikursew:Letmeknow@45.41.169.217:6878', 'Tikursew:Letmeknow@45.252.57.249:6694', 'Tikursew:Letmeknow@104.239.53.86:7504', 'Tikursew:Letmeknow@147.136.85.102:6018', 'Tikursew:Letmeknow@45.61.97.76:6602', 'Tikursew:Letmeknow@209.99.134.230:5926', 'Tikursew:Letmeknow@64.137.126.55:6663', 'Tikursew:Letmeknow@85.198.45.143:6067', 'Tikursew:Letmeknow@142.111.93.25:6586', 'Tikursew:Letmeknow@161.123.214.205:6560', 'Tikursew:Letmeknow@104.239.73.34:6577', 'Tikursew:Letmeknow@109.196.160.250:5996', 'Tikursew:Letmeknow@206.41.174.57:6012', 'Tikursew:Letmeknow@172.84.183.96:5656', 'Tikursew:Letmeknow@154.30.252.171:5302', 'Tikursew:Letmeknow@185.72.241.96:7388', 'Tikursew:Letmeknow@45.146.30.197:6701', 'Tikursew:Letmeknow@45.131.95.222:5886', 'Tikursew:Letmeknow@104.238.7.93:6020', 'Tikursew:Letmeknow@91.223.126.204:6816', 'Tikursew:Letmeknow@104.239.124.55:6333', 'Tikursew:Letmeknow@198.37.121.173:6593', 'Tikursew:Letmeknow@89.40.223.32:6068', 'Tikursew:Letmeknow@104.129.60.199:6631', 'Tikursew:Letmeknow@45.61.121.146:6745', 'Tikursew:Letmeknow@64.137.8.164:6846', 'Tikursew:Letmeknow@91.123.11.122:6388', 'Tikursew:Letmeknow@185.72.241.203:7495', 'Tikursew:Letmeknow@64.137.49.218:6759', 'Tikursew:Letmeknow@104.222.161.221:6353', 'Tikursew:Letmeknow@104.250.200.136:6386']

# Function to rotate proxies
def get_random_proxy(page_number):
    print(page_number)
    return {"http://": proxies[page_number], "https://": proxies[page_number]}



def fetch_last_page_number(base_url):
    """
    Fetch the last page number from the Codeforces problemset pagination.
    """
    scraper = cloudscraper.create_scraper()
    
    for attempt in range(2):
        response = scraper.get(base_url, proxies=get_random_proxy(30))
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

def fetch_problem_data(page_number, list_id):
    """
    Fetch problem data from a specific page and list of the Codeforces problemset.
    """
    page_url = f'https://codeforces.com/problemset/page/{page_number}?list={list_id}'
    problems = {}
    scraper = cloudscraper.create_scraper()
    connect_timeout = 10  
    read_timeout = 30  
    for attempt in range(2):
        response = scraper.get(page_url , proxies=get_random_proxy(page_number))

        if response.status_code == 403:
            print("403 Forbidden, retrying after 15 seconds...")
            time.sleep(15)
            continue

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

                        # If the problem is already in the dictionary, update the list of solved/attempted counts
                        if problem_id in problems:
                            problems[problem_id]['Stats'].append({
                                'List ID': list_id,
                                'Solved by': solved,
                                'Attempted by': tried
                            })
                        else:
                            problems[problem_id] = {
                                'Problem ID': problem_id,
                                'Stats': [{
                                    'List ID': list_id,
                                    'Solved by': solved,
                                    'Attempted by': tried
                                }]
                            }
            else:
                print('Problems table not found.')
        else:
            print(f'Failed to retrieve the page for list {list_id}. Status code: {response.status_code}')
        print(page_number, list_id)
        return problems

def fetch_problems_concurrently(list_id, last_page_number):
    """
    Fetch problems concurrently for all pages using threading.
    """
    problems = {}

    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=20) as executor:
        # Submit tasks for each page
        future_to_page = {executor.submit(fetch_problem_data, page, list_id): page for page in range(1, last_page_number + 1)}
        
        # Process results as they complete
        for future in as_completed(future_to_page):
            page_number = future_to_page[future]
            try:
                page_problems = future.result()

                # Merge the fetched problems into the main problems dictionary
                for problem_id, problem_data in page_problems.items():
                    if problem_id in problems:
                        problems[problem_id]['Stats'].extend(problem_data['Stats'])
                    else:
                        problems[problem_id] = problem_data
            except Exception as exc:
                print(f'Page {page_number} generated an exception: {exc}')
    
    return problems

def main():
    base_url = 'https://codeforces.com/problemset'
    
    # List of list IDs
    list_ids = ['49796217ba55e95a2cda9f75bc886fb0', '58207eaaf9be5ab8371212b9230b1910', '5a9ea3c5af96258e61023ad17c2467bf', '352394d6db1f747c047065746a8741a9', '9453965cd32f77f49eb00a1a463deccb', 'c91b3fefabd264880cf3b006826c1fae', '1158fe9be8f9e07a497db85cf94a0a4c', 'e68a10630c407d1f831f13fff1b82d37', '97c772021ff1a141ed4b3e06a5448d48']
    
    all_problems = {}
    last_page_number = fetch_last_page_number(base_url)
    # last_page_number = 10

    for list_id in list_ids:
        print(f"Processing list: {list_id}")
        
        # Fetch the last page number for the current list
        current_base_url = f'{base_url}?list={list_id}'
        
        # Fetch problems concurrently from all pages for the current list
        list_problems = fetch_problems_concurrently(list_id, last_page_number)

        # Merge list-specific problems into the master all_problems dictionary
        for problem_id, problem_data in list_problems.items():
            if problem_id in all_problems:
                all_problems[problem_id]['Stats'].extend(problem_data['Stats'])
            else:
                all_problems[problem_id] = problem_data
    
    # Save all the problems with unique IDs and list-specific stats to data.txt
    with open('data.txt', 'w') as file:
        file.write(json.dumps(all_problems, indent=4))

if __name__ == '__main__':
    main()
