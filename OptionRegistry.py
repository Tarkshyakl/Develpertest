import os
import sys
import logging


class OptionRegistry:
    def __init__(self):

        hashMap = {}

        self.TXNFR_FREQ = "sensor.data.txns_freq"  # //in seconds: default is 30
        self.MODE = "mode"
        self.MQTT_SERVER = "mqtt.server.address"
        self.MQTT_SERVER_DATAFLOW_REQUEST_TOPIC = "mqtt.server.dtflow_rq.topic"
        self.MQTT_SERVER_DATAFLOW_RESPONSE_TOPIC = "mqtt.server.dtflow_rsp.topic"
        self.MQTT_SERVER_DATA_SUBMIT_TOPIC = "mqtt.server.data.submit.topic"
        self.MQTT_SERVER_COMMADN_RECEIPT_TOPIC = "mqtt.server.cmd.recpt.topic"

        self.DEVICE_ID = "sensor.id"
        self.TYPE = "sensor.type"
        self.SUPPLY_DEV_ID = "sensor.sdev"
        self.BS_DEV_ID = "sensor.bsdev"
        self.DIST_SUPPLY_DEV = "sensor.dsbs"
        self.ADDRESS = "sensor.add"
        self.GEO = "sensor.geo"

        self.RANGE_PRESSURE = "sensor.reading.range.prs"
        self.RANGE_TEMPERATURE = "sensor.reading.range.tmp"
        self.RANGE_FLOW_VELOCITY = "sensor.reading.range.flv"
        self.RANGE_VOLUME = "sensor.reading.range.vol"
        self.RANGE_EXTERNAL_BODY_FORCE = "sensor.reading.range.xbf"

        self.INIT_DATA = "init.data"
