# Interfaz Usuario para Sistema de Arduino

Este proyecto trata de crear una interfaz gráfica para poder controlar un sistema hecho en arduino el cual controla los componentes de este.

## Como usarlo

A continuación se explica lo necesario para poder ejecutar el código y los requisitos e instalación para este.

### Pre requisitos

Primero que nada se necesita Python version 3.5+ junto con las siguientes librerías:

    * serial
    * pygame

para instalar pygame y serial desde la terminal usando pip se hace de la siguiente manera:

```
pip install serial

```

```
pip install pygame

```

### Configuración

Dependiendo del sistema que tengas en tu computador (Windows/Linux/MacOSX), necesitamos saber el puerto en el que está conectado el arduino (se puede usar la IDE de arduino para identificar el puerto).
Luego nos vamos al archivo "ajustes.py" y buscamos la variable que dice "puerto" y la modificamos por el puerto que nos aparece en nuestro computador.

## Cómo ejecutarlo

Para ejecutar nuestro código, simplemente ejecutamos el archivo "tuberias.py"
