from openai import AsyncOpenAI
from config.config import settings

client = AsyncOpenAI(api_key=settings.OPEN_AI_KEY.get_secret_value())


async def get_assistant_response(user_input: str) -> str:
    thread = await client.beta.threads.create()

    await client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_input
    )

    run = await client.beta.threads.runs.create(
        thread_id=thread.id, assistant_id=settings.ASSISTANT_ID.get_secret_value()
    )

    while True:
        status = await client.beta.threads.runs.retrieve(
            thread_id=thread.id, run_id=run.id
        )
        if status.status == "completed":
            break

    messages = await client.beta.threads.messages.list(thread_id=thread.id)
    return messages.data[0].content[0].text.value
