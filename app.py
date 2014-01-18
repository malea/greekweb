import bottle

app = bottle.Bottle()

@app.route('/')
@bottle.view('root')
def root():
    return {}

@app.route('/login')
def login():
    return '<a href="/">Return home</a>'

if __name__ == '__main__':
    bottle.run(app, host='localhost', port=8080, debug=True, reloader=True)
