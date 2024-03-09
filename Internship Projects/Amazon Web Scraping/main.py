import asyncio
from playwright.sync_api import sync_playwright

SBR_WS_CDP = 'wss://brd-customer-hl_e587241a-zone-scraping_browser:xjel1t9a46hh@brd.superproxy.io:9222'

def main():
    with sync_playwright() as pw:
        print('connecting')

        for page_num in range(1, 3):
            browser = pw.chromium.connect_over_cdp(SBR_WS_CDP)



main()