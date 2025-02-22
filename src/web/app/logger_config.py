from loguru import logger
import sys

# Configurar el logger
logger.remove()

# Agregar salida al archivo logs.log con formato JSON a partir del nivel DEBUG
logger.add(
    "logs_web.log",
    level="DEBUG",
    serialize=True
)

# Agregar salida por pantalla con formato personalizado a partir del nivel INFO
logger.add(
    sys.stderr,
    format="{time:MMMM D, YYYY > HH:mm:ss!UTC} | {level} | {message} | {module} | {line} | {extra}",
    level="DEBUG",
    serialize=False,
)

# Añadir como parametro extra la version de la app web
logger = logger.bind(web_version="1.0.0")
