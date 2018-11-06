from src.app import create_app
from src.api import Api

if __name__ == '__main__':
    app = create_app()
    api = Api()


    @app.route('/')
    def index():
        return api.user.index()


    @app.route('/users/add', methods=['POST'])
    def add_users():
        return api.user.add_users()


    @app.route('/users', methods=['GET'])
    def list_users():
        return api.user.list_users()


    app.run()
