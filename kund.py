from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class Kund:
    def __init__(self):
        self.driver = None

    def login(self, platform):
        if platform.lower() != "linkedin":
            raise ValueError("Only 'linkedin' platform is supported in this example.")

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)  # Keeps the browser open
        self.driver = webdriver.Chrome(options=options)

        self.driver.get("https://www.linkedin.com/login")
        print("Log in manually, then press Enter here to continue...")
        input()  # Wait for user to manually log in
        print("✅ Login complete")

    def go_to(self, url: str, wait_css: str = "body"):
        """Navigate and wait for a CSS selector to appear."""
        self.driver.get(url)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, wait_css))
        )

    def scrape_post_comments(self, post_url: str, max_scrolls: int = 15):
        """
        Return a list of dicts: {author, text, timestamp}
        Only grabs top-level comments (not replies).
        """
        self.go_to(post_url, "article")
        print("✅ Post loaded")

        # Open dropdown for comment sort order
        try:
            dropdown_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, "comments-sort-order-toggle__trigger")
                )
            )
            dropdown_button.click()
            print("✅ Dropdown opened")

            input("👋 Manually select 'Most recent' from dropdown, then press Enter to continue...\n")
        except Exception as e:
            print("⚠️ Failed to open dropdown")
            print("Error:", e)

        # Try to expand comments if collapsed
        try:
            comments_toggle = self.driver.find_element(
                By.CSS_SELECTOR, "button[data-control-name='comments']"
            )
            comments_toggle.click()
        except Exception:
            pass  # Already expanded or no toggle

        # Scroll to trigger comment loading
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        # Attempt to click "Load more comments"
        for _ in range(60000):
            try:
                load_more = self.driver.find_element(
                    By.XPATH, "//button[contains(., 'Load more comments')]"
                )
                self.driver.execute_script("arguments[0].click();", load_more)
                time.sleep(2)
            except Exception:
                break  # No more to load

        # Find all comment blocks
        comment_blocks = self.driver.find_elements(
            By.CSS_SELECTOR, "article.comments-comment-entity"
        )

        print(f"✅ Found {len(comment_blocks)} comment blocks")

        comments = []
        for block in comment_blocks:
            try:
                author = block.find_element(
                    By.CSS_SELECTOR, "span.comments-comment-meta__description-title"
                ).text.strip()
            except Exception:
                author = "Unknown"

            try:
                text = block.find_element(
                    By.CSS_SELECTOR, "span[dir='ltr']"
                ).text.strip()
            except Exception:
                text = ""

            try:
                timestamp = block.find_element(
                    By.TAG_NAME, "time"
                ).text.strip()
            except Exception:
                timestamp = ""

            print(f"{author} – {text[:80]}... ({timestamp})")
            comments.append(
                {"author": author, "text": text, "timestamp": timestamp}
            )

        return comments
