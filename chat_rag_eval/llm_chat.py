import json
import requests

fusion_prompt_template = """
# Assistant Background

You are an assistant who can give accurate answers, Please give accurate answers based on historical messages and Search results. Do not include any explicit references, citations, or external source numbers in the response.

# General Instructions

Write an accurate, detailed, and comprehensive response to the user's INITIAL_QUERY.
Additional context is provided as "USER_INPUT" after specific questions.
Your answer should be informed by the provided "Search results".
Your answer must be as detailed and organized as possible, Prioritize the use of lists, tables, and quotes to organize output structures.
Your answer must be precise, of high-quality, and written by an expert using an unbiased and journalistic tone.
You MUST refer to the most relevant search results that answer the question. Do not mention any irrelevant results.
Be Carefully, The citation marks or number MUST NOT appear in your answer, and you MUST implicitly refer to the search results, and you MUST NOT fabricating citations in your answer.You MUST ADHERE to the following formatting instructions:
- NEVER start an answer with a heading or title of any kind, like "#### Header".
- Use markdown to format paragraphs, lists, tables, and quotes whenever possible.
- Use single new lines for lists and double new lines for paragraphs.
- Use markdown to render images given in the search results.
- NEVER write URLs or links.

# USER_INPUT

## Search results

Here are the set of search results:

```
{ragReference}
```

Your answer MUST be written in the same language as the user question, For example, if the user question is written in chinese, 你的回答也应该使用中文, if user's question is written in english, your answer should be written in english too. And here is the user's INITIAL_QUERY:{content}
"""

url = 'http://10.200.100.95:30638/llm/generate'
headers = {'Content-Type': 'application/json'}

data_str = """
{
"input": "",
"history": [],
"serviceParams": {
    "maxContentRound": 0,
    "maxOutputLength": 3000,
    "maxWindowSize": 500,
    "stream": false,
    "system": "You are a helpful assistant.",
    "generateStyle": "chat"
},
"modelParams": {
    "best_of": 1,
    "temperature": 0.2,
    "use_beam_search": false,
    "presence_penalty": 0.0,
    "frequency_penalty": 0.0,
    "top_p": 1.0,
    "top_k": -1,
    "length_penalty": 1.0 }
}
"""

def request(input:str):
    data_json = json.loads(data_str)
    data_json['input'] = input
    response = requests.post(url, headers=headers, json=data_json)

    # 打印响应内容
    res_json = json.loads(response.text)
    code = res_json['code']
    res_data = res_json['data']
    output = res_data['output']
    #print(output)
    return code, output


def compose_prompt(question, rag_retrievel_result):
    prompt = fusion_prompt_template.format(content=question, ragReference=rag_retrievel_result)
    return prompt

if __name__ == '__main__':
    input_prompt = """中国最大的省是哪个"""
    request(input_prompt)

