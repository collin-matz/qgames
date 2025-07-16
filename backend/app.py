from flask import (
    Flask, 
    jsonify,
    send_from_directory, 
    render_template
)

app = Flask(
    __name__, 
    static_folder="../frontend", 
    static_url_path="",
    template_folder="../frontend/templates"
)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/about")
def get_about():
    """Renders and returns the about template upon request."""
    return render_template("about.html")

@app.route("/games")
def get_games_list():
    """Renders and returns the games list template upon request."""
    return render_template("games.html")

@app.route("/games/<game_id>", methods=["POST"])
def get_game(game_id):
    print(f"User clicked game {game_id}")
    return jsonify({"message": f"Received click for item {game_id}"})


if __name__ == "__main__":
    app.run(debug=True)
