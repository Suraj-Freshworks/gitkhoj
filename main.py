import requests
import csv
import time
from colorama import Fore
import argparse


parser = argparse.ArgumentParser(description='Github search')
parser.add_argument('-t', '--token', type=str, help="auth_token", required=True)
# parser.add_argument('-v', '--verbose', required=False, help="verbose messages")
parser.add_argument('-f','--filename', type=argparse.FileType('r'), help="file with absolute path containing multiple queries. Only one query should be in one line.")
parser.add_argument('-o', '--output', type=str, required=False, default="github-scan", help="output filename")
parser.add_argument('-q','--queries')
args = parser.parse_args()

if args.filename is None and args.queries is None:
   parser.error("at least one of --filename and --queries is required...")



headers = {
              'Accept': 'application/vnd.github+json',
              'Authorization': 'Bearer ' + args.token,
              'X-GitHub-Api-Version': '2022-11-28'
        }

def create_query():
    
    search_terms = []
    orgs = []
    final_queries = []
    if args.filename:
        with args.filename as f:
            for search_term in f:
                search_terms.append(search_term)
    
    elif args.queries:
        search_terms = [query for query in args.queries.split(',')]


    url = "https://api.github.com/user/orgs?per_page=100"
    response = requests.request("GET", url, headers=headers).json()
    print(response)

    for records in response:    
        name = orgs.append(records['login'].strip())
        print(name)

    for org in orgs:
        tmp = ["org:"+org+"%20"+search_term.strip() for search_term in search_terms]
        final_queries.extend(tmp)

    return final_queries
# print(final_queries)



def fetch_github_results(url, params=None, headers=None, results=None):
    if results is None:
        results = []

    time.sleep(7)
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    results.extend(data['items'])  

    # Check if there's a next page
    if 'next' in response.links:
        next_url = response.links['next']['url']
        fetch_github_results(next_url, headers=headers, results=results)

    return results

final_queries = create_query()
print(final_queries)

def main():
    count = 0
    with open(args.output+".csv",mode='w') as scanoutput:
        fieldname = ["S.No.","Org", "Repo/Filepath", "URL"]
        writer = csv.DictWriter(scanoutput, fieldnames=fieldname)
        writer.writeheader()
        for query in final_queries: 
            url = f"https://api.github.com/search/code?q={query}&per_page=100&page=1"
            results = fetch_github_results(url, headers=headers)
            for result in results:
                    writer.writerow({"S.No.":f"{count+1}","Org":f"{result['repository']['owner']['login']}", "Repo/Filepath": f"{result['path']}" , "URL":f"{result['html_url']}"})
                    print(f"{Fore.RED}Result {count+1} for {query}: {result['repository']['owner']['login']}  {result['path']}  {result['html_url']}{Fore.WHITE}")
                    count+=1
    print(f"{Fore.RED}{count} results are found.{Fore.WHITE}")

if __name__ == "__main__":
    main()
