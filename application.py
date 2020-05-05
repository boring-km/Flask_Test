from flask import Flask, render_template, request, jsonify
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello 조준우!'


@app.route("/upload")
def upload():
    return render_template('upload.html')

@app.route("/fileupload", methods=['POST'])
def fileUpload():
    music = request.files['files']
    print("업로드 된 파일: ", music.filename)
    return jsonify({"code": "OK"}) # 성공 결과 리턴


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
