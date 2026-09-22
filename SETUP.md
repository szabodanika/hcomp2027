# HCOMP 2027 Website - Setup Complete

## ✅ What Was Done

Your HCOMP website has been successfully compiled into a proper project structure:

### New Structure
- **`public/`** - Complete static website ready to serve
  - 14 HTML pages (index, attend, program, organizers, etc.)
  - CSS files (Bootstrap, custom styles)
  - JavaScript (navbar interaction)
  - Images and logos
  
- **`_archived_exports/`** - Original downloaded HTML exports preserved for reference
  - All original .html files
  - Associated _files directories with resources

### Project Files
- `package.json` - Project metadata with npm scripts
- `README.md` - Documentation
- `.gitignore` - Git configuration
- `extract_pages.py` - Python script for extracting content from exported pages (archived)

## 🚀 Running the Site

### Option 1: Quick Start (Node/npm)
```bash
npm start
```
Opens site at `http://localhost:8000`

### Option 2: Python
```bash
cd public
python3 -m http.server 8000
```

### Option 3: Direct File Access
Open `public/index.html` in your browser

## 📄 Pages Available

- **index.html** - Home page with overview and navigation
- **attend.html** - Attendance main page
- **program.html** - Conference program
- **submit.html** - Call for Participation
- **sponsors.html** - Sponsorship opportunities
- **organizers.html** - Organizer profiles
- **registration.html** - Registration info
- **venue.html** - Venue details
- **accommodations.html** - Hotel information
- **travel-grants.html** - Travel grant details
- **student-volunteers.html** - Volunteer opportunities
- **crowdcamp.html** - CrowdCamp workshop info
- **code-of-conduct.html** - Code of Conduct
- **visa.html** - Visa support letter info
- **past-meetings.html** - Previous HCOMP conferences

## 🎨 Customization

- **Colors**: Edit `:root` variables in `public/index.html` and `public/template.html`
- **Fonts**: Linked from Google Fonts (modify in `<head>`)
- **Styles**: `public/css/landing-page.css` and `public/css/components.css`

## 📦 Deployment

The `public/` folder contains everything needed. Upload it to any static hosting:
- Netlify, Vercel, GitHub Pages
- Any web server (Apache, Nginx, etc.)
- AWS S3 + CloudFront
- Any CDN

## 🔄 Updating Content

If you need to update content, either:
1. Edit the HTML files directly in `public/`
2. Or use `extract_pages.py` with new exported files

## 📋 Notes

- All pages share consistent styling and navigation
- Responsive design works on mobile/tablet/desktop
- Bootstrap 5 grid system for layouts
- Font Awesome icons available for use
- Announcement banner at top (edit in page files)

---

**Ready to deploy!** The site is production-ready and can be hosted immediately.
