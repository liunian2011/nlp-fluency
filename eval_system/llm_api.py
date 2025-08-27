import time
import openai
from openai import OpenAI

Gpt4_Model = 'gpt-4'
Gpt4o_model = 'gpt-4o'
DeepSeek_Model = 'deepseek-chat'
Claude_Model = 'claude-3-7-sonnet-20250219'
Plam_Model = 'PaLM-2'

client = OpenAI(api_key="sk-Avu1NSpZvuMReDJJ27BcC6Ff4b024e1c83Ef4cBa52D69e80",
                base_url="https://openai.sohoyo.io/v1")


def retry(max_retries=3, delay=5, allowed_exceptions=(Exception,)):
    """
    :param max_retries: 最大尝试次数
    :param delay: 每次重试间隔秒数
    :param allowed_exceptions: 哪些异常会触发重试
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except allowed_exceptions as e:
                    retries += 1
                    print(f"尝试执行 {func.__name__} (重试次数: {retries})")
                    if retries == max_retries:
                        print(f'重试{retries}次依然失败，跳过')  # 如果达到最大重试次数，放弃执行
                    time.sleep(delay)
                except Exception as ex:
                    print(f'执行遇到错误：{ex}')
        return wrapper
    return decorator


@retry(max_retries=3, delay=10, allowed_exceptions=(openai.RateLimitError, openai.InternalServerError))
def chart_with_gpt(input):
    chat_completion = None
    try:
        chat_completion = client.chat.completions.create(
            model=Gpt4o_model,
            messages=[{"role": "user", "content": input}]
        )
    except openai.RateLimitError:
        print('上游负载已饱和.需要重试.')
        raise
    except openai.InternalServerError:
        print('内部错误，需要重试.')
        raise
    except openai.AuthenticationError:
        print('令牌已用尽，需要联系管理员-郑鹏飞')
        raise
    except Exception:
        raise

    if chat_completion:
        return chat_completion.choices[0].message.content
    else:
        return chat_completion


if __name__ == '__main__':
    input_prompt = r"""
    # Factuality Assessment Task
Based on the information provided in the article section, evaluate the factuality of the following statements, DO NOT refer to any external knowledge or information beyond the article.
Respond with "Supported", or "Not-supported" or "Not-mentioned" , provide explanatory reasons in the following format:
Statement [Number] | [Your Answer] | [Explanatory Reasoning] 

# Additional Guidance
Supported: The statement is accurate based on available evidence.
Not-mentioned: Lack of credible evidence to determine accuracy.
Not-supported: The statement is inaccurate or contradicts established facts.

