import argparse
from colorama import Fore, Back, Style
from PIL import Image

# Colores
rojo = Fore.RED
verde = Fore.GREEN
azul = Fore.BLUE
cian = Fore.CYAN
amarillo = Fore.YELLOW
magenta = Fore.MAGENTA
blanco = Fore.WHITE
reset = Fore.RESET

def cifrar(imagen: Image, bits):
    # Convertimos la secuencia de bits a una lista
    bits = list(bits)
    # Insertamos la secuencia de bits en la imagen
    for x in range(imagen.width):
        for y in range(imagen.height):
            pixel = imagen.getpixel((x,y))
            nuevo_pixel = []
            for valor in pixel:
                if bits:
                    nuevo_valor = int(format(valor,'08b')[:-1] + bits.pop(0),2)
                    nuevo_pixel.append(nuevo_valor)
                else:
                    nuevo_pixel.append(valor)
            imagen.putpixel((x,y), tuple(nuevo_pixel))
            if not bits:
                return

def longitud_mensaje_en_bits(mensaje):
    return format(len(mensaje),'016b')

def mensaje_en_bits(mensaje):
    bits = ''
    for letra in mensaje:
        bits += format(ord(letra),'08b')
    return bits

# Inserta un mensaje en una imagen
def esteganografia_cifrado(imagen: Image, mensaje):
    # Imagen a regresar
    nueva_imagen = imagen.copy()
    # Secuencia de bits que tenemos que agregar
    bits = longitud_mensaje_en_bits(mensaje)+mensaje_en_bits(mensaje)+'00000000'
    # Insertamos la secuencia de bits
    cifrar(nueva_imagen, bits)
    return nueva_imagen

def longitud(imagen: Image):
    # Leemos los primeros 2 bytes
    stop = 16
    count = 0
    longitud_mensaje = ''
    for x in range(imagen.width):
        for y in range(imagen.height):
            pixel = imagen.getpixel((x,y))
            for valor in pixel:
                if count < stop:
                    longitud_mensaje += format(valor,'08b')[-1]
                    count += 1
                else:
                    return int(longitud_mensaje,2)
                
def descifrar_mensaje(bits):
    mensaje = ''
    for i in range(0, len(bits), 8):
        # Obtenemos un bloque de 8 bits
        bloque_8bits = bits[i:i+8]
        caracter = chr(int(bloque_8bits,2))
        mensaje += caracter
    return mensaje

def descifrar(imagen: Image, longitud):
    stop = 16 + longitud*8 + 8
    count = 0
    bits = ''
    for x in range(imagen.width):
        for y in range(imagen.height):
            pixel = imagen.getpixel((x,y))
            for valor in pixel:
                if count < stop:
                    bits += format(valor, '08b')[-1]
                    count += 1
                else:
                    # Verificamos que termine con 00000000
                    if not (bits[-8:] == '00000000'):
                        return ValueError("El mensaje no termina con el byte 00000000")
                    # Le pasamos los bits y eliminamos los primeros 16 bits y los ultimos 8bits
                    return descifrar_mensaje(bits[16:][:-8])

# Obtiene el mensaje de una imagen
def esteganografia_descifrado(imagen: Image):    
    longitud_mensaje = longitud(imagen)
    return descifrar(imagen, longitud_mensaje)

if __name__ == '__main__':
    descripcion = "Practica08-Criptografia y Seguridad. Programa para realizar esteganografia. Ocultar y leer mensajes en imagenes"
    parser = argparse.ArgumentParser(
        description=descripcion
    )

    # Bandera -i
    parser.add_argument("-i", "--input_image", required=True, help="Ruta de la imagen")

    # Banderas -h (ocultar) y -r (revelar)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-hi', '--hide', nargs=2, metavar=('mensaje', 'ruta_salida'), help="Ocultar mensaje. Bandera -h seguido del mensaje a ocultar entre comillas y la ruta de salida")
    group.add_argument('-r', '--reveal', action='store_true', help="Revelar mensaje")

    # Parseamos los argumentos
    args = parser.parse_args()

    ruta_imagen = args.input_image    
    if args.hide:        
        mensaje, ruta_salida = args.hide
        print(azul+"Imagen: "+reset+f"{ruta_imagen}")
        print(azul+"Mensaje a ocultar: "+reset+f"{mensaje}")
        print(azul+"Ruta de salida: "+reset+f"{ruta_salida}")        
        imagen = Image.open(ruta_imagen)
        imagen_mensaje = esteganografia_cifrado(imagen, mensaje)
        imagen_mensaje.save(ruta_salida)
        print(verde+f"Imagen con el mensaje oculto guardada ʕ•ᴥ•ʔ"+reset)
        
    if args.reveal:        
        print(azul+"Imagen: "+reset+f"{ruta_imagen}")
        imagen = Image.open(ruta_imagen)
        mensaje = esteganografia_descifrado(imagen)
        print(verde+"Mensaje: "+reset+f"{mensaje}")
