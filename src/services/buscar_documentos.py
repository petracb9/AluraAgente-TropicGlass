from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Cargar modelo de embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Cargar índice
vectorstore = FAISS.load_local(
    "data/faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# Crear buscador
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

pregunta = input("Pregunta: ")

documentos = retriever.invoke(pregunta)

print("\nResultados encontrados:\n")

for i, doc in enumerate(documentos, start=1):
    print("=" * 50)
    print(f"Resultado {i}")
    print("=" * 50)
    print(doc.page_content)