from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return HOME_HTML

HOME_HTML = """
     <html><body>
         <h2>Seja bem-vindo!</h2>
         <form action="/greet">
             Qual é o seu nome? <input type='text' name='username' size=(20,1)><br>
             O que você gostaria de comer hoje? <input type='text' name='favfood' size=(20,1)><br>
             <input type='submit' value='Continue'>
         </form>
     </body></html>"""

@app.route('/greet')
def greet():
    username = request.args.get('username', '')
    favfood = request.args.get('favfood', '')
    if username == '':
         username = 'World'
    if favfood == '':
         msg = 'Você não me disse o que gostaria de comer.'
    else:
         msg = 'A eu gosto de ' + favfood + ', também.'

    return GREET_HTML.format(username, msg)

GREET_HTML = """
    <html><body>
         <h2>Hello, {0}!</h2>
         {1}
    </body></html>
     """

if __name__ == "__main__":
     # Launch the Flask dev server
     app.run(host="localhost", debug=True)