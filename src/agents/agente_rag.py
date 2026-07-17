from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from prompts.prompt_agente import PROMPT_AGENTE
from services.llm_service import crear_llm


def iniciar_agente():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        "data/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    llm = crear_llm()

    print("=" * 60)
    print("Alura Agente - TropicGlass")
    print("=" * 60)

    while True:

        pregunta = input("\nPregunta: ")

        if pregunta.lower() == "salir":
            print("\nHasta luego.")
            break

        documentos = retriever.invoke(pregunta)

        contexto = "\n\n".join(
            doc.page_content
            for doc in documentos
        )

        prompt = PROMPT_AGENTE.invoke(
            {
                "contexto": contexto,
                "pregunta": pregunta
            }
        )

        respuesta = llm.invoke(prompt)

        texto = ""

        if isinstance(respuesta.content, list):
            for bloque in respuesta.content:
                if bloque.get("type") == "text":
                    texto += bloque.get("text", "")
        else:
            texto = respuesta.content

        print("\nRespuesta:\n")
        print(texto)