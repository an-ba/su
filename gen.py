import yaml #PyYAML
import random

def read_phrases(location="./phrases.yml"):
    with open(location, 'r') as stream:
        try:
            phrases = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        return phrases
    
def random_phrase(key):
    phrases = read_phrases()
    phrase = random.choice(phrases[key])
    return phrase

output = f"Ich {random_phrase('aktion1')} {random_phrase('aktion2')} {random_phrase('objekt')}, weil {random_phrase('reason')}. {random_phrase('nachsatz')}"


print(output)