import argparse
from pubmedapi.fetcher import fetch_pubmed_data, fetch_article_details, save_to_csv


def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    parser.add_argument("-f", "--file", type=str, help="Output file to save results.")

    args = parser.parse_args()

    pubmed_ids = fetch_pubmed_data(args.query, args.debug)
    articles = fetch_article_details(pubmed_ids, args.debug)

    if args.file:
        save_to_csv(articles, args.file)
    else:
        print("Results:")
        for article in articles:
            print(article)

if __name__ == "__main__":
    main()
