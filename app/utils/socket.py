from app import socket


@socket.on('update')
def update_position(msg):
    print(msg)


@socket.on('update', namespace='/display')
def update_display(msg):
    print(msg)
