from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from database import query_db,initialize_db

import random

database = "pythonsqlite.db"


def read_phrases(database=database):
    df = query_db(database)
    return df


def phrase_picker(key):
    df = read_phrases(database)
    phrase = random.choice(list(df[df["position"] == key]["phrase"]))
    return phrase


def phrase():
    final_string = f"Ich {phrase_picker('aktion1')} {phrase_picker('aktion2')} {phrase_picker('objekt')}, weil {phrase_picker('reason')}. {phrase_picker('nachsatz')}"
    return final_string


templates = Jinja2Templates(directory='templates')

app = Starlette(debug=True)
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.route('/')
async def homepage(request):
    initialize_db()
    return templates.TemplateResponse('index.html', {'request': request, "string":phrase()})
