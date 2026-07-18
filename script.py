import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Carregar toda a  planilha
df = pd.read_excel("EPIC_Boston_2026_Participants.xlsx")

# Carregar template exportado como imagem
template = Image.open("Epic_badgeMain.png")

# Definir fontes
fonte_nome = ImageFont.truetype("Fonts/Montserrat-Bold.ttf", 63)
fonte_empresa = ImageFont.truetype("Fonts/Montserrat-Bold.ttf", 40)

# Loop pelos participantes
for _, linha in df.iterrows():
    nome = linha["Full Name"]
    empresa = linha["Company"]

# Extrair primeiro e último nome
    partes_nome = nome.split()
    first_name = partes_nome[0]
    last_name = partes_nome[-1]
    file_name = f"Badge_{first_name}_{last_name}.png"

# Copiar template
    credencial = template.copy()
    draw = ImageDraw.Draw(credencial)

# Inserir textos (ajuste coordenadas conforme layout)
    draw.text((250, 1050), nome, font=fonte_nome, fill="black")
    draw.text((250, 1350), f"{empresa}", font=fonte_empresa, fill="black")

# Salvar credencial
    credencial.save(f"Badges/{file_name}")

