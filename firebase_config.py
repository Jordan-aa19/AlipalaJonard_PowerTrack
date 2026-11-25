import os
import json
from pathlib import Path
from functools import lru_cache
from threading import RLock

from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore


# ==========================================
# ENVIRONMENT CONFIGURATION
# ==========================================

BASE = Path(__file__).resolve().parent

load_dotenv(BASE / ".env")

_lock = RLock()


# ==========================================
# FIREBASE FIRESTORE CONNECTION
# ==========================================

@lru_cache(maxsize=1)
def get_db():

    with _lock:

        try:
            firebase_app = firebase_admin.get_app()

        except ValueError:

            # VERCEL CONNECTION
            firebase_json = os.getenv(
                "FIREBASE_SERVICE_ACCOUNT", ""
            ).strip()

            if firebase_json:

                service_account = json.loads(
                    firebase_json
                )

                cred = credentials.Certificate(
                    service_account
                )

            # LOCAL PYCHARM CONNECTION
            else:

                credential_path = os.getenv(
                    "GOOGLE_APPLICATION_CREDENTIALS",
                    "ServiceAccountKey.json"
                )

                path = Path(credential_path)

                if not path.is_absolute():
                    path = BASE / path

                if not path.is_file():
                    raise FileNotFoundError(
                        f"Firebase credentials not found: {path}"
                    )

                cred = credentials.Certificate(
                    str(path)
                )

            firebase_app = firebase_admin.initialize_app(
                cred
            )

        return firestore.client(app=firebase_app)
