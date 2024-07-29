# uHTTP Server  (upload HTTP Server)

uHTTP Server es un servidor web simple basado en Flask que permite subir archivos y servirlos.

## Instalación

Puedes instalar uHTTP Server directamente desde GitHub usando pip:

```bash
pip install git+https://github.com/CharlyPierce/uhttp.server.git
```
## Uso

Una vez instalado, puedes iniciar el servidor con el siguiente comando:
uhttp-server [puerto]

Por ejemplo:
```bash
uhttp-server 5033
```

Si no se especifica un puerto, se utilizará el puerto 5033 por defecto.

## Subir archivos

1. Abre tu navegador y ve a `http://localhost:[puerto]` (reemplaza [puerto] con el número de puerto que usaste).
2. Verás un formulario simple para subir archivos.
3. Selecciona uno o más archivos y haz clic en "Subir".
4. Los archivos se guardarán en la carpeta `uploads` del servidor.

Esta carpeta se crea donde se ejecuta uhttp-server 5033

## Acceder a los archivos subidos

Los archivos subidos estarán disponibles en `http://localhost:[puerto]/uploads/nombre_del_archivo`.

O en la carpeta **uploads** creada donde se ejecuto uhttp-server 5033

## uninstall
```bash
pip uninstall uhttp
```