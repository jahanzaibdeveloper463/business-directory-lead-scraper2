# 📇 Lead Generation & Business Directory Scraper

> A high-performance web extraction pipeline designed to crawl business directories, parse commercial listing nodes, extract contact metadata, and serialize clean lead sheets directly into structured Excel workbooks (`.xlsx`). Built for B2B sales agencies, lead-generation pipelines, and market research operations.

---

## 🏗️ Pipeline Architecture
---

## 🧰 Technical Stack

- **Core Runtime:** Python 3.10+
- **HTTP Transport:** `requests` (with timeout and transport exception guards)
- **DOM Parsing:** `BeautifulSoup4` (HTML markup tree navigation)
- **Data Manipulation:** `pandas` (DataFrame memory mapping)
- **Spreadsheet Engine:** `openpyxl` (Office Open XML spreadsheet serialization)

---

## ⚡ Engineering Highlights

1. **🛡️ Resilient Transport Layer:** Implements strict connection timeouts and HTTP status verifications to prevent thread blocking on unstable directory routes.
2. **🧹 Commercial Data Normalization:** Cleans raw string attributes, truncates lengthy descriptions for clean column formatting, and maps categories into structured industry sectors.
3. **⚡ Stateless In-Memory Buffering:** Compiles scraped dictionaries directly into high-performance pandas dataframes for rapid disk I/O flushing.

---

## ⚙️ Quick Start & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/business-directory-lead-scraper.git](https://github.com/your-username/business-directory-lead-scraper.git)
   cd business-directory-lead-scraper
