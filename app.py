from flask import Flask,render_template,request,jsonify
import os
import codecs

app= Flask(__name__)

@app.route('/', defaults={'file_name': "file1.txt",'start_line_no': "0",'end_line_no':"150"})
@app.route('/<file_name>',defaults={'start_line_no': "0", 'end_line_no':"150"})
@app.route('/<file_name>/<start_line_no>',defaults={'end_line_no':"150"})
@app.route('/<file_name>/<start_line_no>/<end_line_no>')
def user(file_name,start_line_no,end_line_no):
    try:
        if file_name =="file2.txt":
            if int(start_line_no) < int(end_line_no):
                s=int(start_line_no)
                e=int(end_line_no)
                txt=''
                with codecs.open(file_name, 'rb', encoding='utf-16be',errors='ignore') as file:
                    for i, line in enumerate(file):
                        if(i>=s and i<e+1):
                            txt= txt+line
                return render_template("display.html", content=txt)
            else:    
                with codecs.open(file_name, 'rb', encoding='utf-16be',errors='ignore') as file:
                    contents = file.read()
                # return jsonify(contents)
                return render_template("display.html", content=contents)
        
        elif file_name =="file3.txt":
            if int(start_line_no) < int(end_line_no):
                s=int(start_line_no)
                e=int(end_line_no)
                txt=''
                with codecs.open(file_name, 'rb', encoding='us-ascii',errors='ignore') as file:
                    for i, line in enumerate(file):
                        if(i>=s and i<e+1):
                            txt= txt+line
                return render_template("display.html", content=txt)
            else:    
                with codecs.open(file_name, 'rb', encoding='us-ascii',errors='ignore') as file:
                    contents = file.read()
                # return jsonify(contents)
                return render_template("display.html", content=contents)
        
        elif file_name =="file4.txt":
            with codecs.open(file_name, 'rb', encoding='utf-16le',errors='ignore') as file:
                contents = file.read()
                # return jsonify(contents)
            return render_template("display.html", content=contents)
        
        else:
                if int(start_line_no) < int(end_line_no):
                    s=int(start_line_no)
                    e=int(end_line_no)
                    txt=''
                    with codecs.open("file1.txt", 'rb', encoding='us-ascii',errors='ignore') as file:
                        for i, line in enumerate(file):
                            if(i>=s and i<e+1):
                                txt= txt+line
                    return render_template("display.html", content=txt)
                else:    
                    with codecs.open("file1.txt", 'rb', encoding='us-ascii',errors='ignore') as file:
                        contents = file.read()
                    # return jsonify(contents)
                    return render_template("display.html", content=contents)
    except Exception as e:
        return render_template("500.html", error = str(e))
    except FileNotFoundError as e:
        return render_template("500.html", error = str(e))
    except ValueError as e:
        return render_template("500.html", error = str(e))
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(debug = True)
