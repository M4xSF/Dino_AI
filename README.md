# T-Rex AI

T-Rex AI permite controlar el salto del juego del dinosaurio de Chrome usando una camara web y los movimientos de una mano. El programa detecta los dedos con MediaPipe y envia una pulsacion de `Espacio` cuando detecta que un dedo baja, haciendo que el dinosaurio salte.

## Requisitos

- Windows, macOS o Linux.
- Python 3.9 o superior.
- Una camara web funcional.
- Permiso del sistema para usar la camara.
- Google Chrome o un navegador compatible con el juego del dinosaurio.
- Permiso para que PyAutoGUI controle el teclado. En macOS tambien puede ser necesario habilitar **Accesibilidad** para la terminal o el editor.

Las dependencias de Python estan declaradas en [requirements.txt](requirements.txt):

- MediaPipe: deteccion de la mano.
- OpenCV: captura y visualizacion de la camara.
- PyAutoGUI: envio de la tecla `Espacio`.

## Instalacion

1. Instala Python desde [python.org](https://www.python.org/downloads/) y verifica que este disponible en la terminal:

   ```bash
   python --version
   ```

2. Clona este repositorio y entra en su carpeta:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd T-Rex-AI
   ```

   Reemplaza `<URL_DEL_REPOSITORIO>` por la URL que GitHub genere para este repositorio.

3. Crea un entorno virtual:

   ```bash
   python -m venv .venv
   ```

4. Activa el entorno virtual.

   En Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   En Windows CMD:

   ```bat
   .venv\Scripts\activate
   ```

   En macOS o Linux:

   ```bash
   source .venv/bin/activate
   ```

5. Instala las dependencias:

   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

## Manual de usuario

1. Abre Chrome y visita `chrome://dino/`. Tambien puedes abrir una pagina sin conexion y pulsar `Espacio` para iniciar el juego.
2. Coloca la camara de modo que una sola mano se vea completa y con buena iluminacion.
3. Enfoca la ventana del juego y ejecuta el programa desde la carpeta del proyecto:

   ```bash
   python game.py
   ```

4. Cuando el programa muestre la imagen de la camara, baja cualquier dedo para enviar una pulsacion de `Espacio` y hacer saltar al dinosaurio.
5. Mantente frente a la camara y deja el juego enfocado. PyAutoGUI envia la tecla a la ventana que este activa.
6. Para detener el programa, pulsa `Esc` mientras la ventana de la camara esta seleccionada.

## Solucion de problemas

**La camara no se abre:** cierra otras aplicaciones que la esten usando, revisa los permisos del sistema y prueba otra camara. El programa usa la camara predeterminada del equipo.

**El dinosaurio no salta:** asegurate de que la ventana del juego esta enfocada, de que la mano aparece completa en la ventana de video y de que `python game.py` se ejecuto con el entorno virtual activado.

**No se puede instalar MediaPipe:** confirma que usas una version compatible de Python y actualiza `pip` antes de ejecutar de nuevo la instalacion.

**PyAutoGUI no controla el teclado:** revisa los permisos de accesibilidad/automatizacion del sistema y evita ejecutar el programa con otra ventana que requiera privilegios especiales.

## Estructura del proyecto

```text
T-Rex-AI/
|-- game.py
|-- requirements.txt
|-- README.md
`-- .gitignore
```