from pathlib import Path
import django
from django.conf import settings


BASE_DIR = (Path(__file__).parent / "media_gallery").resolve()


def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR.parent / "db.sqlite3"
            }
        },
        INSTALLED_APPS=(
            "media_gallery",
        ),
        TIME_ZONE="GMT",
        USE_TZ=True,
    )
    django.setup()
