from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

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

# Modelo de embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Crear índice
vectorstore = FAISS.from_documents(chunks, embeddings)

# Guardar índice
vectorstore.save_local("data/faiss_index")

print("=" * 50)
print("Índice vectorial creado correctamente")
print("=" * 50)
print(f"Chunks indexados: {len(chunks)}")
print("Carpeta creada: data/faiss_index")