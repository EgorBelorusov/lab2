# Подключение библиотек для работы с Flask и Blueprint
from flask import Flask, jsonify, Blueprint

# Подключение библиотеки для создания автоматической документации API
from flasgger import Swagger, swag_from

# Подключение части нашего веб-сервиса с использованием Blueprint
from sitepart.sitepart import sitepart

# Словарь с информацией для API (из методички)
all_info = {
    'version': '1.0',
    'author': 'Student',
    'year': '2026',
    'all': 'Example endpoint returning about info'
}

# Инициализация приложения Flask
app = Flask(__name__)


# Инициализация Swagger для документации API
swagger = Swagger(app)

# Создание основного Blueprint сайта
main = Blueprint("main", __name__,
                 template_folder="templates",
                 static_folder="static")



# Маршрут /info/<about> с документацией Swagger
@main.route('/info/<about>')
def info(about):
    """
    Example endpoint returning about info
    This is using docstrings for specifications.
    ---
    parameters:
      - name: about
        in: path
        type: string
        enum: ['all', 'version', 'author', 'year']
        required: true
        default: all
    definitions:
      About:
        type: string
    responses:
      200:
        description: A string
        schema:
          $ref: '#/definitions/About'
        examples:
          version: '1.0'
    """
    # Формируем результат в зависимости от параметра about
    result = {about: all_info.get(about, "Unknown")}
    return jsonify(result)



# Регистрация Blueprint'ов
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(sitepart, url_prefix='/sitepart')



# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)