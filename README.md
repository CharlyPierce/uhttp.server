# uHTTP Server  (upload HTTP Server)

uHTTP Server es un servidor web simple basado en Flask que permite subir archivos.

## Instalación

## Crea un entorno virutal
1. python3 -m venv myenv
2. source myenv/bin/activate

Una vez con el entorno virtual proceder con:


Puedes instalar uHTTP Server directamente desde GitHub usando pip:

```bash
pip install git+https://github.com/CharlyPierce/uhttp.server.git
```

Forzar sin entorno virtual
```bash
pip install --break-system-packages git+https://github.com/CharlyPierce/uhttp.server.git
```

Agregando al path:
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
```

Recargando bash
```bash
source ~/.bashrc
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

Los archivos subidos estarán disponibles en la carpeta **uploads** 

Creada donde se ejecuto uhttp-server 5033

## uninstall
```bash
pip uninstall uhttp
```

Forzado
```bash
pip uninstall --break-system-packages uhttp
```