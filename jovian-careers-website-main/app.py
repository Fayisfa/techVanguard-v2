from flask import Flask, render_template,jsonify


app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Trivandrum',
    'salary': 10000000
  },
    {
      'id': 2,
      'title': 'Data Scientist',
      'location': 'Kozhikode',
      'salary': 15000000
    },
{
  'id': 1,
  'title': 'Frondent Engineer',
  'location': 'Wayanad',
  'salary': 25000000
},
{
  'id': 1,
  'title': 'Backend Developer',
  'location': 'Manjeri'
}

]

@app.route("/")
def hello():
  return render_template("home.html",jobs= JOBS)

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
