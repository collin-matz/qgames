from flask import (
    Flask,
    send_from_directory, 
    render_template
)

from games.tic_tac_toe import TicTacToe

class Webapp:
    def __init__(self):
        self.app = Flask(
            __name__, 
            static_folder="../frontend", 
            static_url_path="",
            template_folder="../frontend/templates"
        )
        self._setup_routes()

    def _setup_routes(self):
        """Setup the routing functions for the webapp."""
        @self.app.route("/")
        def index():
            return send_from_directory(self.app.static_folder, "index.html")

        @self.app.route("/about")
        def get_about():
            """Renders and returns the about template upon request."""
            return render_template("about.html")

        @self.app.route("/games")
        def get_games_list():
            """Renders and returns the games list template upon request."""
            return render_template("games.html")

        @self.app.route("/games/<game_id>", methods=["POST"])
        def get_game(game_id):
            """Given a game id, return the rendering for that game."""
            match game_id:
                case "tic-tac-toe":
                    game = TicTacToe()
                    return game.render()

    def run(self, host="127.0.0.1", port=5000, debug=True):
        self.app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    # setup and run webapp
    app = Webapp()
    app.run()
