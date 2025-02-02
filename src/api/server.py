import logging
from flask import Flask, request, jsonify
from src.config import API_AUTH_TOKEN
from src.imei_checker.validator import ImeiValidator
from src.imei_checker.service import ImeiService

logger = logging.getLogger(__name__)


def create_app(imei_service: ImeiService) -> Flask:
    app = Flask(__name__)

    @app.route('/api/check-imei', methods=['POST'])
    def check_imei():
        data = request.get_json()
        if not data:
            return jsonify({"error": "Требуется JSON тело запроса"}), 400

        token = data.get("token")
        imei = data.get("imei")

        if token != API_AUTH_TOKEN:
            return jsonify({"error": "Неверный API токен"}), 401

        if not imei:
            return jsonify({"error": "Параметр imei обязателен"}), 400

        if not ImeiValidator.is_valid(imei):
            return jsonify({"error": "Неверный формат IMEI"}), 400

        info = imei_service.get_info(imei)
        return jsonify(info)

    return app
