#!/usr/bin/env python
import asyncio

from hbmqtt.client import MQTTClient
from hbmqtt.mqtt.constants import QOS_0, QOS_1, QOS_2

# Placeholder for missing exception


class ConnectException(Exception):
    pass


async def publish_test():
    try:
        C = MQTTClient()
        # TODO: Unused variable, remove or use. # ret = await C.connect('mqtt://192.168.0.4:1883/')
        await C.connect('mqtt://192.168.0.4:1883/')  # Assuming connect must be called
        # TODO: Unused variable, remove or use. # message = await C.publish('server', 'MESSAGE-QOS_0'.encode(), qos=QOS_0)
        await C.publish('server', 'MESSAGE-QOS_0'.encode(), qos=QOS_0)  # Assuming publish must be called
        # TODO: Unused variable, remove or use. # message = await C.publish('server', 'MESSAGE-QOS_1'.encode(), qos=QOS_1)
        await C.publish('server', 'MESSAGE-QOS_1'.encode(), qos=QOS_1)  # Assuming publish must be called
        # TODO: Unused variable, remove or use. # message = await C.publish('gateway', 'MESSAGE-QOS_2'.encode(), qos=QOS_2)
        await C.publish('gateway', 'MESSAGE-QOS_2'.encode(), qos=QOS_2)  # Assuming publish must be called
        print("messages published")  # noqa: T201
        await C.disconnect()
    except ConnectException as ce:
        print("Connection failed: %s" % ce)
        asyncio.get_event_loop().stop()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(publish_test())
