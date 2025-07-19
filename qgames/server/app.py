"""Code for running the Python webserver."""

from flask import (
    Flask,
    send_from_directory, 
    render_template
)

from games import TicTacToe


class Webapp:
    """Class to maintain the logic of the webserver."""
    def __init__(
        self,
        static_folder: str = "../frontend/",
        static_url_path: str = "",
        template_folder: str = "../frontend/templates/"
    ) -> None:
        """Constructor for Webapp."""
        # initialize the Flask webapp. point the static
        # and template folders to the frontend where all
        # html, css, and js code live
        self.static_folder = static_folder
        self.static_url_path = static_url_path
        self.template_folder = template_folder

        self.app = Flask(
            __name__, 
            static_folder=self.static_folder, 
            static_url_path=self.static_url_path,
            template_folder=self.template_folder
        )

        # setup the routes for the webapp
        self._setup_routes()


    def _setup_routes(self) -> None:
        """Setup the routing functions for Webapp.
        
        This is to be called once at initialization by the constructor.
        """
        @self.app.route("/")
        def get_index():
            return send_from_directory(self.static_folder, "index.html")

        @self.app.route("/about")
        def get_about():
            return render_template("about.html")

        @self.app.route("/games")
        def get_games_list():
            return render_template("games.html")

        @self.app.route("/games/<game_id>", methods=["POST"])
        def get_game(game_id):
            match game_id:
                case "tic-tac-toe":
                    game = TicTacToe()
                    return game.render()


    def run(
        self, 
        host: str = "127.0.0.1", 
        port: int = 5000, 
        debug: bool = True
    ) -> None:
        """Calls run on the webapp.
        
        Parameters
        ----------
        host : str
            Host URL for the webapp.
        port : int
            Port for the webapp.
        debug : bool
            Specifies whether to run in debug mode or not.
        """
        self.app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    # setup and run webapp
    app = Webapp()
    app.run()
