import nsq
import logging
import json
import time
import datetime
import tornado.ioloop
#NSQ消息者
class NsqConsumer(object):
    global nsqConsumerList
    global reader1
    global buf
    def __init__(self):
        self.buf=[]
        self.nsqConsumerList=[]
    #消息处理hardler--一直监听处理
    def process_message(self,message):
        logging.debug("调用process_message方法")
        logging.debug('时间===' + str(datetime.datetime.now()))
        message.enable_async()
        # cache the message for later processing
        self.buf = []
        self.buf.append(message)
        try:
            if len(self.buf) >= 1:
                messageTopic = self.reader1.topic
                logging.info("handler_get_message消息topcic：" + self.reader1.topic)
                messageChannel = self.reader1.channel
                logging.info("handler_get_message消息channel：" + self.reader1.channel)
                for msg in self.buf:
                    # logging.debug(msg)
                    logging.info("消息体body：" + str(msg.body))
                    jsonBody = json.loads(msg.body)
                    msgValue = jsonBody['Msg']
                    # try:
                    if msgValue:
                        if 1 == 1:
                            msg.finish()
                            logging.debug('handler_get_message .. nsq finish')
                        # if 2==2:
                        #     msg.requeue()
                        #     logging.debug('nsq requeue')
            else:
                logging.debug('deferring processing')

        finally:
            logging.debug('handler_get_message ...nsq stop .........')
    #消息处理--完成1次消费处理后退出
    def handler_get_message(self,message):
        logging.debug("调用handler_get_message方法")
        logging.debug('时间==='+str(datetime.datetime.now()))
        message.enable_async()
        # cache the message for later processing
        self.buf = []
        self.buf.append(message)
        try:
            if len(self.buf) >=1:
                messageTopic = self.reader1.topic
                logging.debug("handler_get_message消息topcic：" + self.reader1.topic)
                messageChannel = self.reader1.channel
                logging.debug("handler_get_message消息channel：" + self.reader1.channel)
                for msg in self.buf:
                    # logging.debug(msg)
                    logging.info("消息体body：" + str(msg.body))
                    jsonBody = json.loads(msg.body)
                    msgValue = jsonBody['Msg']
                    # try:
                    if msgValue:
                        if 1==1:
                            msg.finish()

                            logging.debug('handler_get_message .. nsq finish')
                        # if 2==2:
                        #     msg.requeue()
                        #     logging.debug('nsq requeue')
            else:
                logging.debug('deferring processing')

        finally:
            # NsqConsumer.stopLoop()
            logging.debug('handler_get_message ...nsq stop .........')
    #创建消费者Reader对象
    def createOneNsqConsumer(self,host,port, nsqTopic, nsqChannel):
        """
        Adds a Reader to nsq at the specified address.
        :param host: the address to connect to
        :param port: the port to connect to
        :param nsqTopic: the topic to connnet to
        :param nsqChannel: the channel to connet to
        """
        self.reader1  =nsq.Reader(message_handler=self.handler_get_message,
                                  nsqd_tcp_addresses=[host + ':' + port],  # 监听端口默认是4150
                                  # lookupd_http_addresses=['http://' + host + ':' + port], #监听端口默认是4161
                                  topic=nsqTopic,
                                  channel=nsqChannel,
                                  lookupd_poll_interval=15, max_backoff_duration=2, low_rdy_idle_timeout=2, max_tries=65535)

    # 创建多个消费者Reader对象，
    #入参topicAndChannleList 实例： [{'inbound':['inbound_megvi','inbound_g']},{'outbound':['outbound_megvi','outbound_g']}]
    def createMultiNsqConsumer(host,port, topicAndChannleList):
        nsqConsumerList=[]
        for topicAndChannle in topicAndChannleList:
            # logging.debug('nsqTOPTIC======'+str(nsqTopic))
            for key, value in topicAndChannle.items():
                # logging.debug("nsqTopic vlaue"+dict(nsqTopic)[key])
                nsqTopic = key
                nsqChannelList = value
                for nsqChannel in nsqChannelList:
                    nsqConsumer = NsqConsumer()
                    r1 = nsqConsumer.createReader(host, port,nsqTopic, nsqChannel)
                    nsqConsumer.reader1 = r1
                    nsqConsumerList.append(nsqConsumer)
                return nsqConsumerList
    #创建Reader对象
    def createReader(self,host,port,nsqTopic, nsqChannel):
        r=nsq.Reader(message_handler=self.process_message,
                     nsqd_tcp_addresses=[host + ':' + port],  # 监听端口默认是4150
                     # lookupd_http_addresses=['http://' + host + ':' + port], #监听端口默认是4161
                     topic=nsqTopic,
                     channel=nsqChannel,
                     lookupd_poll_interval=2, max_backoff_duration=2, low_rdy_idle_timeout=2, max_tries=65535)
        return r
    #停止消费者进程
    @staticmethod
    def stopLoop():
        tornado.ioloop.IOLoop.instance().stop()

    # 启动消费者进程
    #Duration 监听单位秒 = 不设置超时时间，一直监听处理
    # Duration>0 指定持续监听时间，到达指定时间主动退出
    @staticmethod
    def runLoop(Duration=0):
        if Duration>0:
            tornado.ioloop.IOLoop.instance().add_timeout(time.time() + Duration, callback=NsqConsumer.stopLoop)
        nsq.run()



if __name__ == '__main__':

    host='10.170.124.16'
    # host='127.0.0.1'
    port='4150'
    logging.debug('host=='+host+'; port=='+port)

    #方式一：
    topicAndChannleList=[{'chatRoomOutBound':['outbound_megvi','outbound_gk']},{'outbound':['outbound_megvi','outbound_g']},{'eee':['outbound_megvi']}]
    NsqConsumer.createMultiNsqConsumer(host,port,topicAndChannleList)
    NsqConsumer.runLoop()

   # #方式二
    nsqTopic='chatRoomOutBound'
    channel='outbound_megvi'
    nsqclient = NsqConsumer()
    nsqclient.createOneNsqConsumer(host,port,nsqTopic, channel)
    NsqConsumer.runLoop()
    # 验证有消息生成
    assert len(nsqclient.buf) == 1
    bb=nsqclient.buf
    message = bb[0]
    logging.debug("消息体body：" + str(message.body))
    jsonBody = json.loads(message.body)
    msgValue = jsonBody['Msg']
    logging.debug("消息内容Msg==：" + str(msgValue))

   






