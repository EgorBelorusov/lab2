from flask import Blueprint, jsonify
from flasgger import swag_from

# Создаем Blueprint для отдельной части веб API
sitepart = Blueprint("sitepart", __name__,
                     template_folder="templates",
                     static_folder="static")

# Словарь с цветовыми палитрами
all_colors = {
    'cmyk': ['cian', 'magenta', 'yellow', 'black'],
    'rgb': ['red', 'green', 'blue']
}


# Маршрут /colors/<palette> с документацией Swagger
@sitepart.route('/colors/<palette>')
def colors(palette):
    """
    Example endpoint returning a list of colors by palette
    This is using docstrings for specifications.
    ---
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['all', 'rgb', 'cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    # Формируем результат в зависимости от параметра palette
    if palette == 'all':
        result = all_colors
    else:
        # Возвращаем результат в зависимости от имени палитры
        result = {palette: all_colors.get(palette)}

    # Преобразуем словарь в JSON строку и возвращаем ее
    return jsonify(result)