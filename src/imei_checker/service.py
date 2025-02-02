import requests
import logging
from src.config import IMEI_API_URL, IMEI_API_TOKEN

logger = logging.getLogger(__name__)


class ImeiService:

    def __init__(self, api_url: str = IMEI_API_URL, api_token: str = IMEI_API_TOKEN):
        self.api_url = api_url
        self.api_token = api_token

    def get_info(self, imei: str) -> dict:
        url = f"{self.api_url}/v1/checks"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        payload = {"imei": imei}
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"Ошибка от IMEIcheck API: {response.status_code} - {response.text}")
                return {"error": f"Ошибка от IMEIcheck API: {response.status_code}", "details": response.text}
        except Exception as e:
            logger.exception("Ошибка при обращении к IMEIcheck API")
            return {"error": str(e)}
