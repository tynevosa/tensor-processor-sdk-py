
# coding: utf-8

"""
    tpu-api

    The API for the TPU project  # noqa: E501
"""

from __future__ import absolute_import

import requests
import time

class Tpu(object):
    def __init__(self, apiKey=None):
        self.default_headers = {
            'Content-Type': 'application/json',
            'tpu-api-key': apiKey
        }
        self.base_url = 'http://95.217.158.17:5000/api'
        self.timeout = 600

    def __del__(self):
        pass

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    # Mothod to get model list
    def getModels(self, page=1, count=25, category=None):
        json = {
            "page": page,
            "count": count
        }
        if category is not None:
            json["collection"] = category
        return requests.post(f"{self.base_url}/model/list",
            headers=self.default_headers,
            json=json).json()

    # Mothod to get specific model
    def getModel(self, model_name=None):
        return requests.get(f"{self.base_url}/model/get/{model_name}",
            headers=self.default_headers).json()

    # Method to get categories
    def getCategories(self):
        return requests.get(f"{self.base_url}/collection/list",
            headers=self.default_headers).json()

    # Method to get prediction history
    def predictionHistory(self):
        return requests.get(f"{self.base_url}/prediction/history",
            headers=self.default_headers).json()

    # Method to create a prediction
    def prediction(self, model=None, input=None):
        if model is None or input is None:
            return None
        json = {
            "model": model,
            "input": input
        }
        try:
            resp = requests.post(f"{self.base_url}/prediction",
                headers=self.default_headers,
                json=json).json()
            start_time = time.time()
            while True:
                time.sleep(1)
                status = requests.get(f"{self.base_url}/prediction/status/{resp['id']}",
                            headers=self.default_headers).json()
                if status['status'] == "pending":
                    if (time.time() - start_time) > self.timeout:
                        return "Execution Timeout!"
                else:
                    if status['status'] == "success":
                        result = requests.get(f"{self.base_url}/prediction/result/{status['prediction_id']}",
                                    headers=self.default_headers).json()
                        return result["output"]
                    else:
                        return None
        except Exception as e:
            print(e)
            return None
