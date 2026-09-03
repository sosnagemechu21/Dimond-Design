# Diamond Design — Dagim Portfolio & Resume

A modern, high-converting resume and portfolio web application built for **Dagim** ([Diamond Design](https://diamond-design-dagi.lovable.app)) using **Django**, inspired by the visual aesthetics and interactive experience of [kidus.pro.et](https://kidus.pro.et/).

![Diamond Design Portfolio](resume/static/resume/img/portrait.png)

---

## ✨ Features

- **Hero Section & 3D Interactive Orbit Physics**:
  - Dark luxury theme (`#0C0C0C`) with slate charcoal and metallic silver ambient tones.
  - Interactive 3D drag-to-spin orbital tokens with depth blur, perspective scaling, and momentum physics.
  - Studio portrait with bottom gradient mask.
- **Dual-Row Infinite Moving Marquee Ticker**:
  - Continuous animated displays of client works and core branding principles.
- **About Me Section & Live Stat Counters**:
  - `80+` Brands Shipped, `48h` Signature Turnaround, `100%` Vector Editable Files, `5.0★` Rating.
- **Expertise Section (Kidus High-Contrast Luxury)**:
  - Numbered capabilities (`01`, `02`, `03`, `04`) with interactive skill tag pills.
- **Signature Stacking Cards Showcase**:
  - Sticky project card deck with dual-column media layout (stacked detail thumbnails + full showcase).
  - High-resolution modal image lightbox.
- **48-Hour Signature Branding Service**:
  - 10-deliverable checklist + 4-step workflow.
- **Embedded In-Site Google Form**:
  - Fill and submit the branding questionnaire directly on the site via interactive full-screen modal or on-page framed section without leaving the website.
- **Direct Contact & Django Backend**:
  - Direct WhatsApp chat link, Instagram handle, and asynchronous Django contact form.
  - Fully manageable through the Django Admin dashboard.

---

## 🚀 Quick Start

### 1. Clone & Set Up Virtual Environment
```bash
git clone https://github.com/sosnagemechu21/Dimond-Design.git
cd Dimond-Design

python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Migrations & Seed Portfolio
```bash
python manage.py migrate
python manage.py seed_portfolio
```

### 4. Start Development Server
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser!

---

## 🛠 Tech Stack

- **Backend**: Python 3, Django 6.x
- **Database**: SQLite (built-in)
- **Frontend**: HTML5, Vanilla CSS3 (custom responsive styling), Vanilla JavaScript
- **Typography**: Space Grotesk, Plus Jakarta Sans