# examples
Supported: "The company's revenue increased by 10% in 2020 compared to 2019." (If the attachment files contain a financial report showing the company's revenue in 2019 as $100,000 and in 2020 as $110,000, this statement would be supported because the numbers can be used to calculate the 10% increase.)
Not-Supported: "The company's revenue increased by 20% in 2020 compared to 2019." (If the attachment files contain the same financial report, this statement would not be supported because the numbers do not support a 20% increase.)
Not-mentioned: "The company's CEO is planning to retire in 2023." (If the attachment files do not mention the CEO's retirement plans or any information about the CEO's future plans, this statement would be Not-mentioned.)

# article
# The Fundamentals Of Mental HeAlth AND MeNTAL IlLNeSS 

## THe FUnDAmENTALS Of MEnTAl HEAlTh AND MeNTAL ILLNESS 

vast body of research on mental health and, to an Teven greater extent, on mental illness constitutes the foundation of this Surgeon General's report. To understand and better appreciate the content of the chapters that follow, readers outside the mental health tield may desire some background information. Thus, this chapter furnishes a "primer"' on topics that the report addresses. 

The chapter begins with an overview of research under way today that is focused on the neuroscience of mental health. Modern integrative neuroscience offers a imeans of linking research on broad "systems leve!" aspects of brain function with the remarkably detailed tools and findings of molecular biology. The report begins with a discussion of the brain because it is central to what makes us human and provides an understanding of mental health and mental illness. All of human behavior is mediated by the brain. Consider, for example, a memory that most people have from childhood--that of learning to ride a bicycle with thehelp of a parent or friend. The fear of falling, the anxiety of lack of control, the reassurances of a loved one. and the final liberating experience of mastery and a newly extended universe create an unforgettable combination. For some, the memories are not good ones: falling and being chased by dogs have left marks. of anxiety and fear that may last a lifetime. Science is revealing how the skill learning, emotional overtones, and memories of such experiences are put together physically in the brain. The brain and mind are two sides of the same coin. Mind is not possible without the remarkable physical complexity that is built into the brain, but, in addition, the physical complexity of the brain is useless without the sculpting that environment, experience, and thought itself provides. Thus the brain is now known to be physically shaped by contributions from our genes and our experience, working together. This strengthens the view that mental disorders are hoth caused and can be treated by biological and experiential processes, working together. This understanding has emerged from the breathtaking progress in modern neuroscience that has begun to integrate knowledge from biological and behavioral sciences. 

An overview of mental illness follows the section on modern integrative brain science. The section highlights topics including symptoms, diagnosis, epidemiology (i.e., research having to do with the distribution and determinants of mental disorders in population groups, including various racial and ethnic minority groups), and cost, all of which are discussed in greater and more pointed detail in the chapters that follow. Etiology is the study of the origins and causes of disease, and that section reviews research that is seeking to define, with ever greater precision, the causes of mental disorders. As will be seen, etiology research examines fundamental biological, behavioral, and sociocultural processes, as well as a necessarily broad array of life events. The section on development of temperament reveals how mental health science has attempted over much of the past century to understand how biological, psychological, and sociocultural factors meld in health as well as in illness. The chapter then reviews research approaches to the prevention and treatment of mental disorders and provides an overview of mental health services and their delivery. Final sections cover the growing influence on the mental 

## Mental Health: A Report of the Surgeon General 

health field of the need for attention to cultural diversity, the importance of the consumer movement, and new optimism about recovery from mental. illness---that is, the possibility of recovering one's life.. 

## The Neuroscience of Mental Health 

## Complexity of the Brain I: Structural 

As befits the organ of the mind, the human brain is the most complex structure ever investigated by our science. The brain contains approximately 100 billion. nerve cells, or neurons, and many more supporting cells, or glia. In and of themselves, the number of cells in this 3-pound organ reveal little of its complexity. Yet most organs in the body are composed of only a handful of cell types; the brain, in contrast, has literally. thousands of different kinds of neurons, each distinct in. terms of its chemistry, shape, and connections (Figure 2-1 depicts the structural variety of neurons). To illustrate, one careful, recent investigation of a kind of interneuron that is a small local circuit neuron in the. retina, called the amacrine cell, found no less than 23 identifiable types. 

But this is only the beginning of the brain's complexity. 

Source: Fischbach, 1992, p. 53. (Permission granted: Patricia J. Wynne.) 

Figure 2-1. Structura! variety of neurons 

![](73ef445be96f546f534d38ede555f46807cede169db444d72890fa578c1911db.jpg)


# Your Task
Please evaluate the factual accuracy of the following statements:

The realm of medical science continually evolves.
Medical science evolves with new discoveries.
New discoveries deepen our understanding of the human body's structures.
New discoveries enhance diagnostic techniques.
New discoveries enhance therapeutic techniques.
Classification of biological entities is central to medical advancements.
The classification of biological entities is an intellectual endeavor.
The classification of biological entities has practical implications.
The classification of biological entities has practical implications in molecular biology.
The classification of biological entities has practical implications in cellular function.
The article explores the relationship between classification and intellectual frameworks.
The article explores the relationship between classification and diagnostic procedures.
The article explores the understanding and manipulation of cell function.

Classification in medical science organizes biological information.
Classification enables examination of differences in biological entities.
Classification enables examination of similarities in biological entities.
Classification helps researchers conceptualize scientific data.
Classification helps clinicians prioritize scientific data.
Organisms are classified into domains.
Organisms are classified into kingdoms.

Classification in cellular biology is critical.
Cells are categorized based on function and type.
Examples of cell types include muscle cells, nerve cells, and epithelial cells.
Cell categorization allows for understanding cell function.
Cell categorization informs roles in health and disease.
Classification helps develop diagnostic strategies.
Classification helps develop therapeutic strategies.

Classification enhances diagnostic procedures.
Modern diagnostics use techniques like flow cytometry.
Flow cytometry classifies cells by size, granularity, and protein expression.
Fluorescently labeled antibodies bind to cell-associated antigens in flow cytometry.
Classification provides insights into cell function.
Classification facilitates identification of aberrant cells.
Identifying aberrant cells guides treatment decisions.

Molecular diagnostics employ PCR for disease classification.
PCR stands for Polymerase Chain Reaction.
Molecular diagnostics classify diseases at a genetic level.
Understanding genetic mutations helps tailor therapeutic approaches.
Tailoring therapeutic approaches is part of personalized medicine.
Classification links genetic sequences to functionality in the cell.

Understanding cell function is a pinnacle of classification.
Cell function comprises metabolic processes.
Cell function includes complex functions like signaling and differentiation.
Cellular activity is tied to classes of cells.
Classes of cells are governed by molecular makeup and environmental interaction.
Neurons transmit nerve impulses in the nervous system.
Neuronal classification relates to its function.
Aberrations in neuron function can lead to neurological disorders.
Neurological disorders are diagnosed through specific class markers.

Classification extends to organelles within cells.
Mitochondria are classified based on energy production.
Mitochondria are known as the powerhouse of the cell.
Defects in mitochondrial DNA lead to mitochondrial disorders.
Understanding mitochondrial disorders is rooted in classification and function assessment.

Classification is foundational to diagnostic procedures.
Classification underpins modern medical science procedures.
Classification links to understanding cell function.
Classification links to manipulation of cell function.
Systematic classification maps the landscape of cellular functions.
Classification informs health and disease implications.
    """
    input_prompt = """what is the capital of China?"""
    output = chart_with_gpt(input_prompt)
    print(f'output:{output}')
