"""Game logic for Tic-Tac-Toe"""

import numpy as np

from flask import render_template_string

from ._games import Game


class TicTacToe(Game):
    def __init__(self):
        # constants to indicate which player is which
        self.player_o = 1
        self.player_x = 2

        # setup the tic-tac-toe board as a matrix of zeros
        self.board = np.zeros(shape=(3,3))


    def render(self) -> str:
        """Return the rendering of this game's current state."""
        # generate a template string of the current state of the board
        template_string = f"""
        <div class="grid grid-cols-3 grid-rows-3 gap-20">
            <div class="border-4 p-8">{self._get_player_board_position(0,0)}</div>
            <div class="border-4 p-8">{self._get_player_board_position(0,1)}</div>
            <div class="border-4 p-8">{self._get_player_board_position(0,2)}</div>
            <div class="row-start-2 border-4 p-8">{self._get_player_board_position(1,0)}</div>
            <div class="row-start-2 border-4 p-8">{self._get_player_board_position(1,1)}</div>
            <div class="row-start-2 border-4 p-8">{self._get_player_board_position(1,2)}</div>
            <div class="row-start-3 border-4 p-8">{self._get_player_board_position(2,0)}</div>
            <div class="row-start-3 border-4 p-8">{self._get_player_board_position(2,1)}</div>
            <div class="row-start-3 border-4 p-8">{self._get_player_board_position(2,2)}</div>
        </div>
        """
        return render_template_string(template_string)

    def next_turn(self):
        ...

    def _get_player_board_position(self, i: int, j: int) -> str:
        if self.board[i,j] == self.player_o:
            return '<img class="w-24 h-24" src="../assets/tic-tac-toe/o.svg"/>'
        if self.board[i,j] == self.player_x:
            return '<img class="w-24 h-24" src="../assets/tic-tac-toe/x.svg"/>'
        else:
            return '<div class="w-24 h-24"></div>'
