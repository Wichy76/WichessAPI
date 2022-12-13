import chess
import chess.pgn
from stockfish import Stockfish
from django.db import models
from django.db.models import *


class BoardModel(models.Model):
    FEN = TextField(default="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    theme = TextField(default="green")
    created_at = DateTimeField(auto_now=True)

    @classmethod
    def charge_fen(cls, fen):
        board = chess.Board(fen)

        board_data = {
            "FEN": fen,
            "turn": board.turn,
            "theme": '',
        }

        return cls(**board_data)

    def __str__(self):
        return self.FEN


class OpeningModel(models.Model):
    OPENING_CHOICES = [
        ("rnbqkbnr/ppp2ppp/4p3/3p4/3PP3/8/PPP2PPP/RNBQKBNR w KQkq d6 0 1", "French"),
        ("rnbqkb1r/ppp2ppp/4pn2/8/2pP4/5NP1/PP2PPBP/RNBQK2R b KQkq - 0 1", "Open_Catalan"),
        ("rnbqk2r/ppp1bppp/4pn2/3p4/2PP4/5NP1/PP2PPBP/RNBQK2R b KQkq - 0 1", "Closed_Catalan" )
    ]

    name = CharField(max_length=100, choices=OPENING_CHOICES)


class ComputerModel(models.Model):
    difficulty = IntegerField(default=100)

    STEREOTYPE_CHOICES = [
        ("A", "AGRESIVE"),
        ("P", "POSITIONAL"),
        ("E", "EQUILIBRATED"),
        ("T", "TEORICAL")
    ]
    stereotype = CharField(max_length=10, choices=STEREOTYPE_CHOICES)


class GameModel(models.Model):
    opening = OneToOneField(OpeningModel, on_delete=CASCADE)
    trainingMode = BooleanField(default=True)
    score = IntegerField(default=0)
    PGN = TextField(default=str(chess.pgn.Game()))
    created_at = DateTimeField(auto_now=True)
