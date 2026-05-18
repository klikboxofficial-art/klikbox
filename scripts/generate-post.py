from PIL import Image, ImageDraw, ImageFont
import os, sys
from datetime import datetime

THEMES = [
    {
        "headline1": "Η επιχείρησή σου",
        "headline2": "αξίζει καλύτερο",
        "accent": "site.",
        "sub1": "Επαγγελματικό design που φέρνει πελάτες.",
        "sub2": "Γρήγορα. Αποτελεσματικά.",
        "cta": "klikbox.gr →",
        "tags": "#webdesign #κατασκευήιστοσελίδας #websitegreece"
    },
    {
        "headline1": "AI Automation",
        "headline2": "για την",
        "accent": "επιχείρησή σου.",
        "sub1": "Αυτοματοποίησε. Εξοικονόμησε χρόνο.",
        "sub2": "Περισσότερα leads. Λιγότερη δουλειά.",
        "cta": "klikbox.gr →",
        "tags": "#AIautomation #digitalmarketing #webdevelopment"
    },
    {
        "headline1": "E-shop που",
        "headline2": "πουλάει",
        "accent": "24/7.",
        "sub1": "WooCommerce & custom e-commerce solutions.",
        "sub2": "Παράδοση σε 2 εβδομάδες.",
        "cta": "klikbox.gr →",
        "tags": "#eshop #woocommerce #ηλεκτρονικόκατάστημα"
    },
    {
        "headline1": "Δωρεάν",
        "headline2": "Αξιολόγηση",
        "accent": "του Site σου.",
        "sub1": "Μάθε τι χάνεις χωρίς να πληρώσεις τίποτα.",
        "sub2": "Αποτέλεσμα σε 24 ώρες.",
        "cta": "Ζήτα το τώρα →",
        "tags": "#freeaudit #websitegreece #klikbox"
    },
    {
        "headline1": "SEO που",
        "headline2": "φέρνει",
        "accent": "επισκέπτες.",
        "sub1": "Βρες στη 1η σελίδα της Google.",
        "sub2": "Οργανική ανάπτυξη. Μόνιμα αποτελέσματα.",
        "cta": "klikbox.gr →",
        "tags": "#SEO #googleranking #digitalmarketing"
    }
]

def round_rect(draw, xy, radius, fill=None, outline=None, width=1):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill, outline=outline, width=width)

def generate():
    week_num = datetime.now().isocalendar()[1]
    day = datetime.now().weekday()
    theme = THEMES[(week_num + day) % len(THEMES)]

    SIZE = 1080
    NAVY = (13, 27, 46)
    ORANGE = (255, 107, 0)
    WHITE = (255, 255, 255)
    GRAY = (136, 153, 170)
    DARK_BLUE = (22, 34, 53)
    DIM = (42, 64, 96)

    img = Image.new('RGB', (SIZE, SIZE), NAVY)
    draw = ImageDraw.Draw(img)

    # Top/bottom orange bars
    draw.rectangle([0, 0, SIZE, 8], fill=ORANGE)
    draw.rectangle([0, SIZE-8, SIZE, SIZE], fill=ORANGE)

    # Subtle circle decoration (top right)
    for r in [300, 210]:
        draw.ellipse([SIZE-r, -r, SIZE+r, r], outline=(255, 107, 0, 20), width=1)

    # Logo badge
    round_rect(draw, [80, 88, 152, 160], radius=14, fill=DARK_BLUE, outline=ORANGE, width=2)
    
    # Try to load font, fallback to default
    try:
        font_bold_lg = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 88)
        font_bold_md = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
        font_bold_sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
        font_bold_xs = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 38)
        font_regular = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except:
        font_bold_lg = ImageFont.load_default()
        font_bold_md = ImageFont.load_default()
        font_bold_sm = ImageFont.load_default()
        font_bold_xs = ImageFont.load_default()
        font_regular = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # K letter in badge
    draw.text((116, 90), "K", fill=ORANGE, font=font_bold_xs, anchor="mt")

    # KlikBox text
    draw.text((168, 92), "KlikBox", fill=WHITE, font=font_bold_md)
    draw.text((168, 128), "WEB · AI · SOLUTIONS", fill=ORANGE, font=font_small)

    # Main headlines
    draw.text((80, 220), theme["headline1"], fill=WHITE, font=font_bold_lg)
    draw.text((80, 318), theme["headline2"], fill=WHITE, font=font_bold_lg)
    draw.text((80, 416), theme["accent"], fill=ORANGE, font=font_bold_lg)

    # Divider
    draw.line([(80, 530), (620, 530)], fill=(*ORANGE, 100), width=2)

    # Subtext
    draw.text((80, 558), theme["sub1"], fill=GRAY, font=font_regular)
    draw.text((80, 598), theme["sub2"], fill=GRAY, font=font_regular)

    # CTA button
    round_rect(draw, [80, 660, 420, 736], radius=38, fill=ORANGE)
    cta_bbox = draw.textbbox((0,0), theme["cta"], font=font_bold_sm)
    cta_w = cta_bbox[2] - cta_bbox[0]
    draw.text((250 - cta_w//2, 682), theme["cta"], fill=WHITE, font=font_bold_sm)

    # Hashtags
    tag_bbox = draw.textbbox((0,0), theme["tags"], font=font_small)
    tag_w = tag_bbox[2] - tag_bbox[0]
    draw.text(((SIZE - tag_w)//2, 980), theme["tags"], fill=DIM, font=font_small)

    # Save
    os.makedirs("public", exist_ok=True)
    out = os.path.join("public", "instagram_post.jpg")
    img.save(out, "JPEG", quality=95)
    print(f"Saved: {out}")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    generate()
