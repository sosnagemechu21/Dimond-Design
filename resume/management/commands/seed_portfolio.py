from django.core.management.base import BaseCommand
from resume.models import (
    Profile,
    Expertise,
    Project,
    PosterDesign,
    BrandBoardDeliverable,
    WorkStep
)

class Command(BaseCommand):
    help = 'Seeds database with Dagim / Diamond Design portfolio and resume data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Seeding portfolio data..."))

        # 1. Profile
        Profile.objects.all().delete()
        profile = Profile.objects.create(
            name="Dagim",
            brand_name="Diamond Design",
            title="Brand Identity & Social Media Designer",
            hero_headline="HI, I'M DAGIM",
            hero_subtext="A brand identity & social media designer, shipping complete brand systems in 48 hours.",
            hero_punchline="One Brand Board. Everything your brand needs.",
            hero_description="A studio for brand identity and social media content. Don't let the name fool you — Diamond Design delivers everything you need to launch professionally, all summarized on a single, easy-to-use brand board.",
            about_heading="A studio built for founders in a hurry.",
            about_text="I help early-stage founders and small businesses launch with a real, cohesive brand — not a template. Every project is delivered on a single, useful brand board so your team can actually use it on day one.",
            brands_shipped_count="80+",
            delivery_time="48h",
            satisfaction_rate="100%",
            whatsapp_number="+251984670908",
            whatsapp_display="0984 670 908",
            instagram_handle="@dymndesign12",
            instagram_url="https://instagram.com/dymndesign12",
            booking_form_url="",
            embedded_form_url="",
            email="dymndesign12@gmail.com",
            portrait_image="resume/img/portrait.png"
        )
        self.stdout.write(self.style.SUCCESS("[OK] Profile created"))

        # 2. Expertise
        Expertise.objects.all().delete()
        expertise_data = [
            (
                "01",
                "Brand Identity & Logo Systems",
                "Designing complete visual identity systems from logo marks to unified typography and vector assets for emerging brands and founders.",
                "Primary Logo, Secondary Logo, Brand Mark, Monograms, Color Palette, Typography Hierarchy, Vector Ai / SVG, Brand Board PDF",
                1
            ),
            (
                "02",
                "Social Media & Campaign Creatives",
                "Scroll-stopping single-post and promotional campaign creatives crafted for Instagram, TikTok, and Facebook feeds with consistent brand tone.",
                "Social Media Posters, Product Launch Campaigns, Event Graphics, Story Templates, Typography Art, Brand Voice, Photoshop & Illustrator",
                2
            ),
            (
                "03",
                "48-Hour Rapid Branding Service",
                "Our signature agile branding sprint delivering an end-to-end professional brand board in 48 hours flat, built for founders who want to launch fast.",
                "48h Turnaround, 50% Milestone Deposit, Discovery Brief, One-Page Brand Board, Ready-to-Use Assets, No Template Lock-in",
                3
            ),
            (
                "04",
                "Print Collateral & Merch Mockups",
                "Tangible brand extensions from luxury printed business cards to caps, apparel, packaging, and real-world product mockups.",
                "Printed Business Cards, Apparel & Cap Mockups, Packaging Design, CMYK Prepress, Vector Mockup Systems, Stationery Systems",
                4
            )
        ]
        for num, title, desc, skills, order in expertise_data:
            Expertise.objects.create(
                number=num,
                title=title,
                description=desc,
                skills_csv=skills,
                order=order
            )
        self.stdout.write(self.style.SUCCESS(f"[OK] {len(expertise_data)} Expertise areas created"))

        # 3. Projects (Stacking Cards Showcase)
        Project.objects.all().delete()
        projects_data = [
            {
                "order": 1,
                "number": "01",
                "role": "Lead Brand Designer",
                "title": "Kalu Putics",
                "client": "Kalu Putics Boutique",
                "category": "Brand Identity",
                "year": "'26",
                "description": "Comprehensive visual identity and brand marks for an upscale lifestyle retail boutique. Includes primary emblem, modern packaging system, typographic styling, and one-page brand board.",
                "main_image": "resume/img/kalu-putics.png",
                "preview_1": "resume/img/kp-concept.png",
                "preview_2": "resume/img/kp-cap.png",
                "live_url": "https://diamond-design-dagi.lovable.app#work",
            },
            {
                "order": 2,
                "number": "02",
                "role": "Visual Identity Specialist",
                "title": "Merha Trading",
                "client": "Merha Global Trading",
                "category": "Stationery System",
                "year": "'26",
                "description": "Premium corporate stationery and brand architecture for a multinational trading corporation. Encompasses luxury business cards, letterheads, invoice templates, and official identity marks.",
                "main_image": "resume/img/merha-trading.png",
                "preview_1": "resume/img/merha-garments.png",
                "preview_2": "resume/img/brand-board-preview.png",
                "live_url": "https://diamond-design-dagi.lovable.app#work",
            },
            {
                "order": 3,
                "number": "03",
                "role": "Logo Architect",
                "title": "KP Concept",
                "client": "KP Studio",
                "category": "Logo Construction",
                "year": "'25",
                "description": "Precision geometric logo construction exploring golden-ratio geometry, negative space balance, and modular symbol scaling across digital apps and physical surfaces.",
                "main_image": "resume/img/kp-concept.png",
                "preview_1": "resume/img/kalu-putics.png",
                "preview_2": "resume/img/kp-cap.png",
                "live_url": "https://diamond-design-dagi.lovable.app#work",
            },
            {
                "order": 4,
                "number": "04",
                "role": "Brand Director & Apparel Designer",
                "title": "Dymnd Design Merch",
                "client": "Diamond Studio Merch",
                "category": "Apparel & Cap",
                "year": "'26",
                "description": "Flagship studio apparel identity and streetwear collection. Designed high-contrast embroidery patches, structured cap mockups, garment hangtags, and promotional print assets.",
                "main_image": "resume/img/dymnd-cap.png",
                "preview_1": "resume/img/kp-cap.png",
                "preview_2": "resume/img/portrait.png",
                "live_url": "https://diamond-design-dagi.lovable.app#work",
            },
            {
                "order": 5,
                "number": "05",
                "role": "Product & Merchandise Designer",
                "title": "KP Cap Collection",
                "client": "KP Headwear",
                "category": "Product Mockup",
                "year": "'25",
                "description": "Realistic 3D-styled physical product mockups and embroidery specifications for bespoke headwear and caps, delivering production-ready vector stitch files.",
                "main_image": "resume/img/kp-cap.png",
                "preview_1": "resume/img/kp-concept.png",
                "preview_2": "resume/img/kalu-putics.png",
                "live_url": "https://diamond-design-dagi.lovable.app#work",
            },
            {
                "order": 6,
                "number": "06",
                "role": "Identity Designer",
                "title": "Merha Garments",
                "client": "Merha Garments Co.",
                "category": "Brand Mark",
                "year": "'25",
                "description": "Modern minimalist brand mark combining traditional textile heritage patterns with bold, contemporary lines for a textile and garment manufacturing brand.",
                "main_image": "resume/img/merha-garments.png",
                "preview_1": "resume/img/merha-trading.png",
                "preview_2": "resume/img/brand-board-preview.png",
                "live_url": "https://diamond-design-dagi.lovable.app#work",
            },
        ]
        for p in projects_data:
            Project.objects.create(
                order=p["order"],
                number=p["number"],
                role=p["role"],
                title=p["title"],
                client=p["client"],
                category=p["category"],
                year=p["year"],
                description=p["description"],
                main_image=p["main_image"],
                preview_image_1=p["preview_1"],
                preview_image_2=p["preview_2"],
                live_url=p["live_url"],
                is_featured=True
            )
        self.stdout.write(self.style.SUCCESS(f"[OK] {len(projects_data)} Projects created"))

        # 4. Poster Designs
        PosterDesign.objects.all().delete()
        posters = [
            ("Gengjia Agri", "Product Launch", "resume/img/gengjia-1.png", "'26", 1),
            ("Gengjia Agri", "Hero Campaign", "resume/img/gengjia-2.png", "'26", 2),
            ("ICL Ethiopia", "Health Campaign", "resume/img/icl-health.webp", "'25", 3),
            ("ICL Ethiopia", "Science · Awareness", "resume/img/icl-science.webp", "'25", 4),
            ("NTO Ethiopia", "Travel · Promo", "resume/img/nto-travel.png", "'26", 5),
            ("SAT", "Product · Retail", "resume/img/sat-retail.png", "'26", 6),
        ]
        for brand, cat, img, yr, o in posters:
            PosterDesign.objects.create(
                brand=brand,
                category=cat,
                image=img,
                year=yr,
                order=o
            )
        self.stdout.write(self.style.SUCCESS(f"[OK] {len(posters)} Poster designs created"))

        # 5. Deliverables (48-Hour Brand Board)
        BrandBoardDeliverable.objects.all().delete()
        deliverables = [
            "Primary Logo",
            "Secondary Logo",
            "Brand Mark / Icon",
            "Color Palette (HEX, RGB, CMYK)",
            "Typography Selection & Pairings",
            "One-Page Brand Board (PDF)",
            "Editable Source Files (Ai, PDF, SVG, PNG)",
            "20pc Business Cards (printed)",
            "1 Social Poster Template",
            "High-Resolution Profile Icon"
        ]
        for idx, item in enumerate(deliverables, 1):
            BrandBoardDeliverable.objects.create(title=item, order=idx)
        self.stdout.write(self.style.SUCCESS(f"[OK] {len(deliverables)} Deliverables created"))

        # 6. Work Steps
        WorkStep.objects.all().delete()
        steps = [
            ("01", "Discovery", "Complete a short brand questionnaire — 5 minutes.", 1),
            ("02", "Reserve", "Book your branding slot for the week.", 2),
            ("03", "Deposit", "Pay the 50% deposit to lock it in.", 3),
            ("04", "Delivery", "Get your full brand identity in 48 hours.", 4),
        ]
        for num, title, desc, o in steps:
            WorkStep.objects.create(number=num, title=title, description=desc, order=o)
        self.stdout.write(self.style.SUCCESS(f"[OK] {len(steps)} Work steps created"))

        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully!"))
