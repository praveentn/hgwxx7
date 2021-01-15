#!pip install biopython

# load libraries
from Bio import Entrez

# always tell PubMed who you're
Entrez.email = "sigmoidpth@gmail.com"

# sample search 
handle = Entrez.esearch(db="pubmed", term="biopython[title]", retmax="40" )
record = Entrez.read(handle)

record["IdList"]
# ['22909249', '19304878']

# search based on specific term (treatment)
search_results = Entrez.read(
    Entrez.esearch(
        db="pubmed", term="treatment", reldate=365, datetype="pdat", usehistory="y"
    )
)
count = int(search_results["Count"])
print("Found %i results" % count)

batch_size = 10
out_handle = open("recent_orchid_papers.txt", "w")
for start in range(0, count, batch_size):
    end = min(count, start + batch_size)
    print("Going to download record %i to %i" % (start + 1, end))
    fetch_handle = Entrez.efetch(
        db="pubmed",
        rettype="medline",
        retmode="text",
        retstart=start,
        retmax=batch_size,
        webenv=search_results["WebEnv"],
        query_key=search_results["QueryKey"],
    )
    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)
out_handle.close()

# Found 478918 results
# Going to download record 1 to 10
# Going to download record 11 to 20
# Going to download record 21 to 30
# Going to download record 31 to 40

