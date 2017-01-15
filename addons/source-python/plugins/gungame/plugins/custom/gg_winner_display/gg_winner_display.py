# ../gungame/plugins/custom/gg_winner_display/gg_winner_display.py

"""Plugin used to show a winner display page upon win."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
from urllib.parse import urlencode

# Source.Python
from events import Event
from listeners.tick import Delay

# GunGame
from gungame.core.messages import message_manager
from gungame.core.players.database import winners_database
from gungame.core.players.dictionary import player_dictionary

# Plugin
from .configuration import winner_page


# =============================================================================
# >> EVENTS
# =============================================================================
@Event('gg_win')
def gg_win(game_event):
    """Send the winner display for the individual winner."""
    winner = player_dictionary[game_event['winner']]
    loser = player_dictionary[game_event['loser']]
    places = len(winners_database)

    Delay(
        0.5,
        _send_motd,
        kwargs={
            'winnerName': winner.name,
            'loserName': loser.name,
            'wins': winner.wins,
            'place': winner.rank,
            'totalPlaces': places,
        }
    )


@Event('gg_team_win')
def gg_team_win(game_event):
    """Send the winner display for the winning team."""
    team = 'Terrorist' if game_event['winner'] == 2 else 'Counter-Terrorist'

    Delay(0.5, _send_motd, kwargs={'winningTeam': team})


# =============================================================================
# >> HELPER FUNCTIONS
# =============================================================================
def _send_motd(**kwargs):
    """Send the winner display page."""
    message_manager.motd_message(
        title='GunGame Winner',
        message='{url}?{query}'.format(
            url=winner_page.get_string(),
            query=urlencode(kwargs)
        )
    )
