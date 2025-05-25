# TRABAJO PRÁCTICO N.º 5

### Nuestra primera aplicación en Flask

Para este trabajo vamos a poner en práctica lo aprendido en la clase.  
Deberán crear una aplicación con el framework de Python: **Flask**.  
Recuerden los pasos a seguir:

- Crear un entorno virtual para instalar y ejecutar Flask.
- Instalar Flask en el entorno con:

```bash
pip install flask
```

- Crear un archivo de entrada o principal con el nombre `app.py`, por ahora en la raíz de la carpeta.  
  Se podría llamar de cualquier otra manera, pero Flask por defecto siempre va a estar esperando que tengamos un archivo con ese nombre o `run.py`.

- Crear tres rutas:  
    - `/` con una función llamada `home` que retorne un saludo y una descripción de ustedes: nombre y apellido, y todo lo que quieran contarnos.
    - `/productos` con una función `listar_productos` que retorne una lista de productos. Por ahora algo sencillo que incluya: `id`, `descripcion`, `categoria_id`.
    - `/categorias` con una función `listar_categorias` que retorne una lista de categorías de productos con los atributos: `id`, `descripcion`.

Por ahora vamos a dejar de lado los *joins* entre productos y categorías.  
Este trabajo es meramente para ejemplificar cómo podemos mostrar rutas.

Para mostrar los datos en la página, vamos a tener que formatearlos como *string*.  
Luego veremos la manera correcta de hacerlo cuando trabajemos con nuestra **API**.  
En los diccionarios, al igual que en las listas, podemos acceder a su índice, solo que en este caso el índice es la clave asignada.  
Por ejemplo, podemos acceder a la descripción de un producto haciendo:

```python
producto["descripcion"]
```

Este ejemplo formatea lo que está entre llaves a *string*; estamos mostrando el valor de las claves de un diccionario:

```python
f"ID: {dict['key1']} - {dict['key2']}"
```

---

### Ignorar la carpeta `venv` al hacer *commit*

Por defecto Flask no trabaja con Git, por lo cual no crea el archivo `.gitignore`.  
Si queremos subir nuestro proyecto a un repositorio, también se va a subir la carpeta `venv`, y eso no estaría bien.  
Para que Git ignore dicha carpeta, vamos a crear el archivo `.gitignore` y dentro de él escribimos el nombre de la carpeta:

```
venv
```

Con esta simple acción le estamos diciendo a Git que no la suba.

---

### Datos de ejemplo

En la carpeta `data` tienen un archivo con las listas de los productos y categorías.  
Pueden importarlos con:

```python
from data.data_productos import productos, categorias
```

O directamente copiarlos en sus respectivas funciones.
