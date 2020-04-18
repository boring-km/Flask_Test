from flask import Flask, render_template
import sys
application = Flask(__name__)


@application.route("/")
def hello():
    return 'Hello 조준우!'


@application.route("/test")
def test():
    return render_template('test.html')

@application.route("/test2")
def test2():
    return 'test2'

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]))
