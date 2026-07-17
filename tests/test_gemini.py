from services.llm_service import crear_llm

llm = crear_llm()

respuesta = llm.invoke("¿Qué medios de pago acepta TropicGlass?")



print(respuesta)