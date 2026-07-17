from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

# Ruta del PDF
PDF_PATH = Path("data/pdf/TropicGlass_Manual_Cliente.pdf")

# Cargar el documento
loader = PyPDFLoader(str(PDF_PATH))
documentos = loader.load()

print("=" * 50)
print("PDF cargado correctamente")
print("=" * 50)

print(f"Páginas leídas: {len(documentos)}")

print("\nPrimeros 500 caracteres:\n")
print(documentos[0].page_content[:500])