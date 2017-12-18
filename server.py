import bottle


app = bottle.Bottle()


@app.get('/')
def dummy_string():
    return ''
