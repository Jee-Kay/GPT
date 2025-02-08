import os

import openai


def main() -> None:
    client = openai.AzureOpenAI(
        api_version="2024-06-01",
        azure_endpoint="https://genai-nexus.int.api.corpinter.net/apikey/openai/deployments/gpt-4o/chat/completions/",
        api_key="6559568b-bb8c-4234-af21-b666ea778a26"
,
    )

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": """ hii !! """
,
            },
        ],
    )
    print("Response: " + completion.choices[0].message.content)


if __name__ == "__main__":
    main()


#https://huggingface.co/blog/ngxson/make-your-own-rag
#https://ollama.com/download