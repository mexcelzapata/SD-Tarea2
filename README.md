# SD-Tarea2
KAFKA


## Instalación de Kafka 
Inicialmente descargamos kafka 2.8.1

<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->

    $ mkdir kafka
    $ cd kafka
    $ wget https://downloads.apache.org/kafka/2.8.0/kafka_2.13-2.8.0.tgz
    $ tar -xzf kafka_2.13-2.8.0.tgz
    
<!--endsec-->

Una vez instalado, es necesario poder levantar los servicios de `Zookeeper`, para ello, ejecutamos el archivo que tenemos en el repositorio de nombre `zookeeper_run.sh` y dejamos que corra.

<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->

    $ zsh zookeeper_run.sh
<!--endsec-->

Luego, en otra ventana de la terminal, iniciamos los servicios de kafka, para ello, ejecutamos el archivo `kafka_run.sh` y lo dejamos corriendo.
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $ zsh kafka_run.sh
<!--endsec-->

Una vez levantamos los servicios de kafka, iniciamos los topic "ORDERES" Y "RESUMEN DIARIO" con el archivo `create_topics.sh`
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $ zsh create_topics.sh
<!--endsec-->
Para validar que tenemos el topics, ejecutamos el archivo `list_topic.sh`
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $ zsh list_topic.sh
<!--endsec-->

### Python 3.8.10
Instalamos python para utilizar la API.
```
sudo apt update
sudo apt install software-properties-common
sudo apt install python3.8.10
sudo pip3 install kafka-python
```

## Instalación API -REST
Para la API, se utilizó la herramienta framework `Flask`, para ello, instalamos `flask` comando (teniendo python instalado):

<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $  pip install flask
<!--endsec-->









