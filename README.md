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

Una vez instalado, es necesario poder levantar los servicios de `Zookeeper`, para ello, ejecutamos el archivo que tenemos en el repositorio de nombre `zookeeper_run.sh`

<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->

    $ zsh zookeeper_run.sh
<!--endsec-->

Luego iniciamos los servicios de kafka, para ello, ejecutamos el archivo `kafka_run.sh`
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $ zsh kafka_run.sh
<!--endsec-->

Una vez levantamos los servicios de kafka, iniciamos los topic "ORDERS" Y "DAILY SUMMARY" con el archivo `create_topics.sh`
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $ zsh create_topics.sh
<!--endsec-->
Para validar que tenemos el topic "test" ejecutamos el archivo `list_topic.sh`
<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $ zsh list_topic.sh
<!--endsec-->


## Instalación API -REST
Para la API, se utilizó la herramienta de framework `Flask`, para ello, teniendo python instalamos con el comando:

<!--sec data-title="Prompt: OS X and Linux" data-id="OSX_Linux_prompt" data-collapse=true ces-->
    $  pip install flask
    $  sudo pip3 install kafka-python
<!--endsec-->









