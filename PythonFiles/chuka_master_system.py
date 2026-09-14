"""
Chuka University Master Automation System - Enhanced Version
Single-file implementation with robust selectors
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import hashlib
import re
from datetime import datetime
from typing import Dict, List, Optional
from urllib.parse import urljoin

# ============================================
# CONFIGURATION
# ============================================

CONFIG = {
    'base_url': 'https://www.chuka.ac.ke/',
    'urls': {
        'home': 'https://www.chuka.ac.ke/',
        'academics': 'https://www.chuka.ac.ke/academics-home-page/',
        'students': 'https://www.chuka.ac.ke/students/',
        'research': 'https://www.chuka.ac.ke/research-home/',
        'vacancies': 'https://www.chuka.ac.ke/vacancies/',
        'tenders': 'https://www.chuka.ac.ke/tenders/',
        'short_courses': 'https://www.chuka.ac.ke/short-courses/',
        'library': 'https://library.chuka.ac.ke/',
        'journals': 'https://journals.chuka.ac.ke/index.php/jesar',
        'about': 'https://www.chuka.ac.ke/about/'
    },
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'timeout': 15,
    'delay': 1
}

# ============================================
# UTILITY FUNCTIONS
# ============================================

def fetch_page(url: str) -> Optional[str]:
    """Fetch webpage content with error handling"""
    try:
        headers = {'User-Agent': CONFIG['user_agent']}
        response = requests.get(url, headers=headers, timeout=CONFIG['timeout'])
        if response.status_code == 200:
            return response.text
        print(f"⚠️ Status {response.status_code} for {url}")
        return None
    except Exception as e:
        print(f"❌ Error fetching {url}: {e}")
        return None

def get_hash(text: str) -> str:
    """Generate hash for deduplication"""
    return hashlib.md5(text.encode()).hexdigest()[:16]

def extract_text(element) -> str:
    """Safely extract text from BeautifulSoup element"""
    return element.text.strip() if element else ""

def clean_text(text: str) -> str:
    """Clean text by removing extra whitespace"""
    return ' '.join(text.split()) if text else ""

def print_separator(title: str = "", char: str = "=", length: int = 80):
    """Print formatted separator"""
    if title:
        print(f"\n{char * 5} {title} {char * 5}")
    else:
        print(char * length)

# ============================================
# 1. NEWS ALERT SYSTEM - ENHANCED
# ============================================

class NewsAlertSystem:
    """Monitor and display university news"""
    
    def __init__(self):
        self.news_data = []
        
    def fetch_news(self) -> List[Dict]:
        """Fetch latest news from university website"""
        news_items = []
        
        # Try multiple pages and use generic selectors
        urls = [
            CONFIG['urls']['home'],
            CONFIG['urls']['students'],
            CONFIG['urls']['academics']
        ]
        
        for url in urls:
            html = fetch_page(url)
            if html:
                soup = BeautifulSoup(html, 'html.parser')
                items = self._extract_news_generic(soup, url)
                news_items.extend(items)
                time.sleep(CONFIG['delay'])
        
        # If no news found, try looking for any content that might be news
        if not news_items:
            html = fetch_page(CONFIG['urls']['home'])
            if html:
                soup = BeautifulSoup(html, 'html.parser')
                items = self._extract_content_as_news(soup, CONFIG['urls']['home'])
                news_items.extend(items)
        
        self.news_data = news_items
        return news_items
    
    def _extract_news_generic(self, soup, source: str) -> List[Dict]:
        """Extract news using generic selectors"""
        items = []
        
        # Try multiple selectors
        selectors = [
            'article', '.news-item', '.post', '.entry',
            '.notice', '.announcement', '.blog-post',
            '.content-item', '.entry-content', '.post-content',
            '.latest-news', '.news-list', '.news-article',
            'div[class*="news"]', 'div[class*="post"]', 'div[class*="entry"]'
        ]
        
        for selector in selectors:
            try:
                elements = soup.select(selector)
                for elem in elements:
                    # Skip if too small
                    if len(elem.text.strip()) < 20:
                        continue
                    
                    # Try to find title
                    title_elem = elem.find(['h1', 'h2', 'h3', 'h4', 'h5'])
                    title = extract_text(title_elem) if title_elem else ""
                    
                    # If no title, use first line
                    if not title:
                        lines = elem.text.strip().split('\n')
                        if lines:
                            title = clean_text(lines[0])[:100]
                    
                    # If title is too short, skip
                    if len(title) < 3:
                        continue
                    
                    # Extract date
                    date_elem = elem.find(class_=re.compile(r'date|time|published|posted'))
                    date = extract_text(date_elem) if date_elem else ""
                    
                    # Extract summary
                    summary_elem = elem.find(['p', 'div'], class_=re.compile(r'summary|excerpt|desc'))
                    summary = extract_text(summary_elem) if summary_elem else ""
                    
                    # If no summary, get first paragraph
                    if not summary:
                        p_tags = elem.find_all('p')
                        for p in p_tags:
                            text = clean_text(p.text)
                            if len(text) > 20:
                                summary = text
                                break
                    
                    # Extract link
                    link_elem = elem.find('a', href=True)
                    link = link_elem.get('href') if link_elem else ""
                    if link and not link.startswith('http'):
                        link = urljoin(CONFIG['base_url'], link)
                    
                    # Only add if we have meaningful content
                    if title and (summary or len(title) > 10):
                        items.append({
                            'title': clean_text(title),
                            'date': clean_text(date),
                            'summary': clean_text(summary[:200]),
                            'link': link,
                            'source': source,
                            'hash': get_hash(f"{title}{summary}"),
                            'type': 'news'
                        })
            except Exception as e:
                continue
        
        return items
    
    def _extract_content_as_news(self, soup, source: str) -> List[Dict]:
        """Extract any content that might be news"""
        items = []
        
        # Look for heading tags that might be news titles
        for tag in soup.find_all(['h1', 'h2', 'h3']):
            text = clean_text(tag.text)
            if text and len(text) > 5 and len(text) < 200:
                # Check if it looks like a news title
                if any(word in text.lower() for word in ['news', 'notice', 'announce', 'update', 'event', 'seminar', 'workshop', 'conference', 'deadline']):
                    # Try to find associated content
                    parent = tag.parent
                    content = ""
                    if parent:
                        # Get next sibling or paragraph
                        next_p = parent.find('p')
                        if next_p:
                            content = clean_text(next_p.text)[:200]
                    
                    items.append({
                        'title': text,
                        'date': "",
                        'summary': content,
                        'link': "",
                        'source': source,
                        'hash': get_hash(text),
                        'type': 'news'
                    })
        
        return items
    
    def get_latest_news(self, limit: int = 10) -> List[Dict]:
        """Get latest news items"""
        if not self.news_data:
            self.fetch_news()
        
        # Sort by date if available
        sorted_news = sorted(self.news_data, key=lambda x: x.get('date', ''), reverse=True)
        return sorted_news[:limit]
    
    def display_news(self, limit: int = 10):
        """Display news in terminal"""
        news = self.get_latest_news(limit)
        
        print_separator("📰 LATEST UNIVERSITY NEWS")
        if not news:
            print("  No news found on the website")
            print("  💡 Tip: The website structure may have changed")
            return
        
        for idx, item in enumerate(news, 1):
            print(f"\n{idx}. {item['title']}")
            if item['date']:
                print(f"   📅 {item['date']}")
            if item['summary']:
                print(f"   📝 {item['summary'][:100]}...")
            if item['link']:
                print(f"   🔗 {item['link']}")

# ============================================
# 2. RESEARCH TRACKER - ENHANCED
# ============================================

class ResearchTracker:
    """Track research projects and publications"""
    
    def __init__(self):
        self.research_data = []
    
    def fetch_research(self) -> List[Dict]:
        """Fetch research projects"""
        projects = []
        
        # Try research page
        html = fetch_page(CONFIG['urls']['research'])
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            items = self._extract_research_generic(soup, CONFIG['urls']['research'])
            projects.extend(items)
            time.sleep(CONFIG['delay'])
        
        # Also try home page for research mentions
        html = fetch_page(CONFIG['urls']['home'])
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            items = self._extract_research_mentions(soup, CONFIG['urls']['home'])
            projects.extend(items)
        
        self.research_data = projects
        return projects
    
    def _extract_research_generic(self, soup, source: str) -> List[Dict]:
        """Extract research using generic selectors"""
        items = []
        
        # Look for research-related content
        selectors = [
            '.research', '.project', '.publication', '.paper',
            '.journal', '.article', '.study', '.findings',
            'div[class*="research"]', 'div[class*="project"]'
        ]
        
        for selector in selectors:
            elements = soup.select(selector)
            for elem in elements:
                try:
                    # Try to find title
                    title_elem = elem.find(['h2', 'h3', 'h4'])
                    title = extract_text(title_elem) if title_elem else ""
                    
                    if title and len(title) > 5:
                        # Extract description
                        desc_elem = elem.find(['p', 'div'], class_=re.compile(r'desc|abstract|summary'))
                        description = extract_text(desc_elem) if desc_elem else ""
                        
                        if not description:
                            p_tags = elem.find_all('p')
                            for p in p_tags:
                                text = clean_text(p.text)
                                if len(text) > 20:
                                    description = text
                                    break
                        
                        items.append({
                            'title': clean_text(title),
                            'author': "Chuka University",
                            'description': clean_text(description[:300]),
                            'status': "Active",
                            'source': source,
                            'hash': get_hash(f"{title}{description}"),
                            'type': 'research'
                        })
                except Exception as e:
                    continue
        
        return items
    
    def _extract_research_mentions(self, soup, source: str) -> List[Dict]:
        """Extract research mentions from general content"""
        items = []
        
        # Look for research keywords
        for element in soup.find_all(['p', 'div', 'li']):
            text = clean_text(element.text)
            if 'research' in text.lower() and len(text) > 50:
                # Try to find a title
                title_elem = element.find_previous(['h2', 'h3', 'h4'])
                title = extract_text(title_elem) if title_elem else text[:100]
                
                if title and len(title) > 5:
                    items.append({
                        'title': clean_text(title),
                        'author': "Chuka University",
                        'description': clean_text(text[:300]),
                        'status': "Active",
                        'source': source,
                        'hash': get_hash(f"{title}{text}"),
                        'type': 'research'
                    })
        
        return items
    
    def get_research(self) -> List[Dict]:
        """Get all research projects"""
        if not self.research_data:
            self.fetch_research()
        return self.research_data
    
    def display_research(self, limit: int = 10):
        """Display research in terminal"""
        research = self.get_research()
        
        print_separator("🔬 RESEARCH PROJECTS")
        if not research:
            print("  No research projects found")
            print("  💡 Tip: Check the Research page manually")
            return
        
        print(f"\n📊 Total Projects: {len(research)}")
        
        print("\n📋 Recent Projects:")
        for idx, item in enumerate(research[:limit], 1):
            print(f"\n{idx}. {item['title']}")
            print(f"   👤 {item['author']}")
            print(f"   📊 Status: {item['status']}")
            if item['description']:
                print(f"   📝 {item['description'][:100]}...")

# ============================================
# 3. JOB NOTIFIER - ENHANCED
# ============================================

class JobNotifier:
    """Monitor job vacancies and tenders"""
    
    def __init__(self):
        self.jobs = []
        self.tenders = []
    
    def fetch_jobs(self) -> List[Dict]:
        """Fetch job vacancies"""
        jobs = []
        
        # Try multiple approaches
        urls_to_try = [
            CONFIG['urls']['vacancies'],
            CONFIG['urls']['home']
        ]
        
        for url in urls_to_try:
            html = fetch_page(url)
            if html:
                soup = BeautifulSoup(html, 'html.parser')
                items = self._extract_jobs_generic(soup, url)
                jobs.extend(items)
                time.sleep(CONFIG['delay'])
        
        # Remove duplicates
        unique_jobs = {}
        for job in jobs:
            key = job['title']
            if key not in unique_jobs:
                unique_jobs[key] = job
        
        self.jobs = list(unique_jobs.values())
        return self.jobs
    
    def _extract_jobs_generic(self, soup, source: str) -> List[Dict]:
        """Extract jobs using generic selectors"""
        items = []
        
        # Look for job-related content
        selectors = [
            '.vacancy', '.job', '.position', '.career',
            '.employment', '.opportunity', '.staff',
            'div[class*="job"]', 'div[class*="vacancy"]',
            'li'  # Also check list items
        ]
        
        job_keywords = ['vacancy', 'position', 'job', 'career', 'employment', 'opportunity', 'apply', 'deadline']
        
        for selector in selectors:
            elements = soup.select(selector)
            for elem in elements:
                text = clean_text(elem.text)
                
                # Check if it looks like a job
                if any(keyword in text.lower() for keyword in job_keywords) and len(text) > 30:
                    # Try to find title
                    title_elem = elem.find(['h2', 'h3', 'h4', 'strong'])
                    title = extract_text(title_elem) if title_elem else ""
                    
                    if not title:
                        # Use first line as title
                        lines = text.split('\n')
                        if lines:
                            title = clean_text(lines[0])
                    
                    if title and len(title) > 3:
                        # Look for deadline
                        deadline_match = re.search(r'deadline|closing.*date', text, re.IGNORECASE)
                        deadline = ""
                        if deadline_match:
                            # Extract date pattern
                            date_match = re.search(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', text)
                            if date_match:
                                deadline = date_match.group()
                        
                        items.append({
                            'title': title,
                            'department': "Chuka University",
                            'deadline': deadline if deadline else "Not specified",
                            'description': text[:300],
                            'hash': get_hash(title),
                            'type': 'job'
                        })
        
        return items
    
    def fetch_tenders(self) -> List[Dict]:
        """Fetch tender notices"""
        tenders = []
        
        html = fetch_page(CONFIG['urls']['tenders'])
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            items = self._extract_tenders_generic(soup, CONFIG['urls']['tenders'])
            tenders.extend(items)
        
        # Also check home page for tenders
        html = fetch_page(CONFIG['urls']['home'])
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            items = self._extract_tenders_generic(soup, CONFIG['urls']['home'])
            tenders.extend(items)
        
        # Remove duplicates
        unique_tenders = {}
        for tender in tenders:
            key = tender['title']
            if key not in unique_tenders:
                unique_tenders[key] = tender
        
        self.tenders = list(unique_tenders.values())
        return self.tenders
    
    def _extract_tenders_generic(self, soup, source: str) -> List[Dict]:
        """Extract tenders using generic selectors"""
        items = []
        
        # Look for tender-related content
        selectors = [
            '.tender', '.procurement', '.supply',
            'div[class*="tender"]', 'div[class*="procurement"]'
        ]
        
        tender_keywords = ['tender', 'procurement', 'supply', 'bid', 'quotation', 'proposal']
        
        for selector in selectors:
            elements = soup.select(selector)
            for elem in elements:
                text = clean_text(elem.text)
                
                if any(keyword in text.lower() for keyword in tender_keywords) and len(text) > 30:
                    title_elem = elem.find(['h2', 'h3', 'h4', 'strong'])
                    title = extract_text(title_elem) if title_elem else text[:100]
                    
                    if title and len(title) > 3:
                        # Look for reference number
                        ref_match = re.search(r'ref|no\.|number[:\s]+([A-Z0-9-]+)', text, re.IGNORECASE)
                        reference = ref_match.group(1) if ref_match else "Not specified"
                        
                        # Look for closing date
                        closing_match = re.search(r'closing|deadline.*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})', text, re.IGNORECASE)
                        closing_date = closing_match.group(1) if closing_match else "Not specified"
                        
                        items.append({
                            'title': title,
                            'reference': reference,
                            'closing_date': closing_date,
                            'hash': get_hash(title),
                            'type': 'tender'
                        })
        
        return items
    
    def get_listings(self) -> Dict:
        """Get all job and tender listings"""
        if not self.jobs:
            self.jobs = self.fetch_jobs()
        if not self.tenders:
            self.tenders = self.fetch_tenders()
        
        return {
            'jobs': self.jobs,
            'tenders': self.tenders
        }
    
    def display_listings(self):
        """Display job and tender listings"""
        listings = self.get_listings()
        
        print_separator("💼 JOB VACANCIES")
        if listings['jobs']:
            for idx, job in enumerate(listings['jobs'][:10], 1):
                print(f"\n{idx}. {job['title']}")
                if job['deadline']:
                    print(f"   📅 Deadline: {job['deadline']}")
                if job['description']:
                    print(f"   📝 {job['description'][:100]}...")
        else:
            print("  No job vacancies found")
        
        print_separator("📋 TENDER NOTICES")
        if listings['tenders']:
            for idx, tender in enumerate(listings['tenders'][:10], 1):
                print(f"\n{idx}. {tender['title']}")
                print(f"   📄 Reference: {tender['reference']}")
                print(f"   📅 Closing: {tender['closing_date']}")
        else:
            print("  No tender notices found")

# ============================================
# 4. ANALYTICS DASHBOARD
# ============================================

class AnalyticsDashboard:
    """Generate analytics and statistics"""
    
    def __init__(self, news_system, research_tracker, job_notifier):
        self.news = news_system
        self.research = research_tracker
        self.jobs = job_notifier
    
    def get_statistics(self) -> Dict:
        """Get comprehensive statistics"""
        news_count = len(self.news.news_data) if self.news.news_data else 0
        research_count = len(self.research.research_data) if self.research.research_data else 0
        job_count = len(self.jobs.jobs) if self.jobs.jobs else 0
        tender_count = len(self.jobs.tenders) if self.jobs.tenders else 0
        
        return {
            'total_news': news_count,
            'total_research': research_count,
            'total_jobs': job_count,
            'total_tenders': tender_count,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def display_dashboard(self):
        """Display analytics dashboard"""
        stats = self.get_statistics()
        
        print_separator("📊 ANALYTICS DASHBOARD")
        
        print("\n📈 DATA SUMMARY:")
        print(f"   📰 Total News Items: {stats['total_news']}")
        print(f"   🔬 Total Research Projects: {stats['total_research']}")
        print(f"   💼 Total Job Vacancies: {stats['total_jobs']}")
        print(f"   📋 Total Tender Notices: {stats['total_tenders']}")
        
        print(f"\n🔄 Last Updated: {stats['last_updated']}")

# ============================================
# 5. COURSE INFORMATION SYSTEM - ENHANCED
# ============================================

class CourseInformationSystem:
    """Extract and display course information"""
    
    def __init__(self):
        self.courses = []
    
    def fetch_courses(self) -> List[Dict]:
        """Fetch course information"""
        courses = []
        
        # Try multiple sources
        urls_to_try = [
            CONFIG['urls']['academics'],
            CONFIG['urls']['short_courses'],
            CONFIG['urls']['home']
        ]
        
        for url in urls_to_try:
            html = fetch_page(url)
            if html:
                soup = BeautifulSoup(html, 'html.parser')
                items = self._extract_courses_generic(soup, url)
                courses.extend(items)
                time.sleep(CONFIG['delay'])
        
        # Remove duplicates
        unique_courses = {}
        for course in courses:
            key = course['title'][:30]
            if key not in unique_courses:
                unique_courses[key] = course
        
        self.courses = list(unique_courses.values())
        return self.courses
    
    def _extract_courses_generic(self, soup, source: str) -> List[Dict]:
        """Extract courses using generic selectors"""
        courses = []
        
        # Look for course-related content
        selectors = [
            '.course', '.program', '.curriculum', '.degree',
            '.diploma', '.certificate', '.module',
            'div[class*="course"]', 'div[class*="program"]',
            'div[class*="academic"]', 'div[class*="study"]'
        ]
        
        course_keywords = ['course', 'program', 'degree', 'diploma', 'certificate', 
                          'bachelor', 'master', 'phd', 'module', 'unit']
        
        for selector in selectors:
            elements = soup.select(selector)
            for elem in elements:
                text = clean_text(elem.text)
                
                # Check if it's course-related
                if any(keyword in text.lower() for keyword in course_keywords):
                    # Try to find title
                    title_elem = elem.find(['h2', 'h3', 'h4', 'strong'])
                    title = extract_text(title_elem) if title_elem else ""
                    
                    if not title:
                        # Use first line as title
                        lines = text.split('\n')
                        if lines:
                            title = clean_text(lines[0])
                    
                    if title and len(title) > 3:
                        # Extract description
                        description = ""
                        for p in elem.find_all(['p', 'li']):
                            p_text = clean_text(p.text)
                            if len(p_text) > 20 and p_text != title:
                                description += p_text + " "
                        
                        if not description:
                            description = text[:200]
                        
                        courses.append({
                            'title': clean_text(title),
                            'description': clean_text(description[:500]),
                            'source': source,
                            'hash': get_hash(f"{title}{description}")
                        })
        
        return courses
    
    def get_courses(self) -> List[Dict]:
        """Get all courses"""
        if not self.courses:
            self.fetch_courses()
        return self.courses
    
    def search_courses(self, keyword: str) -> List[Dict]:
        """Search courses by keyword"""
        courses = self.get_courses()
        keyword_lower = keyword.lower()
        results = []
        
        for course in courses:
            search_text = f"{course.get('title', '')} {course.get('description', '')}".lower()
            if keyword_lower in search_text:
                results.append(course)
        
        return results
    
    def display_courses(self, limit: int = 10, search_keyword: str = None):
        """Display course information"""
        if search_keyword:
            courses = self.search_courses(search_keyword)
            print_separator(f"🔍 COURSES MATCHING: '{search_keyword}'")
        else:
            courses = self.get_courses()
            print_separator("📚 COURSE INFORMATION")
        
        if not courses:
            print("  No courses found")
            return
        
        print(f"\n📊 Total Courses: {len(courses)}")
        
        print("\n📋 Courses:")
        for idx, course in enumerate(courses[:limit], 1):
            print(f"\n{idx}. {course['title']}")
            if course['description'] and len(course['description']) > 10:
                print(f"   📝 {course['description'][:150]}...")

# ============================================
# MAIN EXECUTION
# ============================================

def main():
    """Main function to run all systems"""
    
    print("=" * 80)
    print("🎓 CHUKA UNIVERSITY MASTER AUTOMATION SYSTEM")
    print("=" * 80)
    print(f"🕐 System Run: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🌐 Source: Chuka University Website")
    print("=" * 80)
    
    # Initialize all systems
    print("\n⏳ Initializing systems and fetching data...")
    
    news_system = NewsAlertSystem()
    research_system = ResearchTracker()
    job_system = JobNotifier()
    course_system = CourseInformationSystem()
    
    # Fetch data
    print("📥 Fetching data from university website...")
    news_system.fetch_news()
    research_system.fetch_research()
    job_system.fetch_jobs()
    job_system.fetch_tenders()
    course_system.fetch_courses()
    
    # Initialize analytics
    analytics = AnalyticsDashboard(news_system, research_system, job_system)
    
    # Display all systems
    print("\n" + "=" * 80)
    news_system.display_news(limit=5)
    
    print("\n" + "=" * 80)
    research_system.display_research(limit=5)
    
    print("\n" + "=" * 80)
    job_system.display_listings()
    
    print("\n" + "=" * 80)
    analytics.display_dashboard()
    
    print("\n" + "=" * 80)
    course_system.display_courses(limit=5)
    
    # Summary
    print("\n" + "=" * 80)
    print("✅ SYSTEM EXECUTION COMPLETE")
    
    # Quick summary of findings
    total_news = len(news_system.news_data)
    total_research = len(research_system.research_data)
    total_jobs = len(job_system.jobs)
    total_tenders = len(job_system.tenders)
    total_courses = len(course_system.courses)
    
    print(f"\n📊 SUMMARY:")
    print(f"   📰 News items fetched: {total_news}")
    print(f"   🔬 Research projects: {total_research}")
    print(f"   💼 Job vacancies: {total_jobs}")
    print(f"   📋 Tender notices: {total_tenders}")
    print(f"   📚 Courses found: {total_courses}")
    
    print("\n" + "=" * 80)
    print("🏁 Done!")

if __name__ == "__main__":
    main()