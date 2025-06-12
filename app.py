from flask import Flask,send_file
from flask import render_template,request
from generate_cv import create_cv

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        # title
        title1=request.form['title1']
        title2=request.form['title2']
        location=request.form['location']
        profile=request.form['profile']
        # education
        education1=request.form['education']
        education2=request.form['education2']
        # certificate
        certificate1=request.form['certificate1']
        certificate2=request.form['certificate2']
        # experience1
        position1=request.form['position1']
        institution1=request.form['institution1']
        duration_beg1=request.form['duration_beg1']
        duration_end1=request.form['duration_end1']
        workdone1=request.form['workdone1']

          # experience2
        position2=request.form['position2']
        institution2=request.form['institution2']
        duration_beg2=request.form['duration_beg2']
        duration_end2=request.form['duration_end2']
        workdone2=request.form['workdone2']

        # skills
        language1=request.form['language1']
        language2=request.form['language2']
        skill1=request.form['skill1']
        skill2=request.form['skill2']

        filename= create_cv(name,email,phone,title1,title2,
              location,profile,education1,education2,
              certificate1,certificate2,position1,institution1,
              duration_beg1,duration_end1,workdone1,position2,
              institution2,duration_beg2,duration_end2,workdone2,
              language1,language2,skill1,skill2)
        
        return send_file(filename, as_attachment=True, download_name=f"{name}.docx")

    






    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)