from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dice_roller():
    result = ''
    dice_img = ''
    if request.method == 'POST':
        rolled = random.randint(1, 6)
        img_url = f"https://upload.wikimedia.org/wikipedia/commons/{get_wiki_dice_path(rolled)}"
        dice_img = f'<img src="{img_url}" alt="Dice {rolled}" class="dice-img">'
        result = f'''
            <div class="result">
                🎲 Kamu mendapat angka: <span class="rolled">{rolled}</span><br>
                {dice_img}
            </div>
        '''

    return f'''
        <html>
        <head>
            <title>Dice Roller</title>
            <style>
                body {{
                    font-family: 'Segoe UI', sans-serif;
                    background: #f5f7fa;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                }}
                form {{
                    background: white;
                    padding: 20px;
                    border-radius: 12px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                    text-align: center;
                }}
                select, button {{
                    font-size: 16px;
                    padding: 8px;
                    margin: 10px 0;
                    border-radius: 6px;
                    border: 1px solid #ccc;
                }}
                .result {{
                    margin-top: 20px;
                    font-size: 20px;
                    color: #2c3e50;
                    font-weight: bold;
                    background: #ecf0f1;
                    padding: 15px;
                    border-radius: 8px;
                    text-align: center;
                }}
                .rolled {{
                    color: #e74c3c;
                    font-size: 28px;
                }}
                .dice-img {{
                    display: block;
                    margin: 0 auto;
                    width: 100px;
                }}
            </style>
        </head>
        <body>
            <h1>🎲 Dice Roller (d6)</h1>
            <form method="post">
                <p><strong>Lempar dadu 6-sisi:</strong></p>
                <button type="submit">🎲 Lempar!</button>
            </form>
            {result}
        </body>
        </html>
    '''

# URL path for Wikimedia dice images
def get_wiki_dice_path(value):
    dice_map = {
        1: "2/2c/Alea_1.png",
        2: "3/3b/Alea_2.png",
        3: "2/2f/Alea_3.png",
        4: "8/8d/Alea_4.png",
        5: "5/55/Alea_5.png",
        6: "f/f4/Alea_6.png"
    }
    return dice_map[value]

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run()
