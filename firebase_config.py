import os
import json
import logging
from pathlib import Path
from threading import RLock

from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore


BASE = Path(__file__).resolve().parent
load_dotenv(BASE / ".env")

_db = None
_lock = RLock()


def get_db():

    global _db

    with _lock:

        if _db is not None:
            return _db

        try:

            try:
                firebase_app = firebase_admin.get_app()

            except ValueError:

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
                            "Firebase service account file not found."
                        )

                    cred = credentials.Certificate(
                        str(path)
                    )

                firebase_app = firebase_admin.initialize_app(
                    cred
                )

            _db = firestore.client(app=firebase_app)

            logging.info(
                "Firebase client initialized: %s",
                _db.project
            )

            return _db

        except Exception:

            logging.exception(
                "Firebase initialization failed"
            )

            raise
