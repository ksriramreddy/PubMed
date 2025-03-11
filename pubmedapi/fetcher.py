
import requests
import csv
import xml.etree.ElementTree as ET
import re 
def fetch_pubmed_data(query, debug=False):
    
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 5  # Limit results for testing
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if debug:
        print("Debug: PubMed Search Response", data)
    
    return data.get("esearchresult", {}).get("idlist", [])


def fetch_article_details(pubmed_ids, debug=False):
    if not pubmed_ids:
        return []

    details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(details_url, params=params)

    # Parse XML response
    root = ET.fromstring(response.text)

    articles = []
    for article in root.findall(".//PubmedArticle"):
        title = article.find(".//ArticleTitle").text if article.find(".//ArticleTitle") is not None else "N/A"
        pub_date = article.find(".//PubDate/Year")
        pub_date = pub_date.text if pub_date is not None else "N/A"

        authors_list = []
        corresponding_author_email = "N/A"

        # Extract author details
        for author in article.findall(".//Author"):
            last_name = author.find("LastName")
            first_name = author.find("ForeName")
            full_name = f"{first_name.text} {last_name.text}" if first_name is not None and last_name is not None else "Unknown"
            authors_list.append(full_name)

            # Extract email from affiliation text using regex
            affiliation_info = author.find("AffiliationInfo/Affiliation")
            if affiliation_info is not None:
                affiliation_text = affiliation_info.text
                email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", affiliation_text)
                if email_match:
                    corresponding_author_email = email_match.group(0)

        articles.append({
            "PubmedID": pubmed_ids[0],
            "Title": title,
            "Publication Date": pub_date,
            "Authors": ", ".join(authors_list) if authors_list else "N/A",
            "Corresponding Author Email": corresponding_author_email
        })

    return articles

def save_to_csv(articles, filename):
    
    if not articles:
        print("No articles found to save.")
        return
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=articles[0].keys())
        writer.writeheader()
        writer.writerows(articles)
    
    print(f"Results saved to {filename}")