# 🚀 Build. Automate. Hack. Repeat.
# 🧠 Author: Bruna Carmo
# ✨ Purpose: Fetch data from APIs, process, analyze, automate anything.

import requests
import time
from datetime import datetime

class APIClient:
    def __init__(self, url, headers=None, params=None, retries=3, delay=10):
        self.url = url
        self.headers = headers or {}
        self.params = params or {}
        self.retries = retries
        self.delay = delay

    def fetch_data(self):
        attempt = 0
        while attempt < self.retries:
            try:
                response = requests.get(self.url, headers=self.headers, params=self.params, timeout=30)
                response.raise_for_status()
                self._log("Data fetched successfully", success=True)
                return response.json()
            except requests.exceptions.RequestException as e:
                self._log(f"Error: {e}. Retrying in {self.delay} seconds...", success=False)
                attempt += 1
                time.sleep(self.delay)
        self._log("Failed after maximum retries.", success=False)
        return None

    def _log(self, message, success=True):
        status = "✔️" if success else "❌"
        print(f"[{datetime.now()}] {status} {message}")


class DataProcessor:
    def process(self, data):
        if not data:
            print("⚠️ No data to process.")
            return None

        print(f"[{datetime.now()}] 🔧 Processing data...")
        try:
            processed = [
                {
                    "id": item.get("id"),
                    "name": item.get("name"),
                    "created_at": item.get("created_at"),
                    "status": item.get("status"),
                }
                for item in data
            ]
            print(f"[{datetime.now()}] ✔️ Data processed successfully.")
            return processed
        except Exception as e:
            print(f"❌ Processing error: {e}")
            return None


class DataAnalyzer:
    def analyze(self, data):
        if not data:
            print("⚠️ No data to analyze.")
            return

        print(f"[{datetime.now()}] 📊 Analyzing {len(data)} records...")
        statuses = {}
        for item in data:
            status = item.get("status", "unknown")
            statuses[status] = statuses.get(status, 0) + 1

        print("🔍 Status distribution:")
        for status, count in statuses.items():
            print(f"   • {status}: {count} occurrences")


class AutomationPipeline:
    def __init__(self, api_url, headers=None):
        self.client = APIClient(api_url, headers=headers)
        self.processor = DataProcessor()
        self.analyzer = DataAnalyzer()

    def run(self):
        raw_data = self.client.fetch_data()
        processed_data = self.processor.process(raw_data)
        self.analyzer.analyze(processed_data)


def main():
    API_URL = "https://jsonplaceholder.typicode.com/users"  # Demo API
    HEADERS = {"Accept": "application/json"}

    pipeline = AutomationPipeline(api_url=API_URL, headers=HEADERS)
    pipeline.run()


if __name__ == "__main__":
    main()
