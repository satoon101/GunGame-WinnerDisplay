# ../gungame/plugins/custom/gg_winner_display/configuration.py

"""Creates the gg_winner_display configuration."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame
from gungame.core.config.manager import GunGameConfigManager

# Plugin
from .info import info


# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = (
)


# =============================================================================
# >> CONFIGURATION
# =============================================================================
with GunGameConfigManager(info.name) as _config:
    with _config.cvar(
        name='winner_page',
        default='http://gungame.net/gg5_win.php',
    ) as winner_page:
        winner_page.add_text()
