from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data
matches = [
    {
        'id': 1,
        'team1': 'Team A',
        'team2': 'Team B',
        'odds_team1': 1.75,
        'odds_team2': 2.10
    },
    {
        'id': 2,
        'team1': 'Team C',
        'team2': 'Team D',
        'odds_team1': 2.50,
        'odds_team2': 1.90
    }
]

@app.route('/')
def home():
    return render_template('index.html', matches=matches)

@app.route('/place_bet', methods=['POST'])
def place_bet():
    match_id = int(request.form['match_id'])
    bet_team = request.form['team']
    amount = float(request.form['amount'])

    # Find the selected match
    match = next((m for m in matches if m['id'] == match_id), None)
    if match:
        if bet_team == 'team1':
            odds = match['odds_team1']
        elif bet_team == 'team2':
            odds = match['odds_team2']
        else:
            return 'Invalid team selection'

        potential_winnings = amount * odds
        return f'You placed a bet of {amount}$ on {bet_team} with odds {odds}. Potential winnings: {potential_winnings}$'
    else:
        return 'Invalid match ID'

if __name__ == '__main__':
    app.run(debug=True)
<!DOCTYPE html>
<html>
<head>
    <title>FinEntertainment</title>
    <style>
        /* CSS for the graphical representation */
        .match {
            display: inline-block;
            padding: 10px;
            border: 1px solid #ccc;
            margin: 10px;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>FinEntertainment</h1>
    
    <!-- User Authentication -->
    <div>
        {% if user %}
            <p>Welcome, {{ user }}</p>
            <a href="/logout">Logout</a>
        {% else %}
            <a href="/login">Login</a> |
            <a href="/register">Register</a>
        {% endif %}
    </div>

    <!-- Graphical Representation of Matches -->
    <div>
        {% for match in matches %}
            <div class="match">
                <h3>Match {{ match.id }}</h3>
                <p>{{ match.team1 }} vs {{ match.team2 }}</p>
                <p>Odds for {{ match.team1 }}: {{ match.odds_team1 }}</p>
                <p>Odds for {{ match.team2 }}: {{ match.odds_team2 }}</p>
                <form action="/place_bet" method="post">
                    <input type="hidden" name="match_id" value="{{ match.id }}">
                    <label for="team">Select Team:</label>
                    <select name="team">
                        <option value="team1">Team A</option>
                        <option value="team2">Team B</option>
                    </select>
                    <br>
                    <label for="amount">Enter Bet Amount:</label>
                    <input type="number" name="amount" step="0.01" min="0" required>
                    <br>
                    <input type="submit" value="Place Bet">
                </form>
            </div>
        {% endfor %}
    </div>

    <!-- Stored Bets -->
    <div>
        <h2>Stored Bets</h2>
        <!-- Placeholder for displaying stored bets -->
    </div>
</body>
</html>
<!DOCTYPE html>
<html>
<head>
    <title>FinEntertainment</title>
    <style>
        /* CSS for the graphical representation */
        .match {
            display: inline-block;
            padding: 10px;
            border: 1px solid #ccc;
            margin: 10px;
            text-align: center;
        }

        .graph {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 300px;
            background-color: #f5f5f5;
            border: 1px solid #ccc;
            margin-top: 20px;
        }

        .graph img {
            max-height: 100%;
            max-width: 100%;
        }
    </style>
</head>
<body>
    <h1>FinEntertainment</h1>
    
    <!-- User Authentication -->
    <div>
        {% if user %}
            <p>Welcome, {{ user }}</p>
            <a href="/logout">Logout</a>
        {% else %}
            <a href="/login">Login</a> |
            <a href="/register">Register</a>
        {% endif %}
    </div>

    <!-- Graphical Representation of Matches -->
    <div>
        {% for match in matches %}
            <div class="match">
                <h3>Match {{ match.id }}</h3>
                <p>{{ match.team1 }} vs {{ match.team2 }}</p>
                <p>Odds for {{ match.team1 }}: {{ match.odds_team1 }}</p>
                <p>Odds for {{ match.team2 }}: {{ match.odds_team2 }}</p>
                <form action="/place_bet" method="post">
                    <input type="hidden" name="match_id" value="{{ match.id }}">
                    <label for="team">Select Team:</label>
                    <select name="team">
                        <option value="team1">Team A</option>
                        <option value="team2">Team B</option>
                    </select>
                    <br>
                    <label for="amount">Enter Bet Amount:</label>
                    <input type="number" name="amount" step="0.01" min="0" required>
                    <br>
                    <input type="submit" value="Place Bet">
                </form>
                <p>Entertainment feature: {{ match.entertainment_feature }}</p>
            </div>
        {% endfor %}
    </div>

    <!-- Stored Bets -->
    <div>
        <h2>Stored Bets</h2>
        {% if bets %}
            <table>
                <thead>
                    <tr>
                        <th>Match ID</th>
                        <th>Team</th>
                        <th>Amount</th>
                    </tr>
                </thead>
                <tbody>
                    {% for bet in bets %}
                        <tr>
                            <td>{{ bet.match_id }}</td>
                            <td>{{ bet.team }}</td>
                            <td>{{ bet.amount }}</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        {% else %}
            <p>No bets placed yet.</p>
        {% endif %}
    </div>

    <!-- Finance Entertainment Graphical Picture -->
    <div class="graph">
        <img src="{{ url_for('static', filename='finance_entertainment_graph.png') }}" alt="Finance Entertainment Graph">
    </div>
</body>
</html>
