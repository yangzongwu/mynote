from flask import Flask
import time

app=Flask(__name__)

@app.route('/1')
def index1():
    time.sleep(1)
    return 'hello 1'

@app.route('/2')
def index2():
    time.sleep(1)
    return 'hello 2'

@app.route('/3')
def index3():
    time.sleep(1)
    return 'hello 3'

if __name__=='__main__':
    app.run(threaded=True)