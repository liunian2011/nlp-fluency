import llm_api
import json
import json5

get_geo_entities_prompt = '''
# General Instructions
You are a geoscience terminology extraction assistant. Please carefully read the following text and extract all terms and phrases that are specifically related to geoscience.
Requirements:
1.Extract only geoscience-related terms (e.g., landforms, stratigraphic units, rock types, geological ages, structural features, sedimentary environments, geophysical terms, etc.).
2.Do not include common words or terms unrelated to geoscience.
3.Keep compound terms intact (e.g., “Cambrian strata”, “alluvial fan deposits”).
4.Output the extracted terms in JSON format with the following structure:
    {{
      "geoscience_terms": [
        "term1",
        "term2",
      ]
    }}
5.Do not add explanations or additional text — output only the valid JSON object.

# Examples
Example input Text:
"Extending entirely across the state of Alabama for about 20 miles along its northern boundary is the Cumberland Plateau, or Tennessee Valley region, broken into broad tablelands by the dissection of rivers. In the northern part of this plateau, west of Jackson County, there are about 1000 sq mi of level highlands ranging from 700 to 1000 ft above sea level. South of the plateau lies the Appalachian Valley and Ridge province, characterized by folded and faulted sedimentary rocks."

Example Output:
{{
  "geoscience_terms": [
    "Cumberland Plateau",
    "Tennessee Valley region",
    "tablelands",
    "Jackson County",
    "Appalachian Valley and Ridge province",
    "folded and faulted sedimentary rocks"
  ]
}}

please extract geoscience terms from the following text:
{input_text}
'''


def get_geo_entities(orig_text):
    geo_entities = {}
    input_prompt = get_geo_entities_prompt.format(input_text = orig_text)
    llm_answer = llm_api.chart_with_gpt(input_prompt)
    if llm_answer:
        try:
            geo_entities = json5.loads(llm_answer.strip().replace("```json", "").replace("```", "").strip())
        except json.decoder.JSONDecodeError as e:
            print(f'llm answer can not json load. answer:{llm_answer}, 错误信息:{e.doc}')

    return geo_entities

if __name__ == '__main__':
    example_text = "Extending entirely across the state of Alabama for about 20 miles along its northern boundary is the Cumberland Plateau, or Tennessee Valley region, broken into broad tablelands by the dissection of rivers. In the northern part of this plateau, west of Jackson County, there are about 1000 sq mi of level highlands ranging from 700 to 1000 ft above sea level. South of the plateau lies the Appalachian Valley and Ridge province, characterized by folded and faulted sedimentary rocks."
    output = get_geo_entities(example_text)
    print(f'geo entities:{output}')
    output_j = json.loads(output)
    print(output_j['geoscience_terms'])

