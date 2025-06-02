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
from gungame.core.messages.manager import message_manager
from gungame.core.players.database import winners_database
from gungame.core.players.dictionary import player_dictionary
from gungame.core.teams import team_names

# Plugin
from .configuration import winner_page


# =============================================================================
# >> EVENTS
# =============================================================================
@Event("gg_win")
def gg_win(game_event):
    """Send the winner display for the individual winner."""
    winner = player_dictionary[game_event["winner"]]
    try:
        loser = player_dictionary[game_event["loser"]].name
    except ValueError:
        loser = ""
    places = len(winners_database)

    Delay(
        0.5,
        _send_motd,
        kwargs={
            "winnerName": winner.name,
            "loserName": loser,
            "wins": winner.wins,
            "place": winner.rank,
            "totalPlaces": places,
        },
    )


@Event("gg_team_win")
def gg_team_win(game_event):
    """Send the winner display for the winning team."""
    Delay(
        delay=0.5,
        callback=_send_motd,
        kwargs={"winningTeam": team_names.get(game_event["winner"])},
    )


# =============================================================================
# >> HELPER FUNCTIONS
# =============================================================================
def _send_motd(**kwargs):
    """Send the winner display page."""
    message_manager.motd_message(
        title="GunGame Winner",
        message=f"{str(winner_page)}?{urlencode(kwargs)}",
    )
