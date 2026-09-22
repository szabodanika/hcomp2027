#!/usr/bin/env python3
"""Extract page content from downloaded HCOMP HTML files and generate clean pages."""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

# Page mapping: filename -> (output_filename, page_title)
PAGES = {
    "Attend.html": ("attend.html", "Attend"),
    "Accommodations.html": ("accommodations.html", "Accommodations"),
    "Call for Participation.html": ("submit.html", "Call for Participation"),
    "Call for Sponsors.html": ("sponsors.html", "Call for Sponsors"),
    "Code of Conduct.html": ("code-of-conduct.html", "Code of Conduct"),
    "CrowdCamp.html": ("crowdcamp.html", "CrowdCamp"),
    "Organizers.html": ("organizers.html", "Organizers"),
    "Past Meetings.html": ("past-meetings.html", "Past Meetings"),
    "Program.htm": ("program.html", "Program"),
    "Registration.html": ("registration.html", "Registration"),
    "Student Volunteers.html": ("student-volunteers.html", "Student Volunteers"),
    "Travel Grants.html": ("travel-grants.html", "Travel Grants"),
    "Venue.htm": ("venue.html", "Venue"),
    "Visa Support Letter.html": ("visa.html", "Visa Support Letter"),
}

ROOT_DIR = Path(__file__).parent
PUBLIC_DIR = ROOT_DIR / "public"
PAGES_DIR = PUBLIC_DIR / "pages"

# Load template
with open(PUBLIC_DIR / "template.html", "r") as f:
    TEMPLATE = f.read()

def extract_main_content(html_content):
    """Extract main content from HTML file."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find main content area
    page_content = soup.find('div', class_='page-content')
    if not page_content:
        # Try alternative selectors
        page_content = soup.find('div', class_='container')

    if page_content:
        # Clean up internal style references
        for script in page_content.find_all('script'):
            script.decompose()
        return str(page_content)

    return "<p>Content extraction failed</p>"

def generate_page(input_file, output_file, page_title):
    """Generate a clean HTML page from exported content."""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        content = extract_main_content(html_content)

        # Generate page
        page_html = TEMPLATE.replace("{{PAGE_TITLE}}", page_title + " - HCOMP 2026")
        page_html = page_html.replace("{{CONTENT}}", content)

        # Write output
        output_path = PUBLIC_DIR / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(page_html)

        print(f"✓ Generated {output_file}")
        return True
    except Exception as e:
        print(f"✗ Failed to generate {output_file}: {str(e)}")
        return False

def main():
    """Process all pages."""
    print("Extracting HCOMP pages...")
    success_count = 0

    for input_name, (output_file, page_title) in PAGES.items():
        input_path = ROOT_DIR / input_name
        if input_path.exists():
            if generate_page(input_path, output_file, page_title):
                success_count += 1
        else:
            print(f"⚠ Input file not found: {input_name}")

    print(f"\nCompleted: {success_count}/{len(PAGES)} pages generated")

if __name__ == "__main__":
    main()
