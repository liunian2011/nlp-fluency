import time

import openai
from openai import OpenAI

client = OpenAI(api_key="sk-Avu1NSpZvuMReDJJ27BcC6Ff4b024e1c83Ef4cBa52D69e80",
                base_url="https://openai.sohoyo.io/v1")

def chart_with_gpt(input):
    chat_completion = None
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": input}]
        )
    except openai.RateLimitError:
        print('上游负载已饱和.过30s再试.')
        time.sleep(30)
    except openai.InternalServerError:
        print('internal server error.')

    if chat_completion:
        return chat_completion.choices[0].message.content
    else:
        return None


if __name__ == '__main__':
    input_prompt = """what is the capital of China?"""
    output = chart_with_gpt(input_prompt)
    print(f'output:{output}')

