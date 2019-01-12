from score_alerts.scrapers.score_scraper import parse_results

def test_announce_results():
    expected = True
    mock_team_data = (['team 1', 'team 2'], ['300', '0'])
    result = parse_results(mock_team_data)
    assert result == expected

def test_announce_results_no_scores():
    expected = False
    mock_team_data = (['team 1', 'team 2'], [])
    result = parse_results(mock_team_data)
    assert result == expected

def test_announce_results_no_teams():
    expected = False
    mock_team_data = ([], ['300', '0'])
    result = parse_results(mock_team_data)
    assert result == expected