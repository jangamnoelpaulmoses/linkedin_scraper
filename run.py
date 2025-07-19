# run.py

from kund import Kund
import csv
if __name__ == "__main__":
    k = Kund()
    k.login("linkedin")  # opens browser, you log in manually, then press Enter

    post_url = "https://www.linkedin.com/posts/tyler-j-leinenbach-106667223_looking-for-an-internship-this-fall-or-spring-activity-7198644506865397762-vpeh/?utm_source=share&utm_medium=member_desktop&rcm=ACoAADJnFLcBChSL6nTyBIUw4-iQFPwcCgDKaCg"
    comments = k.scrape_post_comments(post_url)

    print(f"\nTotal comments scraped: {len(comments)}\n")
    for c in comments:
        print(f"{c['author']} – {c['text'][:80]}...  ({c['timestamp']})")
    
    with open("6k-comments.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["author", "text", "timestamp"])
        writer.writeheader()
        writer.writerows(comments)
