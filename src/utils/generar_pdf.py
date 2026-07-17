from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Carpetas
DOCS_DIR = Path("docs")
OUTPUT_DIR = Path("data/pdf")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PDF_FILE = OUTPUT_DIR / "TropicGlass_Manual_Cliente.pdf"

styles = getSampleStyleSheet()
story = []

# Lee todos los archivos Markdown en orden
for md_file in sorted(DOCS_DIR.glob("*.md")):
    story.append(Paragraph(f"<b>{md_file.stem}</b>", styles["Heading1"]))

    contenido = md_file.read_text(encoding="utf-8")

    for linea in contenido.splitlines():
        linea = linea.strip()

        if not linea:
            continue

        # Evitar problemas con caracteres HTML
        linea = (
            linea.replace("&", "&amp;")
                 .replace("<", "&lt;")
                 .replace(">", "&gt;")
        )

        story.append(Paragraph(linea, styles["BodyText"]))

doc = SimpleDocTemplate(str(PDF_FILE))
doc.build(story)

print(f"PDF generado correctamente en: {PDF_FILE}")