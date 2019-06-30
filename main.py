from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

import yaml #PyYAML
import random


def read_phrases(location="./phrases.yml"):
    with open(location, 'r') as stream:
        try:
            phrases = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        return phrases

def phrase_picker(key):
    phrases = read_phrases()
    phrase = random.choice(phrases[key])
    return phrase

def phrase():
    final_string = f"Ich {phrase_picker('aktion1')} {phrase_picker('aktion2')} {phrase_picker('objekt')}, weil {phrase_picker('reason')}. {phrase_picker('nachsatz')}"
    return final_string



templates = Jinja2Templates(directory='templates')

app = Starlette(debug=True)
app.mount('/static', StaticFiles(directory='static'), name='static')



@app.route('/')
async def homepage(request):
    return templates.TemplateResponse('index.html', {'request': request, "string":phrase()})
