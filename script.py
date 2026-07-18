import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Loading the entire spreadsheet
df = pd.read_excel("Participants_spreadsheet/EPIC_Boston_2026_Participants.xlsx")

# Load templates
template_badge = Image.open("Template_badge/Epic_badgeMain.png")
template_certificate = Image.open("Template_certificate/Template_certificate_main.png")

# Define fonts
fonte_name_badge = ImageFont.truetype("Text_Fonts/Montserrat-Bold.ttf", 90)
fonte_company_badge = ImageFont.truetype("Text_Fonts/Montserrat-Bold.ttf", 40)

# Specific font for the certificate (normal size and reduced size for long names)
fonte_cert_nome = ImageFont.truetype("Text_Fonts/GreatVibes-Regular.ttf", 160)
fonte_cert_nome_reduzida = ImageFont.truetype("Text_Fonts/GreatVibes-Regular.ttf", 120)

# Color black and teal (#09ABA3)
teal = (9, 171, 163)

# Rules for "long name" handling
MAX_SOBRENOMES = 3          # more than this many surnames counts as a long name
BADGE_TEXT_X = 250          # x position where the badge name starts
BADGE_MAX_WIDTH = 900       # available width (in px) for the name on the badge before it overflows the image

for _, line in df.iterrows():
    nome = line["Full Name"]
    empresa = line["Company"]

    parts_name = nome.split()
    first_name = parts_name[0]
    last_name = parts_name[-1]
    sobrenomes = parts_name[1:]           # everything after the first name
    nome_curto = f"{first_name} {last_name}"

    badge_name = f"Badge_{first_name}_{last_name}.png"
    certificate_name = f"Certificate_{first_name}_{last_name}.pdf"

#---Badge---
    badge = template_badge.copy()
    draw_badge = ImageDraw.Draw(badge)

    # Use the short name (first + last) if there are more than 3 surnames,
    # OR if the full name is simply too wide to fit on the badge image.
    largura_nome = draw_badge.textbbox((0, 0), nome, font=fonte_name_badge)[2]
    if len(sobrenomes) > MAX_SOBRENOMES or largura_nome > BADGE_MAX_WIDTH:
        nome_cracha = nome_curto
    else:
        nome_cracha = nome

    draw_badge.text((BADGE_TEXT_X, 1050), nome_cracha, font=fonte_name_badge, fill="black")
    draw_badge.text((BADGE_TEXT_X, 1350), empresa, font=fonte_company_badge, fill="black")
    badge.save(f"Epic_Badges/{badge_name}")

#---Certificate---
    cert = template_certificate.copy()
    draw_cert = ImageDraw.Draw(cert)

    # Certificate always keeps the FULL name — only the font size shrinks
    # when there are more than 3 surnames.
    if len(sobrenomes) > MAX_SOBRENOMES:
        fonte_certificado = fonte_cert_nome_reduzida
    else:
        fonte_certificado = fonte_cert_nome

    draw_cert.text(
        (1754, 1305),
        nome,
        font=fonte_certificado,
        fill="teal",
        anchor="mm"
    )
    cert.save(f"Epic_Certificates/{certificate_name}", "PDF")

