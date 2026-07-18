import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Loading the entire spreadsheet
df = pd.read_excel("Participants_spreadsheet/EPIC_Boston_2026_Participants.xlsx")

# Load templates
template_badge = Image.open("Template_badge/Epic_badgeMain.png")
template_certificate = Image.open("Template_certificate/Template_certificate_main.png")

# Define fonts
font_name_badge = ImageFont.truetype("Text_Fonts/Montserrat-Bold.ttf", 90)
font_company_badge = ImageFont.truetype("Text_Fonts/Montserrat-Bold.ttf", 40)

# Specific font for the certificate (normal size and reduced size for long names)
font_cert_name = ImageFont.truetype("Text_Fonts/GreatVibes-Regular.ttf", 160)
font_cert_name_reduced = ImageFont.truetype("Text_Fonts/GreatVibes-Regular.ttf", 120)

#Font: Great Vibes - Size: 48
#Color: Dark teal
#Code: #09ABA3

#red: 9
#green: 171
#blue: 163

teal = (9, 171, 163)

# Rules for "long name" handling
MAX_SOBRENOMES = 3
BADGE_TEXT_X = 250
BADGE_MAX_WIDTH = 900 

for _, line in df.iterrows():
    name = line["Full Name"]
    company = line["Company"]

    parts_name = name.split()
    first_name = parts_name[0]
    last_name = parts_name[-1]
    surbname = parts_name[1:]
    short_name = f"{first_name} {last_name}"

    badge_name = f"Badge_{first_name}_{last_name}.png"
    certificate_name = f"Certificate_{first_name}_{last_name}.pdf"

#---Badge---
    badge = template_badge.copy()
    draw_badge = ImageDraw.Draw(badge)

# Use the short name (first + last) if there are more than 3 surnames,
# OR if the full name is simply too wide to fit on the badge image.
    larg_name = draw_badge.textbbox((0, 0), name, font=font_name_badge)[2]
    if len(surbname) > MAX_SOBRENOMES or larg_name > BADGE_MAX_WIDTH:
        name_badge = short_name
    else:
        name_badge = name

    draw_badge.text((BADGE_TEXT_X, 1050), name_badge, font=font_name_badge, fill="black")
    draw_badge.text((BADGE_TEXT_X, 1350), company, font=font_company_badge, fill="black")
    badge.save(f"Epic_Badges/{badge_name}")

#---Certificate---
    cert = template_certificate.copy()
    draw_cert = ImageDraw.Draw(cert)

# Certificate always keeps the FULL name, only the font size shrinks,
# when there are more than 3 surnames.
    if len(surbname) > MAX_SOBRENOMES:
        font_certificate = font_cert_name_reduced
    else:
        font_certificate = font_cert_name

    draw_cert.text(
        (1754, 1305),
        name,
        font= font_certificate,
        fill="teal",
        anchor="mm"
    )
    cert.save(f"Epic_Certificates/{certificate_name}", "PDF")

