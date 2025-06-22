import requests

def obtener_respuesta(pregunta):
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Sos un asistente llamado Loan que responde con claridad y simpatía creado por Fran."},
            {"role": "user", "content": pregunta}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        respuesta = response.json()["choices"][0]["message"]["content"]
        return respuesta
    except Exception as e:
        return f"Lo siento, hubo un error: {e}"
