def get_team_abbreviation(team_name):
    if team_name == 'Arizona Cardinals' or team_name == ' St. Louis Cardinals':
        return 'ARI'
    elif team_name == 'Atlanta Falcons':
        return 'ATL'
    elif team_name == 'Baltimore Ravens':
        return 'BAL'
    elif team_name == 'Buffalo Bills':
        return 'BUF'
    elif team_name == 'Carolina Panthers':
        return 'CAR'
    elif team_name == 'Chicago Bears':
        return 'CHI'
    elif team_name == 'Cincinnati Bengals':
        return 'CIN'
    elif team_name == 'Cleveland Browns':
        return 'CLE'
    elif team_name == 'Dallas Cowboys':
        return 'DAL'
    elif team_name == 'Denver Broncos':
        return 'DEN'
    elif team_name == 'Detroit Lions':
        return 'DET'
    elif team_name == 'Green Bay Packers':
        return 'GB'
    elif team_name == 'Houston Texans':
        return 'HOU'
    elif team_name == 'Indianapolis Colts' or team_name == 'Baltimore Colts':
        return 'IND'
    elif team_name == 'Jacksonville Jaguars':
        return 'JAX'
    elif team_name == 'Kansas City Chiefs':
        return 'KC'
    elif team_name == 'Las Vegas Raiders' or team_name == 'Oakland Raiders':
        return 'LV'
    elif team_name == 'Los Angeles Chargers' or team_name == 'San Diego Chargers':
        return 'LAC'
    elif team_name == 'Los Angeles Rams' or team_name == 'St. Louis Rams':
        return 'LAR'
    elif team_name == 'Miami Dolphins':
        return 'MIA'
    elif team_name == 'Minnesota Vikings':
        return 'MIN'
    elif team_name == 'New England Patriots':
        return 'NE'
    elif team_name == 'New Orleans Saints':
        return 'NO'
    elif team_name == 'New York Giants':
        return 'NYG'
    elif team_name == 'New York Jets':
        return 'NYJ'
    elif team_name == 'Philadelphia Eagles':
        return 'PHI'
    elif team_name == 'Pittsburgh Steelers':
        return 'PIT'
    elif team_name == 'San Francisco 49ers':
        return 'SF'
    elif team_name == 'Seattle Seahawks':
        return 'SEA'
    elif team_name == 'Tampa Bay Buccaneers':
        return 'TB'
    elif team_name == 'Tennessee Titans' or team_name == 'Houston Oilers':
        return 'TEN'
    elif team_name == 'Washington Football Team' or team_name == 'Washington Redskins':
        return 'WAS'
    else:
        return None
