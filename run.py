from kund import Kund
import csv
import os

BATCH_SIZE = 200
OUTPUT_FILE = "comments.csv"

# Create file and write header if doesn't exist
if not os.path.exists(OUTPUT_FILE):
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["author", "text", "timestamp"])
        writer.writeheader()

k = Kund()
k.login("linkedin")

post_url = "https://www.linkedin.com/posts/tyler-j-leinenbach-106667223_looking-for-an-internship-this-fall-or-spring-activity-7198644506865397762-vpeh/?utm_source=share&utm_medium=member_desktop&rcm=ACoAADJnFLcBChSL6nTyBIUw4-iQFPwcCgDKaCg"

total_scraped = 0

try:
    for batch in k.scrape_post_comments(post_url, batch_size=BATCH_SIZE):
        with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["author", "text", "timestamp"])
            writer.writerows(batch)
        total_scraped += len(batch)
        print(f"📦 Batch saved ({len(batch)}), total so far: {total_scraped}")

except KeyboardInterrupt:
    print("\n⛔ Interrupted by user. All scraped data has been saved.")
except Exception as e:
    print(f"\n⚠️ Error occurred: {e}. Data up to this point has been saved.")
finally:
    print(f"✅ Finished with {total_scraped} total comments saved to {OUTPUT_FILE}")
