import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

def fetch_page(url):
    """Fetch page with proper headers and error handling"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching {url}: {e}")
        return None

def extract_all_headings(html):
    """Extract all types of headings"""
    soup = BeautifulSoup(html, 'html.parser')
    
    # Look for all heading tags
    heading_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    headings = {}
    
    for tag in heading_tags:
        elements = soup.find_all(tag)
        if elements:
            headings[tag] = [elem.text.strip() for elem in elements if elem.text.strip()]
    
    return headings

def extract_links(html, base_url):
    """Extract and categorize links"""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    
    for tag in soup.find_all('a', href=True):
        href = tag.get('href')
        if href.startswith('#'):
            continue  # Skip anchor links
            
        # Convert relative URLs to absolute
        absolute_url = urljoin(base_url, href)
        
        # Get link text
        text = tag.text.strip()
        
        links.append({
            'url': absolute_url,
            'text': text[:50] + '...' if len(text) > 50 else text,
            'type': 'internal' if absolute_url.startswith(base_url) else 'external'
        })
    
    return links

def extract_navigation_links(html):
    """Extract navigation/menu items specifically"""
    soup = BeautifulSoup(html, 'html.parser')
    
    # Common navigation selectors
    nav_selectors = [
        'nav a',
        '.menu-item a',
        '.nav-menu a',
        '.navigation a',
        '.navbar a',
        '.main-nav a'
    ]
    
    nav_links = []
    for selector in nav_selectors:
        elements = soup.select(selector)
        for elem in elements:
            href = elem.get('href')
            text = elem.text.strip()
            if href and text:
                nav_links.append({
                    'text': text,
                    'url': href
                })
    
    return nav_links

def scrape_chuka_university():
    """Main scraping function"""
    base_url = "https://www.chuka.ac.ke/"
    
    print("🔍 Scraping Chuka University Website")
    print("=" * 50)
    
    # Fetch homepage
    html = fetch_page(base_url)
    if not html:
        return
    
    # 1. Extract all headings
    print("\n📌 HEADINGS FOUND:")
    headings = extract_all_headings(html)
    for tag, content in headings.items():
        if content:
            print(f"\n{tag.upper()} tags ({len(content)}):")
            for idx, heading in enumerate(content[:5], 1):  # Show first 5
                print(f"  {idx}. {heading}")
    
    # 2. Extract navigation links
    print("\n🧭 NAVIGATION LINKS:")
    nav_links = extract_navigation_links(html)
    if nav_links:
        for idx, link in enumerate(nav_links[:10], 1):  # Show first 10
            print(f"  {idx}. {link['text']} -> {link['url']}")
    else:
        print("  No navigation links found using common selectors")
    
    # 3. Extract all links with categorization
    print("\n🔗 ALL LINKS SUMMARY:")
    all_links = extract_links(html, base_url)
    
    internal_links = [l for l in all_links if l['type'] == 'internal']
    external_links = [l for l in all_links if l['type'] == 'external']
    
    print(f"  Internal links: {len(internal_links)}")
    print(f"  External links: {len(external_links)}")
    
    # Show some important internal links
    print("\n🔗 IMPORTANT INTERNAL LINKS:")
    important_sections = ['admission', 'academic', 'student', 'portal', 'courses', 'research']
    important_links = []
    
    for link in internal_links:
        url_lower = link['url'].lower()
        if any(section in url_lower for section in important_sections):
            important_links.append(link)
    
    if important_links:
        for link in important_links[:10]:
            print(f"  • {link['text']}")
            print(f"    → {link['url']}")
    else:
        print("  No specific important links found")
    
    # 4. Try to fetch key pages (with delay to avoid rate limiting)
    print("\n📄 FETCHING KEY PAGES:")
    key_pages = [
        '/admissions/',
        '/academics/',
        '/students/',
        '/research/',
        '/about/'
    ]
    
    for page in key_pages:
        full_url = urljoin(base_url, page)
        print(f"\n  Attempting: {full_url}")
        
        # Add delay to be respectful to the server
        time.sleep(1)
        
        page_html = fetch_page(full_url)
        if page_html:
            soup = BeautifulSoup(page_html, 'html.parser')
            title = soup.title.string if soup.title else "No title"
            print(f"  ✅ Page loaded: {title[:50]}...")
            
            # Get some content preview
            paragraphs = soup.find_all('p')
            if paragraphs:
                preview = paragraphs[0].text[:100] if paragraphs else ""
                print(f"  📝 Preview: {preview}...")
        else:
            print(f"  ❌ Could not load page")

# Run the scraper
if __name__ == "__main__":
    scrape_chuka_university()
    print("\n" + "=" * 50)
    print("✅ Scraping complete!")