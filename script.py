import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Loading the entire spreadsheet
df = pd.read_excel("Participants_spreadsheet/EPIC_Boston_2026_Participants.xlsx")

# Load templates
template_badge = Image.open("Template_badge/Epic_badgeMain.png")
template_certificate = Image.open("Template_certificate/Template_certificate_main.png")

# Define fonts
fonte_name_badge = ImageFont.truetype("Text_Fonts/Montserrat-Bold.ttf", 63)
fonte_company_badge = ImageFont.truetype("Text_Fonts/Montserrat-Bold.ttf", 40)

# Specific font for the certificate
fonte_cert_nome = ImageFont.truetype("Text_Fonts/GreatVibes-Regular.ttf", 160)

# Color black and teal (#09ABA3)
teal = (9, 171, 163)

for _, line in df.iterrows():
    nome = line["Full Name"]
    empresa = line["Company"]

    parts_name = nome.split()
    first_name = parts_name[0]
    last_name = parts_name[-1]

    badge_name = f"Badge_{first_name}_{last_name}.png"
    certificate_name = f"Certificate_{first_name}_{last_name}.pdf"

#---Badge---
    badge = template_badge.copy()
    draw_badge = ImageDraw.Draw(badge)
    draw_badge.text((250, 1050), nome, font=fonte_name_badge, fill="black")
    draw_badge.text((250, 1350), empresa, font=fonte_company_badge, fill="black")
    badge.save(f"Epic_Badges/{badge_name}")

#---Certificate---
    cert = template_certificate.copy()
    draw_cert = ImageDraw.Draw(cert)
    draw_cert.text(
        (1754, 1305), #
        nome,
        font=fonte_cert_nome,
        fill="teal",
        anchor="mm"
    )
    cert.save(f"Epic_Certificates/{certificate_name}", "PDF")


