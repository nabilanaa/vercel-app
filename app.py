from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dice_roller():
    result = ''
    if request.method == 'POST':
        dice = int(request.form['dice'])
        rolled = random.randint(1, dice)
        result = f'<p>🎲 Kamu melempar dadu {dice}-sisi dan mendapat: <strong>{rolled}</strong></p>'
    
    return f'''
        <h1>🎲 Dice Roller</h1>
        <form method="post">
            <label>Pilih jenis dadu:</label>
            <select name="dice">
                <option value="6">d6</option>
                <option value="10">d10</option>
                <option value="20">d20</option>
            </select>
            <button type="submit">Lempar!</button>
        </form>
        {result}
    '''

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run()
