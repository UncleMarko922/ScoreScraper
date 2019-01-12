from bs4 import BeautifulSoup
import requests
import urllib


def get_soup():
    url = "https://www.thescore.com/nhl/events/date/2018-11-01"

    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")


def eat_soup(soup):
    teams = soup.find_all("div", {"class": "EventCard__teamName--JweK5"})
    scores = soup.find_all("div", {"class": "EventCard__score--2C1-p"})

    team_names = group_every_two_elems([team.text for team in teams])
    team_scores = group_every_two_elems([score.text for score in scores])
    print(team_names, team_scores)
    return team_names, team_scores


def group_every_two_elems(team_data):
    hacky_team_names = []
    for i, team in enumerate(team_data, start=1):
        if not i % 2:
            print(i)
            if i == 2:
                team_1 = team_data[0]
                team_2 = team_data[1]
            else:
                team_1 = team_data[i - 2]
                team_2 = team_data[i - 1]
            hacky_team_names.append(
                (team_1, team_2)
            )
    return hacky_team_names


def parse_results(team_data):
    team_names, team_scores = team_data
    list_results = []
    if team_scores and team_names:
        scores_and_names = zip(team_names, team_scores)
        for result in scores_and_names:
            results = {}
            results[result[0][0]] = result[1][0]
            results[result[0][1]] = result[1][1]
            list_results.append(results)
    return list_results


def get_scores():
    soup = get_soup()
    teams_and_scores = eat_soup(soup)
    return parse_results(teams_and_scores)

#
# if __name__ == '__main__':
#     get_scores()
