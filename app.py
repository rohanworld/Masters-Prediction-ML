from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('masters_predictor.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        gre_score = float(request.form['gre_score'])
        toefl_score = float(request.form['toefl_score'])
        university_rating = float(request.form['university_rating'])
        sop = float(request.form['sop'])
        lor = float(request.form['lor'])
        cgpa = float(request.form['cgpa'])
        research_paper = float(request.form['research_paper'])

        input_data = [[gre_score, toefl_score, university_rating, sop, lor, cgpa, research_paper]]
        chance = model.predict(input_data)

        return render_template('index.html', chance=f"{chance[0]*100:.2f}%")

    return render_template('index.html', chance="")

if __name__ == '__main__':
    app.run(debug=True)
