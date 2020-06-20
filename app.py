from flask import Flask,request,jsonify
# from werkzeug import secure_filename
import codecs

app= Flask(__name__)

@app.route('/', defaults={'file_name': "file1.txt"})
@app.route('/<file_name>')
def user(file_name):
    if file_name =="file2.txt":
        with codecs.open(file_name, 'rb', encoding='utf-16be',errors='ignore') as file:
            contents = file.read()
            return jsonify(contents)
    
    elif file_name =="file3.txt":
        with codecs.open(file_name, 'rb', encoding='us-ascii',errors='ignore') as file:
            contents = file.read()
            return jsonify(contents)
    
    elif file_name =="file4.txt":
        with codecs.open(file_name, 'rb', encoding='utf-16le',errors='ignore') as file:
            contents = file.read()
            return jsonify(contents)
    
    else:
        with codecs.open("file1.txt", 'rb', encoding='us-ascii',errors='ignore') as file:
            contents = file.read()
            return jsonify(contents)

if __name__ == '__main__':
    app.run(debug = True)