from app import app, create_app
from app.utils.logs import Logger

if __name__ == '__main__':
    Logger.info('Server starting at 5000 port')
    create_app()
    app.run()
