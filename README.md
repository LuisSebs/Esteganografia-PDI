# Tarea08 - Esteganografia

## Autor: Arrieta Mancera Luis Sebastian

<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3phb2lpNHIxcGFzanFpaTUxc3NmYWNhYW1obDlveG9vN3k5aGJiaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wbD3QXowS1ujm/giphy.gif"/>

La esteganografia es el arte de esconder información a plena vista.

**Argumentos**

+ `-i` ruta de la imagen
+ `-hi` Ocultar imagen:
  + Mensaje a ocultar
  + Ruta de salida de la imagen
+ `-r` Revelar mensaje

# Ejecución:

Instala las librerias **colorarma** y **pillow**

**Colorama**

```bash
pip install colorama
```

**Pillow**

```bash
pip install pillow
```

Para probar el programa ejecuta los siguientes comandos con python o python3. Los comandos tienen la siguiente estructura:

Para ocultar un mensaje en una imagen:

```bash
python3 esteganografia.py -i <Ruta de la imagen> -hi "<Mensaje a ocultar>" <Ruta de salida de la imagen>.png
```

Para revelar el mensaje de una imagen:

```bash
python3 esteganografia.py -i <Ruta de la imagen> -r
```

## Ejemplo:

Insetar un mensaje en una imagen de perrito:

```bash
python3 esteganografia.py -i ./imagenes/perrito.jpg -hi "proceso digital de imagenes es la mejor optativa" ./imagenes/perrito_con_mensaje.png
```

Para revelar el mensaje de perrito:

```bash
python3 esteganografia.py -i ./imagenes/perrito_con_mensaje.png -r
```

# Chessboard

Ejecuta el siguiente comando para mostrar el mensaje oculto de la imagen `Chessboard.png`

```bash
python3 esteganografia.py -i ./imagenes/chessboard.png -r
```