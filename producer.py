#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 14:42:51 2023

@author: user
"""


import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='myhelloqueue')

for i in range(1000000):
    message = f"Message {i}"
    channel.basic_publish(exchange='', routing_key='myhelloqueue', body=message)

print(" [x] Sent 1000000 'Hello World!' Messsages")

connection.close()
