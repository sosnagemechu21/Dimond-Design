from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100, default="Dagim")
    brand_name = models.CharField(max_length=100, default="Diamond Design")
    title = models.CharField(max_length=200, default="Brand Identity & Social Media Designer")
    hero_headline = models.CharField(max_length=200, default="HI, I'M DAGIM")
    hero_subtext = models.CharField(
        max_length=255, 
        default="A brand identity & social media designer, shipping complete brand systems in 48 hours."
    )
    hero_punchline = models.CharField(
        max_length=255,
        default="One Brand Board. Everything your brand needs."
    )
    hero_description = models.TextField(
        default="A studio for brand identity and social media content. Don't let the name fool you — Diamond Design delivers everything you need to launch professionally, all summarized on a single, easy-to-use brand board."
    )
    about_heading = models.CharField(max_length=255, default="A studio built for founders in a hurry.")
    about_text = models.TextField(
        default="I help early-stage founders and small businesses launch with a real, cohesive brand — not a template. Every project is delivered on a single, useful brand board so your team can actually use it on day one."
    )
    brands_shipped_count = models.CharField(max_length=50, default="80+")
    delivery_time = models.CharField(max_length=50, default="48h")
    satisfaction_rate = models.CharField(max_length=50, default="100%")
    whatsapp_number = models.CharField(max_length=50, default="+251984670908")
    whatsapp_display = models.CharField(max_length=50, default="0984 670 908")
    instagram_handle = models.CharField(max_length=100, default="@dymndesign12")
    instagram_url = models.URLField(default="https://instagram.com/dymndesign12")
    booking_form_url = models.URLField(blank=True, default="")
    embedded_form_url = models.URLField(blank=True, default="")
    email = models.EmailField(default="dymndesign12@gmail.com")
    portrait_image = models.CharField(max_length=255, default="resume/img/portrait.png")

    def __str__(self):
        return f"{self.name} - {self.brand_name}"


class Expertise(models.Model):
    number = models.CharField(max_length=10, default="01")
    title = models.CharField(max_length=150)
    description = models.TextField()
    skills_csv = models.TextField(
        help_text="Comma-separated skills/tags, e.g. Primary Logo, Color Palette, Typography"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Expertise Areas"

    def skills_list(self):
        return [s.strip() for s in self.skills_csv.split(',') if s.strip()]

    def __str__(self):
        return f"{self.number} - {self.title}"


class Project(models.Model):
    order = models.PositiveIntegerField(default=0)
    number = models.CharField(max_length=10, default="01")
    role = models.CharField(max_length=120, default="Brand Identity Designer")
    title = models.CharField(max_length=150)
    client = models.CharField(max_length=150, blank=True)
    category = models.CharField(max_length=100, default="Brand Identity")
    year = models.CharField(max_length=20, default="'26")
    description = models.TextField(blank=True)
    main_image = models.CharField(max_length=255, help_text="Static path or URL")
    preview_image_1 = models.CharField(max_length=255, blank=True, help_text="Static path or URL")
    preview_image_2 = models.CharField(max_length=255, blank=True, help_text="Static path or URL")
    live_url = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.number} - {self.title}"


class PosterDesign(models.Model):
    brand = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    image = models.CharField(max_length=255, help_text="Static path or URL")
    year = models.CharField(max_length=20, default="'26")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.brand} - {self.category}"


class BrandBoardDeliverable(models.Model):
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class WorkStep(models.Model):
    number = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.number} - {self.title}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service_needed = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


class BrandingQuestionnaire(models.Model):
    STATUS_CHOICES = [
        ('new', 'New Brief'),
        ('reviewed', 'Reviewed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_or_whatsapp = models.CharField(max_length=50, blank=True)
    brand_name = models.CharField(max_length=150)
    industry = models.CharField(max_length=120, blank=True)
    brand_stage = models.CharField(max_length=100, blank=True)
    services_selected = models.TextField(blank=True, help_text="Comma-separated selected services")
    brand_vibe = models.CharField(max_length=255, blank=True, help_text="Aesthetic style keywords")
    color_preferences = models.CharField(max_length=255, blank=True)
    target_audience = models.TextField(blank=True)
    timeline = models.CharField(max_length=100, blank=True)
    project_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, default='new', choices=STATUS_CHOICES)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Branding Discovery Questionnaire"
        verbose_name_plural = "Branding Discovery Questionnaires"

    def __str__(self):
        return f"{self.brand_name} ({self.full_name}) - {self.created_at.strftime('%Y-%m-%d')}"
