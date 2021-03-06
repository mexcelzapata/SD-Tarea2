# 馃浉SD-Tarea2-KAFKA馃槑 - Nicolas Correa - Mexcel Zapata

`Apache Kafka` es una plataforma distribuida de transmisi贸n de datos que permite publicar, almacenar y procesar flujos de registros, as铆 como suscribirse a ellos, de forma inmediata. Est谩 dise帽ada para administrar los flujos de datos de varias fuentes y distribuirlos a diversos usuarios. En pocas palabras, transfiere cantidades enormes de datos, no solo desde el punto A hasta el B, sino tambi茅n del punto A al Z y a cualquier otro lugar que necesite, y todo al mismo tiempo.

Apache Kafka es la alternativa a un sistema de mensajer铆a tradicional para empresas. Comenz贸 como un sistema interno que LinkedIn desarroll贸 para gestionar 1,4 billones de mensajes por d铆a. Ahora, es una soluci贸n open source de transmisi贸n de datos que permite satisfacer diversas necesidades empresariales.


## Instalaci贸n de Kafka 馃洬
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

Una vez levantamos los servicios de kafka, iniciamos los topic "ORDENES" Y "RESUMEN DIARIO" con el archivo `create_topics.sh` donde cada uno de ellos est谩 configurado por 1 partici贸n y un factor de replicaci贸n de 1.
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $ zsh create_topics.sh
<!--endsec-->
Para validar que tenemos el topics, ejecutamos el archivo `list_topic.sh`
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $ zsh list_topic.sh
<!--endsec-->

### Python 3.8.10 馃悕
Instalamos `python` para utilizar la API.
```
sudo apt update
sudo apt install software-properties-common
sudo apt install python3.8.10
sudo apt-get -y install python3-pip
sudo pip3 install kafka-python
```

## Instalaci贸n API -REST 馃拝
Para la API, se utiliz贸 la herramienta framework `Flask`, para ello, instalamos `flask` comando (teniendo python instalado):

<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $  pip3 install flask
<!--endsec-->

## Ejecutar programa 馃サ馃サ锟?
Para ejecutar el programa, simplemente corremos el archivo `app.py`, es importante mensionar que se asume que los vendedores con los cocineros durante el dia trabajan en conjunto y no se separan (o sea siempre estan juntos en las ordenes).
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $  python3 app.py
<!--endsec-->

Utilizando un software para realizar pruebas a API como lo es ``INSOMNIA'' que es una aplicaci贸n que nos permite realizar pruebas API. Donde es un cliente HTTP que nos da la posibilidad de testear 'HTTP requests' a trav茅s de una interfaz gr谩fica de usuario. vamos a realizar las pruebas correspondientes
### 馃搩 Generar Orden 馃搩
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


### 馃枿 Generar Resumen Diario 馃摀
Ingresamos la url con metodo `GET`:
```
http://localhost:3000/resumenDiario
```
`output: "resumen diario realizado con exito" `


### 馃捀 Env铆ar Mails馃摡
Ingresamos la url con metodo `GET`:
```
http://localhost:3000/enviarEmails
```
`output: "emails enviados" `


