from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🍽️ My Food Blog</h1>
    <p>Welcome to my simple food blog!</p>

    <h2>Recipes</h2>
    <ul>
        <li>Margherita Pizza</li>
        <li>Chocolate Cake</li>
        <li>Pasta Alfredo</li>
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)
