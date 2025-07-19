# run.py

from kund import Kund
import csv
if __name__ == "__main__":
    k = Kund()
    k.login("linkedin")  # opens browser, you log in manually, then press Enter

    post_url = "https://www.linkedin.com/posts/samchenmedia_post-closed-%F0%9D%9F%91%F0%9D%9F%8E%F0%9D%9F%8E-%F0%9D%90%88%F0%9D%90%A7%F0%9D%90%AD%F0%9D%90%9E%F0%9D%90%AB%F0%9D%90%A7%F0%9D%90%AC%F0%9D%90%A1-activity-7186026879244472320-CU25/?utm_source=share&utm_medium=member_desktop&rcm=ACoAADJnFLcBChSL6nTyBIUw4-iQFPwcCgDKaCg"
    comments = k.scrape_post_comments(post_url)

    print(f"\nTotal comments scraped: {len(comments)}\n")
    for c in comments:
        print(f"{c['author']} – {c['text'][:80]}...  ({c['timestamp']})")
    
    with open("2k-comments.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["author", "text", "timestamp"])
        writer.writeheader()
        writer.writerows(comments)
