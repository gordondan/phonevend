from azure.servicebus import ServiceBusService, Message, Queue

bus_service = ServiceBusService(
    service_namespace='appcandy-ns',
    shared_access_key_name='MachineListen',
    shared_access_key_value='OLYoVII6DU85jRQ70F06aHhX3wJwoTq+LC7WiW0zO6Q=')
    
msg = bus_service.receive_queue_message('appcandy', peek_lock=False)
print(msg.body)
