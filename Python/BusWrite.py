from azure.servicebus import ServiceBusService, Message, Queue

bus_service = ServiceBusService(
    service_namespace='appcandy-ns',
    shared_access_key_name='MachineSend',
    shared_access_key_value='Q4uctgrpqj+SZOejERPkkH0Mw0r4W4mOSb7yHSmLLI4=')
    
msg = Message(b'New Test Message')
bus_service.send_queue_message('appcandy', msg)
