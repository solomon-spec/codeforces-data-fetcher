from data import list_ids
import json
from data_processing  import fetch_problems_concurrently
from data_scraper import fetch_last_page_number

def main():
    base_url = 'https://codeforces.com/problemset'
        
    all_problems = {}
    last_page_number = fetch_last_page_number(base_url)
    # last_page_number = 10

    for list_id in range(len(list_ids)):
        print(f"Processing list: {list_id}")
        
        
        # Fetch problems concurrently from all pages for the current list
        list_problems = fetch_problems_concurrently(list_id, last_page_number)

        # Merge list-specific problems into the master all_problems dictionary
        for problem_id, problem_data in list_problems.items():
            if problem_id in all_problems:
                all_problems[problem_id]['Stats'].extend(problem_data['Stats'])
            else:
                all_problems[problem_id] = problem_data
        print(f"Processing list done: {list_id}")
        # time.sleep(60)
    
    # Save all the problems with unique IDs and list-specific stats to data.txt
    with open('data.txt', 'w') as file:
        file.write(json.dumps(all_problems, separators=(',', ':'), indent=None))

if __name__ == '__main__':
    main()
