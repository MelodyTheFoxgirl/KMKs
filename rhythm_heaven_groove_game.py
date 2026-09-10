from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import DefaultOnToggle, Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

# Based on the Rhythm Heaven Fever KMK

@dataclass
class RhythmHeavenGrooveArchipelagoOptions:
    rhythm_heaven_groove_frontside_enabled: RhythmHeavenGrooveFrontsideEnabled
    rhythm_heaven_groove_flipside_enabled: RhythmHeavenGrooveFlipsideEnabled
    rhythm_heaven_groove_perfects_enabled: RhythmHeavenGroovePerfectsEnabled
    rhythm_heaven_groove_night_modes_enabled: RhythmHeavenGrooveNightModesEnabled
    rhythm_heaven_groove_side_games_enabled: RhythmHeavenGrooveSideGamesEnabled


class RhythmHeavenGrooveGame(Game):
    name = "Rhythm Heaven Groove"
    platform = KeymastersKeepGamePlatforms.SW

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = RhythmHeavenGrooveArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = []
        if self.frontside_enabled or not self.flipside_enabled:
            templates.extend([
                GameObjectiveTemplate(
                    label="Achieve RESULT in GAME",
                    data={
                        "RESULT": (self.frontside_results, 1),
                        "GAME": (self.frontside_games, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=100,
                ),
                
                GameObjectiveTemplate(
                    label="Achieve RESULT in Deep Sea (Other-4)",
                    data={
                        "RESULT": (self.frontside_results, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=5,
                ),
            ])

            if self.perfects_enabled:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Achieve a Perfect in GAME",
                        data={
                            "GAME": (self.frontside_games, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=20,
                    ),
                ])
                
            if self.night_modes_enabled:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Achieve RESULT in GAME with Night Mode enabled",
                        data={
                            "RESULT": (self.frontside_results, 1),
                            "GAME": (self.frontside_games, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=True,
                        weight=50,
                    ),
                ])
                
                if self.perfects_enabled:
                    templates.extend([
                        GameObjectiveTemplate(
                            label="Achieve a Perfect in GAME with Night Mode enabled",
                            data={
                                "GAME": (self.frontside_games, 1),
                            },
                            is_time_consuming=True,
                            is_difficult=True,
                            weight=10,
                        ),
                    ])

        if self.flipside_enabled:
            templates.extend([
                GameObjectiveTemplate(
                    label="Achieve RESULT in GAME",
                    data={
                        "RESULT": (self.flipside_results, 1),
                        "GAME": (self.flipside_games, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=100,
                ),
                
                GameObjectiveTemplate(
                    label="Achieve RESULT in Cast of Characters (Other-4)",
                    data={
                        "RESULT": (self.flipside_results, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=5,
                ),
            ])
            
            if self.perfects_enabled:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Achieve a Perfect in GAME",
                        data={
                            "GAME": (self.flipside_games, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=20,
                    ),
                ])
            
            if self.night_modes_enabled:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Achieve RESULT in GAME with Night Mode enabled",
                        data={
                            "RESULT": (self.flipside_results, 1),
                            "GAME": (self.flipside_games, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=True,
                        weight=50,
                    ),
                ])
                
                if self.perfects_enabled:
                    templates.extend([
                        GameObjectiveTemplate(
                            label="Achieve a Perfect in GAME with Night Mode enabled",
                            data={
                                "GAME": (self.flipside_games, 1),
                            },
                            is_time_consuming=True,
                            is_difficult=True,
                            weight=10,
                        ),
                    ])
            
        if self.side_games_enabled:
            if self.frontside_enabled or not self.flipside_enabled:
                templates.extend([
                    GameObjectiveTemplate(
                        label="In Who's Got Rhythm? (Rhythm Toy Box), Score at least SCORE points",
                        data={
                            "SCORE": (self.wgr_score, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=10,
                    ),
                    
                    GameObjectiveTemplate(
                        label="In Bouncy Puffer Fish (Rhythm Toy Box), tank at least AMOUNT fish",
                        data={
                            "AMOUNT": (self.fish, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=10,
                    ),
                    
                    GameObjectiveTemplate(
                        label="In Swing (Rhythm Toy Box), kick your shoe at least DISTANCE yards",
                        data={
                            "DISTANCE": (self.distance, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=10,
                    ),
                    
                    GameObjectiveTemplate(
                        label="In Owls (Rhythm Toy Box), match at least OWLS patterns",
                        data={
                            "OWLS": (self.owls, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=10,
                    ),
                    
                    GameObjectiveTemplate(
                        label="Spend a few minutes in SOUNDBOARD (Rhythm Toy Box)",
                        data={
                            "SOUNDBOARD": (self.soundboards, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=10,
                    ),
                    
                    GameObjectiveTemplate(
                        label="Complete CHAPTER in Beatspell",
                        data={
                            "CHAPTER": (self.early_beatspell, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=10,
                    ),
                    
                    GameObjectiveTemplate(
                        label="Complete CHAPTER in Beatspell",
                        data={
                            "CHAPTER": (self.late_beatspell, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=10,
                    ),
                    
                    GameObjectiveTemplate(
                        label="Do a Random Cave Quest in Beatspell",
                        data={
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=5,
                    ),
                ])
                
            if self.flipside_enabled:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Play a round of GAME (Score Attack)",
                        data={
                            "GAME": (self.score_attack_games, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=10,
                    ),
                    
                    GameObjectiveTemplate(
                        label="Complete LESSON (Drum Lessons)",
                        data={
                            "LESSON": (self.basic_lessons, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=10,
                    ),
                    
                    GameObjectiveTemplate(
                        label="Complete LESSON (Drum Lessons)",
                        data={
                            "LESSON": (self.advanced_lessons, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=10,
                    ),
                    
                    GameObjectiveTemplate(
                        label="Spend a few minutes in Free Jam (Drum Lessons)",
                        data={
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=10,
                    ),
                ])
            
        return templates

    @property
    def frontside_enabled(self) -> bool:
        return bool(self.archipelago_options.rhythm_heaven_groove_frontside_enabled.value)
        
    @property
    def perfects_enabled(self) -> bool:
        return bool(self.archipelago_options.rhythm_heaven_groove_perfects_enabled.value)

    @property
    def flipside_enabled(self) -> bool:
        return bool(self.archipelago_options.rhythm_heaven_groove_flipside_enabled.value)
        
    @property
    def night_modes_enabled(self) -> bool:
        return bool(self.archipelago_options.rhythm_heaven_groove_night_modes_enabled.value)

    @property
    def side_games_enabled(self) -> bool:
        return bool(self.archipelago_options.rhythm_heaven_groove_side_games_enabled.value)

    @staticmethod
    def frontside_results() -> List[str]:
        return [
            "Good or better",
            "Really Good or better",
            "Amazing",
        ]

    @staticmethod
    def flipside_results() -> List[str]:
        return [
            "OK or better",
            "Just OK or better",
            "Superb",
        ]
    
    @staticmethod
    def frontside_games() -> List[str]:
        return [
            "Hoop Trundling (1-1)",
            "Brolly Good Show (1-2)",
            "Disc Dog (1-3)",
            "Feeding the Beast (1-4)",
            "Remix 1 (1-5)",
            "Ribbit Rocket (2-1)",
            "Stop N Go N Stop (2-2)",
            "Hop N Slide (2-3)",
            "Pop, Don't Drop (2-4)",
            "Remix 2 (2-5)",
            "Slice N Dice Kitchen (3-1)",
            "Sneezy Moon (3-2)",
            "Crab Snacks (3-3)",
            "Hop, Stop N Roll (3-4)",
            "Remix 3 (3-5)",
            "Fruit Flex (4-1)",
            "Alien Alphabet (4-2)",
            "Can Do (4-3)",
            "Backup Spotlight (4-4)",
            "Remix 4 (4-5)",
            "Flutter Speed (5-1)",
            "Lightning Bolting (5-2)",
            "Yum-Bot Simulator (5-3)",
            "Wiper Bosses (5-4)",
            "Remix 5 (5-5)",
            "Soccer Dreams (6-1)",
            "Sweeper Star (6-2)",
            "A for Effort (6-3)",
            "Spirit Slasher (6-4)",
            "Remix 6 (6-5)",
            "Stop N Go N Stop 2 (7-1)",
            "Fruit Flex 2 (7-2)",
            "Hop, Stop N Roll 2 (7-3)",
            "Brolly Good Show 2 (7-4)",
            "Remix 7 (7-5)",
            "Yum-Bot Simulator 2 (8-1)",
            "Sneezy Moon 2 (8-2)",
            "Ribbit Rocket 2 (8-3)",
            "Alien Alphabet 2 (8-4)",
            "Remix 8 (8-5)",
        ]
    
    @staticmethod
    def flipside_games() -> List[str]:
        return [
            "Hoop Trundling 2 (9-1)",
            "Backup Spotlight 2 (9-2)",
            "Flutter Speed 2 (9-3)",
            "Quick Hands (9-4)",
            "Remix 9 (9-5)",
            "Sweeper Star 2 (10-1)",
            "Hop N Slide 2 (10-2)",
            "Lightning Bolting 2 (10-3)",
            "Soda Hop (10-4)",
            "Remix 10 (10-5)",
            "Soccer Dreams 2 (11-1)",
            "Disc Dog 2 (11-2)",
            "Crab Snacks 2 (11-3)",
            "Space Sentry (11-4)",
            "Remix 11 (11-5)",
            "Quick Hands 2 (12-1)",
            "Spirit Slasher 2 (12-2)",
            "Wiper Bosses 2 (12-3)",
            "High-Five Fever (12-4)",
            "Remix 12 (12-5)",
            "Can Do 2 (13-1)",
            "Soda Hop 2 (13-2)",
            "A for Effort 2 (13-3)",
            "Germ Aerobics (13-4)",
            "Remix 13 (13-5)",
            "Space Sentry 2 (14-1)",
            "Slice N Dice Kitchen 2 (14-2)",
            "Pop, Don't Drop 2 (14-3)",
            "Synchro Wings (14-4)",
            "Remix 14 (14-5)",
            "Germ Aerobics 2 (15-1)",
            "Feeding the Beast 2 (15-2)",
            "High-Five Fever 2 (15-3)",
            "Synchro Wings 2 (15-4)",
            "Remix 15 (15-5)",
            "Remix 16 (16-1)",
            "Remix 17 (16-2)",
            "Remix 18 (16-3)",
            "Remix 19 (16-4)",
            "Remix 20 (16-5)",
        ]

    @staticmethod
    def wgr_score() -> range:
        return range(5, 21)

    @staticmethod
    def fish() -> range:
        return range(2, 9)

    @staticmethod
    def distance() -> List[str]:
        return [
            "100",
            "150",
            "200",
            "250",
            "300",
            "350",
        ]

    @staticmethod
    def owls() -> range:
        return range(3, 9)
    
    @staticmethod
    def soundboards() -> List[str]:
        return [
            "Soundboard",
            "Soundboard 2",
            "Soundboard 3",
        ]
    
    @staticmethod
    def early_beatspell() -> List[str]:
        return [
            "Chapter 1: Awakening",
            "Chapter 2: Healing Magic",
            "Chapter 3: The Fire Monster",
            "Chapter 4: The Fourth Fear!",
        ]
    
    @staticmethod
    def late_beatspell() -> List[str]:
        return [
            "Chapter 5: New Awakening",
            "Chapter 6: Backflip the Script",
            "Chapter 7: Spell Boosts",
            "Final Chapter: Showdown",
        ]
    
    @staticmethod
    def score_attack_games() -> List[str]:
        return [
            "Can You Clap It?",
            "Sensei Sparring",
            "Can You Clap It? 2",
            "Skateboarding",
            "Can You Clap It? 3",
            "Brolly Good Encore",
            "Skateboarding 2",
            "Firing Frenzy",
        ]
    
    @staticmethod
    def basic_lessons() -> List[str]:
        return [
            "Snare Drum",
            "Kick Drim",
            "Cymbals",
            "Floor Tom",
            "High Tom",
            "Hi-Hat",
            "Double Bass Pedal",
        ]
    
    @staticmethod
    def advanced_lessons() -> List[str]:
        return [
            "Bossa Nova Rhythm",
            "Technical Skills (Pt. 1)",
            "Technical Skills (Pt. 2)",
            "Adv. Double Bass Pedal (Pt. 1)",
            "Adv. Double Bass Pedal (Pt. 2)",
            "Otherworldly Skill",
        ]

# Archipelago Options
class RhythmHeavenGrooveFrontsideEnabled(DefaultOnToggle):
    """
    Indicates whether to include the Frontside levels in objectives
    Will be forced on if the Flipside is disabled
    """

    display_name = "Rhythm Heaven Groove Perfects Enabled"

class RhythmHeavenGroovePerfectsEnabled(Toggle):
    """
    Indicates whether Perfects should be included in objectives
    """

    display_name = "Rhythm Heaven Groove Perfects Enabled"

class RhythmHeavenGrooveFlipsideEnabled(DefaultOnToggle):
    """
    Indicates whether to include the Flipside levels in objectives
    If false, the Frontside is forced on
    """
    
    display_name = "Rhythm Heaven Groove Flipside Enabled"
    
class RhythmHeavenGrooveNightModesEnabled(Toggle):
    """
    Indicates whether to include Night Mode in objectives
    """
    
    display_name = "Rhythm Heaven Groove Night Mode Enabled"

class RhythmHeavenGrooveSideGamesEnabled(Toggle):
    """
    Indicates whether to include side games (Beatspell, Score Attack, Drum Lessons) in objectives
    """
    
    display_name = "Rhythm Heaven Groove Side Games Enabled"
