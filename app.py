import bottle

app = bottle.Bottle()

@app.route('/')
@bottle.view('root')
def root():
    return {}

@app.route('/login')
def login():
    return '<a href="/">Return home</a>'

@app.route('/js/<filename>')
def js(filename):
  return bottle.static_file(filename, root='static/js')

@app.route('/css/<filename>')
def css(filename):
  return bottle.static_file(filename, root='static/css')

@app.route('/fonts/<filename>')
def fonts(filename):
  return bottle.static_file(filename, root='static/fonts')

if __name__ == '__main__':
    bottle.run(app, host='localhost', port=8080, debug=True, reloader=True)
