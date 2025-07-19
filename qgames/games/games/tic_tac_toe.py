"""Game logic for Tic-Tac-Toe."""

import numpy as np

from flask import render_template_string

from ._games import Game


class TicTacToe(Game):
    def __init__(
        self,
        player_o: int = 1,
        player_x: int = 2,
    ) -> None:
        """Constructor for the TicTacToe game.
        
        Parameters
        ----------
        player_o : int
            Constant that represents player O.
        player_x : int
            Constant that represents player X.
        """
        # constants to indicate which player is which
        self.player_o = player_o
        self.player_x = player_x

        # setup the tic-tac-toe board as a matrix of zeros
        # (for now, we assume we only ever want to play a 3x3
        # game of Tic-Tac-Toe. If this is to be changed, a
        # higher dimensional game should be implemented elsewhere!)
        self.board = np.zeros(shape=(3,3))


    def render(self) -> str:
        """Return the rendering of this game's current state."""
        # generate a template string of the current state of the board
        BORDER_WIDTH: int = 4
        BORDER_COLOR: str = f"border-black"
        BORDER_PADDING: str = f"p-16"
        GRID_GAP: str = "gap-0"

        BORDER_L: str = f"border-l-{BORDER_WIDTH} {BORDER_COLOR} {BORDER_PADDING}"
        BORDER_R: str = f"border-r-{BORDER_WIDTH} {BORDER_COLOR} {BORDER_PADDING}"
        BORDER_T: str = f"border-t-{BORDER_WIDTH} {BORDER_COLOR} {BORDER_PADDING}"
        BORDER_B: str = f"border-b-{BORDER_WIDTH} {BORDER_COLOR} {BORDER_PADDING}"
        
        # return a template string to be rendered as HTML on the frontend side
        template_string = f"""
        <div class="grid grid-cols-3 grid-rows-3 {GRID_GAP}">
            <div class="{BORDER_R} {BORDER_B}">{self._get_player_board_position(0,0)}</div>
            <div class="{BORDER_L} {BORDER_B} {BORDER_R}">{self._get_player_board_position(0,1)}</div>
            <div class="{BORDER_L} {BORDER_B}">{self._get_player_board_position(0,2)}</div>
            <div class="row-start-2 {BORDER_T} {BORDER_B} {BORDER_R}">{self._get_player_board_position(1,0)}</div>
            <div class="row-start-2 {BORDER_T} {BORDER_B} {BORDER_R} {BORDER_L}">{self._get_player_board_position(1,1)}</div>
            <div class="row-start-2 {BORDER_T} {BORDER_B} {BORDER_L}">{self._get_player_board_position(1,2)}</div>
            <div class="row-start-3 {BORDER_T} {BORDER_R}">{self._get_player_board_position(2,0)}</div>
            <div class="row-start-3 {BORDER_T} {BORDER_R} {BORDER_L}">{self._get_player_board_position(2,1)}</div>
            <div class="row-start-3 {BORDER_T} {BORDER_L}">{self._get_player_board_position(2,2)}</div>
        </div>
        """
        return render_template_string(template_string)

    def next_turn(self):
        ...

    def _get_player_board_position(
        self, 
        i: int, 
        j: int
    ) -> str:
        """Returns a rendering for a board position.
        
        Given a board position indexed by i and j, return a
            rendering for the player at that position.
        
        Parameters
        ----------
        i : int
            Board row index.
        j : int
            Board column index.

        Raises
        ------
        IndexError
            If the supplied index is not within the bounds of the board,
            raises an IndexError.

        Returns
        -------
        rendering : str
            The HTML rendering for that board position.
        """
        if (i < 0) or (i > self.board.shape[0] - 1) or (j < 0 or (j > self.board.shape[1] - 1)):
            raise IndexError(f"Index ({i},{j}) not within bounds of 3x3 board.")
        
        WIDTH: int = 24
        HEIGHT: int = 24

        # check which player is in the board position and return that rendering.
        # these assets are relative to frontend/js/main.js
        if self.board[i,j] == self.player_o:
            return f"<img class='w-{WIDTH} h-{HEIGHT}' src='../assets/tic-tac-toe/o.svg'/>"
        if self.board[i,j] == self.player_x:
            return f"<img class='w-{WIDTH} h-{HEIGHT}' src='../assets/tic-tac-toe/x.svg'/>"
        else:
            return f"<div class='w-{WIDTH} h-{HEIGHT}'></div>"
