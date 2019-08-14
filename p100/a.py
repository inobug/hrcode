#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading, queue, time

q = queue.Queue(maxsize=10)


def Producer(name):
        count = 0
        while True:
                q.put("产品1%s" % count)
                print("[%s]生产了产品" % name, count)
                count += 1
                time.sleep(0.5)


def Consumer(name):
        while True:
                print("[%s] 取到[%s]并且消费了它..." % (name, q.get()))
                time.sleep(1)


for i in range(2):
        p = threading.Thread(target=Producer, args=("生产者%s" % i,))
        p.start()

for i in range(3):
        c = threading.Thread(target=Consumer, args=("消费者%s" % i,))
        c.start()