from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class RhythmHeavenDSArchipelagoOptions:
    rhythm_heaven_ds_perfects_enabled: RhythmHeavenDSPerfectsEnabled
    
# Based very heavily on the Rhythm Heaven Fever KMK. In fact, only the level names were changed.
class RhythmHeavenDSGame(Game):
    name = "Rhythm Heaven"
    platform = KeymastersKeepGamePlatforms.NDS

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = RhythmHeavenDSArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Get RESULT in LEVEL",
                data={
                    "RESULT": (self.results, 1),
                    "LEVEL": (self.levels, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
        ]

        if self.perfects_enabled:
            templates.extend([
                GameObjectiveTemplate(
                    label="Get Perfect in LEVEL",
                    data={
                        "LEVEL": (self.levels_without_airboarder, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
            ])

        return templates

    @property
    def perfects_enabled(self) -> bool:
        return bool(self.archipelago_options.rhythm_heaven_ds_perfects_enabled.value)

    @staticmethod
    def results() -> List[str]:
        return [
            "OK or better",
            "Superb",
        ]

    @staticmethod
    def levels() -> List[str]:
        return [
            "Built to Scale",
            "Glee Club",
            "Fillbots",
            "Fan Club",
            "Remix 1",
            "Rhythm Rally",
            "Shoot-'Em-Up",
            "Blue Birds",
            "Moai Doo-Wop",
            "Remix 2",
            "Love Lizards",
            "Crop Stomp",
            "Freeze Frame",
            "The Dazzles",
            "Remix 3",
            "Munchy Monk",
            "DJ School",
            "Drummer Duel",
            "Love Lab",
            "Remix 4",
            "Splashdown",
            "Big Rock Finish",
            "Dog Ninja",
            "Frog Hop",
            "Remix 5",
            "Space Soccer",
            "Lockstep",
            "Rockers",
            "Karate Man",
            "Remix 6",
            "Built to Scale 2",
            "The Dazzles 2",
            "Frog Hop 2",
            "Fan Club 2",
            "Remix 7",
            "Rhythm Rally 2",
            "Fillbots 2",
            "Blue Birds 2",
            "Lockstep 2",
            "Remix 8",
            "Moai Doo-Wop 2",
            "Karate Man 2",
            "Glee Club 2",
            "Space Soccer 2",
            "Remix 9",
            "Shoot-'Em-Up 2",
            "Splashdown 2",
            "Munchy Monk 2",
            "Rockers 2",
            "Remix 10",
            "Airboarder",
        ]

    def levels_without_airboarder(self) -> List[str]:
        levels: List[str] = self.levels()[:]

        if "Airboarder" in levels:
            levels.remove("Airboarder")

        return levels


# Archipelago Options
class RhythmHeavenDSPerfectsEnabled(Toggle):
    """
    Indicates whether to include Perfects in objectives
    """

    display_name = "Rhythm Heaven DS Perfects Enabled"
