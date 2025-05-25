from flask import Flask
from data.data_productos import productos, categorias

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hola, soy Julián Martínez</h1>
    <p>Estudiante de la Tecnicatura en Desarrollo Web.</p>
    <p>Esta es mi primera aplicación usando Flask.</p>
    """

@app.route("/productos")
def listar_productos():
    resultado = "<h2>Lista de Productos</h2>"
    for producto in productos:
        resultado += f"<p>ID: {producto['id']} - Descripción: {producto['descripcion']} - Categoría ID: {producto['categoria_id']}</p>"
    return resultado

@app.route("/categorias")
def listar_categorias():
    resultado = "<h2>Lista de Categorías</h2>"
    for categoria in categorias:
        resultado += f"<p>ID: {categoria['id']} - Descripción: {categoria['descripcion']}</p>"
    return resultado

if __name__ == "__main__":
    app.run(debug=True)
