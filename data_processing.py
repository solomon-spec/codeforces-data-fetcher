from concurrent.futures import ThreadPoolExecutor, as_completed
from data_scraper import fetch_problem_data


def fetch_problems_concurrently(list_id, last_page_number):
    """
    Fetch problems concurrently for all pages using threading.
    """
    problems = {}

    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=98) as executor:
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