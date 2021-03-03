from app import socket, create_app, app
from app.utils.logs import Logger

if __name__ == '__main__':
    Logger.info('Server starting at 5000 port')
    create_app()
    socket.run(app, host='0.0.0.0')
