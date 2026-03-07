import argparse
import re
import time
from playwright.sync_api import sync_playwright

# definicao dos argumentos necessarios para funcionamento do codigo
parser = argparse.ArgumentParser()
parser.add_argument("--index", required=True)
parser.add_argument("--term", required=True)
args = parser.parse_args()

url_inicial = f"https://web.archive.org/web/2/http://orkut.google.com/l-{args.index}.html" # url do acervo 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page() # abre aba

    page.set_default_timeout(180000)

    page.goto(url_inicial, wait_until="domcontentloaded")

    while True:
        
        print("SCANNED:", page.url)

        text = page.content()
        if re.search(rf"\b{re.escape(args.term)}\b", text, re.IGNORECASE): # garante que a palavra seja encontrada de forma inteira e não aglutinada, ignora case
            print(f"FOUND [{args.term}] IN ->", page.url)

        next_btn = page.locator("a.paginationSeparator:has-text('next')")
        if next_btn.count() == 0:
            break

        next_btn.first.click()
        page.wait_for_load_state("networkidle")

    browser.close()
