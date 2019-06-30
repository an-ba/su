import yaml #PyYAML
import random


with open("./phrasen.yml", 'r') as stream:
    try:
        phrasen = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


output = f"Ich {random.choice(phrasen['aktion1'])} {random.choice(phrasen['aktion2'])} {random.choice(phrasen['objekt'])}, weil {random.choice(phrasen['reason'])}. {random.choice(phrasen['nachsatz'])}"


print(output)