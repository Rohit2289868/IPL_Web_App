from flask import  Flask, render_template,request # request is function of flask used to fetch the information sent by the form from html file
import requests # this requests is used to hit the api

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/teams')
def teams():
    response = requests.get("https://rohit1504.pythonanywhere.com/api/teams") # for local server-> "http://127.0.0.1:5000/api/teams"
    teams = response.json()['teams']
    return render_template('teams.html', teams=sorted(teams))

@app.route('/team-selection')
def team_selection():
    response = requests.get("https://rohit1504.pythonanywhere.com/api/teams")
    teams = response.json()['teams']
    return render_template('team-selection.html', teams=sorted(teams))


@app.route('/teamvsteam')
def teamvsteam():
    # team Vs team detail
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = requests.get("https://rohit1504.pythonanywhere.com/api/teamvsteam?team1={}&team2={}".format(team1, team2))
    result = response.json()

    # teams
    response2 = requests.get("https://rohit1504.pythonanywhere.com/api/teams")
    teams = response2.json()['teams']

    return render_template('team-selection.html', result=result, teams=sorted(teams))

@app.route('/team-record')
def team_record():
    response = requests.get("https://rohit1504.pythonanywhere.com/api/teams")
    teams = response.json()['teams']
    return render_template('team-record.html', teams=sorted(teams))

@app.route('/team-record-details')
def team_record_details():
    team = request.args.get('team')
    response = requests.get("https://rohit1504.pythonanywhere.com/api/team-record?team={}".format(team))
    response = response.json()
    return render_template('team-record-details.html', response=response, team=team)

@app.route('/batter')
def batter():
    response = requests.get("https://rohit1504.pythonanywhere.com/api/batter")
    batters = response.json()['batters']
    return render_template('batter-list.html', batters=batters)

@app.route('/batter-record')
def batter_record():
    batsman = request.args.get('batsman')
    response = requests.get("https://rohit1504.pythonanywhere.com/api/batsman-record?name={}".format(batsman))
    response = response.json()
    return render_template('batter-record.html', response=response, batsman=batsman)

@app.route('/bowler')
def bowler():
    response = requests.get("https://rohit1504.pythonanywhere.com/api/bowler")
    bowlers = response.json()['bowler']
    return render_template('bowler-list.html', bowlers=bowlers)

@app.route('/bowler-record')
def bowler_record():
    bowler = request.args.get('bowler')
    response = requests.get("https://rohit1504.pythonanywhere.com/api/bowler-record?name={}".format(bowler))
    response = response.json()
    return render_template('bowler-record.html', response=response, bowler=bowler)


app.run(debug=True, port=7000)