# 🛸SD-Tarea2-KAFKA😎 - Nicolas Correa - Mexcel Zapata

`Apache Kafka` es una plataforma distribuida de transmisión de datos que permite publicar, almacenar y procesar flujos de registros, así como suscribirse a ellos, de forma inmediata. Está diseñada para administrar los flujos de datos de varias fuentes y distribuirlos a diversos usuarios. En pocas palabras, transfiere cantidades enormes de datos, no solo desde el punto A hasta el B, sino también del punto A al Z y a cualquier otro lugar que necesite, y todo al mismo tiempo.

Apache Kafka es la alternativa a un sistema de mensajería tradicional para empresas. Comenzó como un sistema interno que LinkedIn desarrolló para gestionar 1,4 billones de mensajes por día. Ahora, es una solución open source de transmisión de datos que permite satisfacer diversas necesidades empresariales.


## Instalación de Kafka 🛫
Inicialmente descargamos kafka 2.8.0

<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->

    $ mkdir kafka
    $ cd kafka
    $ wget https://downloads.apache.org/kafka/2.8.0/kafka_2.13-2.8.0.tgz
    $ tar -xzf kafka_2.13-2.8.0.tgz
    
<!--endsec-->
`Importante: ingresar en archivo kafka_home.sh el PATH correspondiente al archivo kafka_2.13-2.8.0`
Una vez instalado, es necesario poder levantar los servicios de `Zookeeper`, para ello, ejecutamos el archivo que tenemos en el repositorio de nombre `zookeeper_run.sh` y dejamos que corra.

<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->

    $ zsh zookeeper_run.sh
<!--endsec-->

Luego, en otra ventana de la terminal, iniciamos los servicios de kafka, para ello, ejecutamos el archivo `kafka_run.sh` y lo dejamos corriendo.
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $ zsh kafka_run.sh
<!--endsec-->

Una vez levantamos los servicios de kafka, iniciamos los topic "ORDENES" Y "RESUMEN DIARIO" con el archivo `create_topics.sh`
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $ zsh create_topics.sh
<!--endsec-->
Para validar que tenemos el topics, ejecutamos el archivo `list_topic.sh`
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $ zsh list_topic.sh
<!--endsec-->

### Python 3.8.10 🐍
Instalamos `python` para utilizar la API.
```
sudo apt update
sudo apt install software-properties-common
sudo apt install python3.8.10
sudo apt-get -y install python3-pip
sudo pip3 install kafka-python
```

## Instalación API -REST 💅
Para la API, se utilizó la herramienta framework `Flask`, para ello, instalamos `flask` comando (teniendo python instalado):

<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $  pip3 install flask
<!--endsec-->

## Ejecutar programa 🥵🥵�
Para ejecutar el programa, simplemente corremos el archivo `app.py`, es importante mensionar que se asume que los vendedores con los cocineros durante el dia trabajan en conjunto y no se separan (o sea siempre estan juntos en las ordenes).
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $  python3 app.py
<!--endsec-->

Utilizando un software para realizar pruebas a API como lo es ``INSOMNIA'' que es una aplicación que nos permite realizar pruebas API. Donde es un cliente HTTP que nos da la posibilidad de testear 'HTTP requests' a través de una interfaz gráfica de usuario. vamos a realizar las pruebas correspondientes
### 📃 Generar Orden 📃
Ingresamos a la url:
```
http://localhost:3000/nuevaOrden
```
y ingresamos un JSON con la siguinte estructura con metodo `POST`:
```
{
  "correoVendedor": "pruebasboltonudp@gmail.com",
  "correoCocinero": "pruebasboltonudp@gmail.com",
  "cantidad": 1,
  "total": 5
}
```
`output: "Orden realizada con Exito" `


### 🖨 Generar Resumen Diario 📓
Ingresamos la url con metodo `GET`:
```
http://localhost:3000/resumenDiario
```
`output: "resumen diario realizado con exito" `


### 💸 Envíar Mails📩
Ingresamos la url con metodo `GET`:
```
http://localhost:3000/enviarEmails
```
`output: "emails enviados" `


