from chart import gpt_ops

gen_fact_prompt_template = """
Please breakdown the following sentence into independent facts, here are some examples:

[INPUT] He made his acting debut in the film The Moon is the Sun’s Dream (1992), and continued to appear in small and supporting roles throughout the 1990s.
[OUTPUT]
He made his acting debut in the film.
He made his acting debut in The Moon is the Sun’s Dream.
The Moon is the Sun’s Dream is a film.
The Moon is the Sun’s Dream was released in 1992.
After his acting debut, he appeared in small and supporting roles.
After his acting debut, he appeared in small and supporting roles throughout the 1990s.
[INPUT] He is also a successful producer and engineer, having worked with a wide variety of artists, including Willie Nelson, Tim McGraw, and Taylor Swift.
[OUTPUT]
He is successful.
He is a producer.
He is an engineer.
He has worked with a wide variety of artists.
Willie Nelson is an artist.
He has worked with Willie Nelson.
Tim McGraw is an artist.
He has worked with Tim McGraw.
Taylor Swift is an artist.
He has worked with Taylor Swift.
[INPUT] In 1963, Collins became one of the third group of astronauts selected by NASA and he served as the back-up Command Module Pilot for the Gemini 7 mission.
[OUTPUT]
Collins became an astronaut.
Collins became one of the third group of astronauts.
Collins became one of the third group of astronauts selected.
Collins became one of the third group of astronauts selected by NASA.
Collins became one of the third group of astronauts selected by NASA in 1963.
He served as the Command Module Pilot.
He served as the back-up Command Module Pilot.
He served as the Command Module Pilot for the Gemini 7 mission.
[INPUT] In addition to his acting roles, Bateman has written and directed two short films and is currently in development on his feature debut.
[OUTPUT]
Bateman has acting roles.
Bateman has written two short films.
Bateman has directed two short films.
Bateman has written and directed two short films.
Bateman is currently in development on his feature debut.

Please breakdown the following sentence into independent facts.
Sentence:{article}
"""


def generate_fact(output_article):
     gen_prompt = gen_fact_prompt_template.format(article= output_article)
     facts = gpt_ops.chart_with_gpt(gen_prompt)

     return facts

