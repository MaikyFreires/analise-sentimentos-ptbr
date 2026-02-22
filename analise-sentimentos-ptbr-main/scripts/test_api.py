import json
import time

import requests


BASE_URL = "http://127.0.0.1:8000"


def main() -> None:
    print("Before running this script, start the API with:")
    print("uvicorn app.main:app --reload")
    print("-" * 60)

    samples = [
        "Esse filme foi incrivel, gostei muito!",
        "Que atendimento pessimo, fiquei decepcionado.",
        "A entrega foi rapida e o produto e excelente.",
    ]

    for idx, text in enumerate(samples, start=1):
        payload = {"text": text}
        try:
            response = requests.post(f"{BASE_URL}/predict", json=payload, timeout=10)
            print(f"[{idx}] status={response.status_code}")
            try:
                print(json.dumps(response.json(), ensure_ascii=False, indent=2))
            except ValueError:
                print(response.text)
        except requests.RequestException as exc:
            print(f"[{idx}] request failed: {exc}")

        print("-" * 60)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
