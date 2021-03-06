import unittest
from dotenv import load_dotenv
load_dotenv()

# Import test classes
from tests.player_test import TestPlayer
from tests.team_test import TestTeam
from tests.player_team_test import TestPlayerTeam
from tests.league_test import TestLeague
from tests.group_test import TestGroup
from tests.player_group_test import TestPlayerGroup
from tests.match_test import TestMatch
from tests.prediction_test import TestPrediction
from tests.player_league_test import TestPlayerLeague

if __name__ == "__main__":
    unittest.main()