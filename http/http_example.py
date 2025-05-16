from flask import Flask, render_template

# Aplicación Flask simple para mostrar ítems
app = Flask(__name__)

# Datos de ejemplo
items = {
    1: "cal",
    2: "rir",
    3: "foo"
}

@app.route('/')
def show_items():
    """
    Ruta principal:
    Muestra la lista de ítems disponibles.
    """
    return render_template('items.html', items=items)

if __name__ == '__main__':
    # Ejecutar en localhost:5412
    app.run(host='127.0.0.1', port=5412, debug=True)