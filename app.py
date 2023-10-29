from flask import Flask, render_template

app = Flask(__name__)


JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': '45k'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': '35k'
  },
  {
    'id': 3,
    'title': 'Front End Engineer',
    'location': 'Remote',
    'salary': '120k'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Fransisco, USA',
    'salary': '110k'
  } 
]



@app.route('/')
def hello_world():
  return render_template('home.html',
                          jobs=JOBS,
                          company_name='Alec'
                        )
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)