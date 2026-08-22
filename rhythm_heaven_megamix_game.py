from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

# Based on the Rhythm Heaven Fever KMK

@dataclass
class RhythmHeavenMegamixArchipelagoOptions:
    rhythm_heaven_megamix_perfects_enabled: RhythmHeavenMegamixPerfectsEnabled
    rhythm_heaven_megamix_heaven_world_enabled: RhythmHeavenMegamixHeavenWorldEnabled
    rhythm_heaven_megamix_challenge_land_enabled: RhythmHeavenMegamixChallengeLandEnabled
    rhythm_heaven_megamix_shop_games_enabled: RhythmHeavenMegamixShopGamesEnabled


class RhythmHeavenMegamixGame(Game):
    name = "Rhythm Heaven Megamix"
    platform = KeymastersKeepGamePlatforms._3DS

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = RhythmHeavenMegamixArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Achieve RESULT in GAME",
                data={
                    "RESULT": (self.resultstar, 1),
                    "GAME": (self.earth_world_games, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=100,
            ),
            
            GameObjectiveTemplate(
                label="Achieve a flow of FLOW or better in GAME",
                data={
                    "FLOW": (self.flow_range, 1),
                    "GAME": (self.earth_world_games, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=100,
            ),
            
            GameObjectiveTemplate(
                label="Achieve RESULT in all games in SERIES",
                data={
                    "RESULT": (self.results, 1),
                    "SERIES": (self.earth_world_series, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=40,
            ),
            
            GameObjectiveTemplate(
                label="At the GATE, complete Saffron's trial",
                data={
                    "GATE": (self.gates, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
            
            GameObjectiveTemplate(
                label="At the GATE, complete Saltwater's trial",
                data={
                    "GATE": (self.gates, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
            
            GameObjectiveTemplate(
                label="At the GATE, complete Paprika's trial",
                data={
                    "GATE": (self.gates, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=20,
            ),
        ]

        if self.perfects_enabled:
            templates.extend([
                GameObjectiveTemplate(
                    label="Achieve a no-miss run in GAME",
                    data={
                        "GAME": (self.earth_world_games, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=20,
                ),
            ])

        if self.heaven_world_enabled:
            templates.extend([
                GameObjectiveTemplate(
                    label="Achieve RESULT in GAME",
                    data={
                        "RESULT": (self.resultstar, 1),
                        "GAME": (self.heaven_world_games, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=50,
                ),
                
                GameObjectiveTemplate(
                    label="Achieve a flow of FLOW or better in GAME",
                    data={
                        "FLOW": (self.flow_range, 1),
                        "GAME": (self.heaven_world_games, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=50,
                ),
                
                GameObjectiveTemplate(
                    label="Achieve RESULT in all games in SERIES",
                    data={
                        "RESULT": (self.results, 1),
                        "SERIES": (self.heaven_world_series, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=20,
                ),
                
                GameObjectiveTemplate(
                    label="At the fourth gate (Clap Trap), complete Saffron's trial",
                    data={},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=10,
                ),
                
                GameObjectiveTemplate(
                    label="At the fourth gate (Clap Trap), complete Saltwater's trial",
                    data={},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=10,
                ),
                
                GameObjectiveTemplate(
                    label="At the fourth gate (Clap Trap), complete Paprika's trial",
                    data={},
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=10,
                ),
            ])
            
            if self.perfects_enabled:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Achieve a no-miss run in GAME",
                        data={
                            "GAME": (self.heaven_world_games, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=10,
                    ),
                ])
        
        if self.shop_games_enabled:
            templates.extend([
                GameObjectiveTemplate(
                    label="Achieve RESULT in GAME",
                    data={
                        "RESULT": (self.resultstar, 1),
                        "GAME": (self.shop_games, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=30,
                ),
                
                GameObjectiveTemplate(
                    label="Achieve a flow of FLOW or better in GAME",
                    data={
                        "FLOW": (self.flow_range, 1),
                        "GAME": (self.shop_games, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=30,
                ),
            ])
            
            if self.perfects_enabled:
                templates.extend([
                    GameObjectiveTemplate(
                        label="Achieve a no-miss run in GAME",
                        data={
                            "GAME": (self.shop_games, 1),
                        },
                        is_time_consuming=True,
                        is_difficult=True,
                        weight=10,
                    ),
                    
                ])
        
        if self.challenge_land_enabled:
            templates.extend([
                GameObjectiveTemplate(
                    label="Complete CHALLENGE in Saffron World",
                    data={
                        "CHALLENGE": (self.saffron_normal_challenges, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=7,
                ),
                
                GameObjectiveTemplate(
                    label="Complere CHALLENGE in Saffron World",
                    data={
                        "CHALLENGE": (self.saffron_hard_challenges, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3,
                ),
                
                GameObjectiveTemplate(
                    label="Complete CHALLENGE in Saltwater World",
                    data={
                        "CHALLENGE": (self.saltwater_normal_challenges, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=7,
                ),
                
                GameObjectiveTemplate(
                    label="Complete CHALLENGE in Saltwater World",
                    data={
                        "CHALLENGE": (self.saltwater_long_challenges, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=5,
                ),
                
                GameObjectiveTemplate(
                    label="Complete CHALLENGE in Saltwater World",
                    data={
                        "CHALLENGE": (self.saltwater_hard_challenges, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=1,
                ),
                
                GameObjectiveTemplate(
                    label="Complete CHALLENGE in Saltwater World",
                    data={
                        "CHALLENGE": (self.saltwater_long_hard_challenges, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=2,
                ),
                
                GameObjectiveTemplate(
                    label="Complete CHALLENGE in Paprika World",
                    data={
                        "CHALLENGE": (self.paprika_normal_challenges, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=5,
                ),
                
                GameObjectiveTemplate(
                    label="Complete CHALLENGE in Paprika World",
                    data={
                        "CHALLENGE": (self.paprika_long_challenges, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=6,
                ),
                
                GameObjectiveTemplate(
                    label="Complete CHALLENGE in Paprika World",
                    data={
                        "CHALLENGE": (self.paprika_hard_challenges, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=2,
                ),
                
                GameObjectiveTemplate(
                    label="Complete CHALLENGE in Paprika World",
                    data={
                        "CHALLENGE": (self.paprika_long_hard_challenges, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=2,
                ),
            ])
            
        return templates

    @property
    def perfects_enabled(self) -> bool:
        return bool(self.archipelago_options.rhythm_heaven_megamix_perfects_enabled.value)

    @property
    def heaven_world_enabled(self) -> bool:
        return bool(self.archipelago_options.rhythm_heaven_megamix_heaven_world_enabled.value)
        
    @property
    def challenge_land_enabled(self) -> bool:
        return bool(self.archipelago_options.rhythm_heaven_megamix_challenge_land_enabled.value)

    @property
    def shop_games_enabled(self) -> bool:
        return bool(self.archipelago_options.rhythm_heaven_megamix_shop_games_enabled.value)

    @staticmethod
    def results() -> List[str]:
        return [
            "OK or better",
            "Superb or better",
        ]

    @staticmethod
    def resultstar() -> List[str]:
        return [
            "OK or better",
            "OK or better",
            "OK or better and hit the Skill Star",
            "Superb or better",
            "Superb or better",
            "Superb or better and hit the Skill Star",
        ]

    @staticmethod
    def flow_range() -> range:
        return range(70, 86)
    
    @staticmethod
    def earth_world_games() -> List[str]:
        return [
            "Karate Man (Honeybee Land)",
            "Fillbots (Honeybee Land)",
            "Air Rally (Honeybee Land)",
            "Catchy Tune (Honeybee Land)",
            "Rhythm Tweezers (Machine Land)",
            "Glee Club (Machine Land)",
            "Figure Fighter (Machine Land)",
            "Fruit Basket (Machine Land)",
            "The Clappy Trio (Citrus Land)",
            "Shoot-'em-up (Citrus Land)",
            "Micro-Row (Citrus Land)",
            "First Contact (Citrus Land)",
            "Bunny Hop (Donut Land)",
            "Airborder (Donut Land)",
            "Exhibition Match (Donut Land)",
            "Tongue Lashing (Donut Land)",
            "Sneaky Spirits (Barbershop Land)",
            "Rhythm Rally (Barbershop Land)",
            "Flipper-Flop (Barbershop Land)",
            "LumBEARjack (Barbershop Land)",
            "Power Calligraphy (Songbird Land)",
            "Blue Birds (Songbird Land)",
            "Flock Step (Songbird Land)",
            "Super Samurai Slice (Songbird Land)",
            "Spaceball (Lush Tower)",
            "Dog Ninja (Lush Tower)",
            "Hole in One (Lush Tower)",
            "Sumo Brothers (Lush Tower)",
            "Lush Remix (Lush Tower)",
            "Karate Man Returns! (Honeybee Tower)",
            "Fillbots 2 (Honeybee Tower)",
            "Air Rally 2 (Honeybee Tower)",
            "Catchy Tune 2 (Honeybee Tower)",
            "Honeybee Remix (Honeybee Tower)",
            "Rhythm Tweezers 2 (Machine Tower)",
            "Glee Club 2 (Machine Tower)",
            "Figure Fighter 2 (Machine Tower)",
            "Fruit Basket 2 (Machine Tower)",
            "Machine Remix (Machine Tower)",
            "The Clappy Trio 2 (Citrus Tower)",
            "Shoot-'em-up 2 (Citrus Tower)",
            "Micro-Row 2 (Citrus Tower)",
            "Second Contact (Citrus Tower)",
            "Citrus Remix (Citrus Tower)",
            "Rat Race (Donut Tower)",
            "Fan Club (Donut Tower)",
            "Working Dough (Donut Tower)",
            "Animal Acrobat (Donut Tower)",
            "Donut Remix (Donut Tower)",
            "Sneaky Spirits 2 (Barbershop Tower)",
            "Rhythm Rally 2 (Barbershop Tower)",
            "Flipper-Flop 2 (Barbershop Tower)",
            "LumBEARjack 2 (Barbershop Tower)",
            "Barbershop Remix (Barbershop Tower)",
            "Tap Trial (Songbird Tower)",
            "Frog Hop (Songbird Tower)",
            "Ringside (Songbird Tower)",
            "Tangotronic 3000 (Songbird Tower)",
            "Songbird Remix (Songbird Tower)",
        ]
    
    @staticmethod
    def gates() -> List[str]:
        return [
            "first gate (Coin Toss)",
            "second gate (Sick Beats)",
            "third gate (Charging Chicken",
        ]
    
    @staticmethod
    def earth_world_series() -> List[str]:
        return [
            "Honeybee Land",
            "Machine Land",
            "Citrus Land",
            "Donut Land",
            "Barbershop Land",
            "Songbird Land",
            "Lush Tower",
            "Honeybee Tower",
            "Machine Tower",
            "Citrus Tower",
            "Donut Tower",
            "Barbershop Tower",
            "Songbird Tower",
        ]
    
    @staticmethod
    def heaven_world_games() -> List[str]:
        return [
            "Ninja Bodyguard (Star Land)",
            "Freeze Frame (Star Land)",
            "Launch Party (Star Land)",
            "Pajama Party (Star Land)",
            "Marching Orders (Comet Land)",
            "Munchy Monk (Comet Land)",
            "See-Saw (Comet Land)",
            "Blue Bear (Comet Land)",
            "Space Dance (Planet Land)",
            "Lockstep (Planet Land)",
            "Cheer Readers (Planet Land)",
            "Kitties! (Planet Land)",
            "The Snappy Trio (Left-Hand Tower)",
            "Fan Club 2 (Left-Hand Tower)",
            "Figure Fighter 3 (Left-Hand Tower)",
            "Jungle Gymnast (Left-Hand Tower)",
            "Left-Hand Remix (Left-Hand Tower)",
            "Tap Trial 2 (Right-Hand Tower)",
            "Jumpin' Jazz (Right-Hand Tower)",
            "Hole in One 2 (Right-Hand Tower)",
            "Super Samurai Slice 2 (Right-Hand Tower)",
            "Right-Hand Remix (Right-Hand Tower)",
            "Cosmic Dance (Tibby's Mom)",
            "Cosmic Rhythm Rally (Tibby's Mom)",
            "Working Dough 2 (Tibby's Mom)",
            "Karate Man Senior (Tibby's Mom)",
            "Final Remix (Tibby's Mom)",
        ]
    
    @staticmethod
    def heaven_world_series() -> List[str]:
        return [
            "Star Land",
            "Comet Land",
            "Planet Land",
            "Left-Hand Tower",
            "Right-Hand Tower",
            "Tibby's Mom",
        ]
    
    @staticmethod
    def shop_games() -> List[str]:
        return [
            "Bouncy Road (Shop Game)",
            "Night Walk (Shop Game)",
            "Quiz Show (Shop Game)",
            "The Dazzles (Shop Game)",
            "Big Rock Finish (Shop Game)",
            "Karate Man Kicks! (Shop Game)",
            "Built to Scale (Shop Game)",
            "Double Date (Shop Game)",
            "Catch of the Day (Shop Game)",
            "Fork Lifter (Shop Game)",
            "Love Rap (Shop Game)",
            "Bossa Nova (Shop Game)",
            "Screwbot Factory (Shop Game)",
            "Board Meeting (Shop Game)",
            "Samurai Slice (Shop Game)",
            "Packing Pests (Shop Game)",
            "Monkey Watch (Shop Game)",
            "Karate Man Combos! (Shop Game)",
        ]
    
    @staticmethod
    def saffron_normal_challenges() -> List[str]:
        return [
            "Simplicity Is Best",
            "Punch! Shoot! Smack!",
            "Bringing Topknots Back",
            "Aim True",
            "Pattern Play",
            "A Tale of Dietary Fiber",
            "Master of the Delayed Response",
        ]
    
    @staticmethod
    def saffron_hard_challenges() -> List[str]:
        return [
            "Group Activity (Super Hard!)",
            "Monster Maw (Super Hard!)",
            "Game Gamble: Beginner (Super Hard!)",
        ]
    
    @staticmethod
    def saltwater_normal_challenges() -> List[str]:
        return [
            "The Soul of Japan",
            "All Singing, All Dancing",
            "Full-Belly Dojo",
            "Round Object Fan Club",
            "Factory Tourism",
            "On the Job",
            "Monster Maw 2",
        ]
    
    @staticmethod
    def saltwater_long_challenges() -> List[str]:
        return [
            
            "Getting Vocal",
            "Be a Good Sport",
            "So Many Monkeys!",
            "Remix Medley",
            "That's Show Biz!",
        ]
        
    @staticmethod
    def saltwater_hard_challenges() -> List[str]:
        return [
            "Game Gamble: Intermediate (Super Hard!)",
        ]
        
    @staticmethod
    def saltwater_long_hard_challenges() -> List[str]:
        return [
            "Extreme Sports (Super Hard!)",
            "Super Remix Medley (Super Hard!)",
        ]
    
    @staticmethod
    def paprika_normal_challenges() -> List[str]:
        return [
            "All or Nothing!",
            "Demon Slayer",
            "Tales of Romance",
            "Wario...Where?",
            "Wario...Where? 2: The Sequel",
        ]
    
    @staticmethod
    def paprika_long_challenges() -> List[str]:
        return [
            "Karate Man vs. the Monster",
            "Group Activity 2",
            "Getting Vocal 2",
            "Spaaaaaaaaaaaaaaace!",
            "Rhythm Safari",
            "Hello, Ladies...",
        ]
    
    @staticmethod
    def paprika_hard_challenges() -> List[str]:
        return [
            "Lockstep Lockdown (Super Hard!)",
            "Game Gamble: Advanced (Super Hard!)",
        ]
        
    @staticmethod
    def paprika_long_hard_challenges() -> List[str]:
        return [
            "Back and So Forth (Super Hard!)",
            "Copycats (Super Hard!)",
        ]

# Archipelago Options
class RhythmHeavenMegamixPerfectsEnabled(Toggle):
    """
    Indicates whether No-Miss runs should be included in objectives
    """

    display_name = "Rhythm Heaven Megamix Perfects Enabled"

class RhythmHeavenMegamixHeavenWorldEnabled(Toggle):
    """
    Indicates whether to include Heaven World levels and lands in objectives
    """
    
    display_name = "Rhythm Heaven Megamix Heaven World Enabled"
    
class RhythmHeavenMegamixChallengeLandEnabled(Toggle):
    """
    Indicates whether to include Challenge courses in objectives
    """
    
    display_name = "Rhythm Heaven Megamix Challenge Land Enabled"

class RhythmHeavenMegamixShopGamesEnabled(Toggle):
    """
    Indicates whether to include games buyable in the shop in objectives
    """
    
    display_name = "Rhythm Heaven Megamix Shop Games Enabled"
