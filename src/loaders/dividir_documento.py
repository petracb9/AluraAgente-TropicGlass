from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Ruta del PDF
PDF_PATH = Path("data/pdf/TropicGlass_Manual_Cliente.pdf")

# Cargar documento
loader = PyPDFLoader(str(PDF_PATH))
documentos = loader.load()

# Dividir en fragmentos
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documentos)

print("=" * 50)
print("Documento dividido correctamente")
print("=" * 50)

print(f"Páginas originales : {len(documentos)}")
print(f"Chunks generados   : {len(chunks)}")

print("\nPrimer chunk:\n")
print(chunks[0].page_content)

print("\nMetadata:\n")
print(chunks[0].metadata)