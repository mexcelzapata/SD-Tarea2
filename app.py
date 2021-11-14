from flask import Flask, request
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from flask import jsonify
import json
import smtplib
import asyncio

#el siguiente codigo esta hecho solo para kafka en el puerto 9092

app = Flask(__name__)

def producer(value, topic):
    producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'),bootstrap_servers='localhost:9092')
    producer.send(topic, value)
    print("se produjo " , value)
    producer.flush()

def consumer_from_beginning(topic):
    arr_json = [] 
    consumer = KafkaConsumer(
        topic,
        value_deserializer = lambda m: json.loads(m.decode('ascii')),
        bootstrap_servers = 'localhost:9092',
        auto_offset_reset = 'earliest',
        enable_auto_commit=False
    )
    partitions = [TopicPartition(topic,p) for p in consumer.partitions_for_topic(topic)]
    lenght_consumer = consumer.end_offsets(partitions)
    val_ultimo = list(lenght_consumer.values())[0]
    con = 0
    for msg in consumer:
        arr_json.append(msg.value)
        con += 1 
        if(con == val_ultimo):
            break
    return arr_json

def suma_ordenes(arr_ordenes_json):
    suma = 0
    cantidad = 0
    con = 0
    arr = []
    data = {}
    data["dailySumary"] = []
    boolean = False
    for i in arr_ordenes_json:
        for j in arr:
            if i['correoCocinero'] == j:
                boolean = True
        if(boolean == False):
            for val in arr_ordenes_json:
                if val['correoVendedor'] == i['correoVendedor'] and val['correoCocinero'] == i['correoCocinero']:
                    suma += val['total']
                    cantidad += val['cantidad']
                    arr.append(val['correoCocinero'])
                    con += 1
            data["dailySumary"].append({
                'correoVendedor': i['correoVendedor'],
                'correoCocinero': i['correoCocinero'],
                'cantidad': cantidad,
                'total': suma
            })
        boolean = False
        suma = 0
        cantidad = 0

    if con == 0:
        return -1
    else:
        return data

@app.route('/nuevaOrden', methods = ['POST'])
def nuevaOrden():
    producer(request.json, "ordenes")
    return "Orden realizada con exito"

@app.route('/resumenDiario')  
def resumenDiario():
    arr_ordenes_json = consumer_from_beginning("ordenes")
    arr_suma = suma_ordenes(arr_ordenes_json)
    for a in arr_suma['dailySumary']:
        producer(a, "resumenDiario")
    return "resumen diario realizado con exito"

@app.route('/enviarEmails')    
def enviarEmails():
    print("---------------------------")
    arr_resumenDiario_json = consumer_from_beginning("resumenDiario")
    print(arr_resumenDiario_json)
    #SMTP es un protocolo de transferencia de mail simple mail transfer protocole
    server = smtplib.SMTP('smtp.gmail.com',587) #(servidor del correo, puerto a utilizar)
    server.starttls()
    server.login('pruebasboltonudp@gmail.com',"aAbB12345678")
    msg = ""
    for val in arr_resumenDiario_json:
        msg = "\nBuenas tardes, la cantidad de sopaipillas vendidas el dia de hoy son:" + str(val['cantidad']) + " lo cual corresponde a un total de $" + str(val['total'])
        print(msg)
        #msg = str(val['cantidad']) + str(val['total'])
        server.sendmail("pruebasboltonudp@gmail.com",val['correoVendedor'],msg)
        server.sendmail("pruebasboltonudp@gmail.com",val['correoCocinero'],msg)
    server.quit()
    return "emails enviados"

app.run(host='0.0.0.0', port=3000)
