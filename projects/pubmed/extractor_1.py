# load libraries
import json
import requests

# set date - between 1800 and current date
pubmed_search_dates_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&mindate=1800/01/01&maxdate=2021/1/15&usehistory=y&retmode=json"
pubmed_search_post_req = requests.post(search_url)
pubmed_search_data = pubmed_search_post_req.json()
pubmed_search_webenv = pubmed_search_data["esearchresult"]['webenv']
pubmed_search_total_records = int(pubmed_search_data["esearchresult"]['count'])
pubmed_search_fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmax=9999&query_key=1&webenv=" + pubmed_search_webenv
print("Total records found : " + str(pubmed_search_total_records))

# Total records found : 31975683

# 32mn records - takes > 24 hrs on single core
for i in range(0, pubmed_search_total_records, 10000):
    fetch_url = pubmed_search_fetch_url + "&retstart=" + str(i)
    print("Getting this URL: "+ fetch_url)
    fetch_post_req = requests.post(fetch_url)
    f = open('pubmed_batch_' + str(i) + '_to_' + str(i+9999) + ".json", 'w')
    f.write(fetch_post_req.text)
    f.close()
