from flask import Flask
from registro import registros_bp

app = Flask(__name__)

# Registrar el Blueprint de registros
app.register_blueprint(registros_bp)

if __name__ == '__main__':
    app.run(debug=True)
