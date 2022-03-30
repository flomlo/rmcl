import datetime
import enum

RFC3339Nano = "%Y-%m-%dT%H:%M:%SZ"

DEFAULT_TOKEN_SERVER_URL = "https://webapp-production-dot-remarkable-production.appspot.com"
DEFAULT_SERVICE_MGR_SERVER_URL = "https://service-manager-production-dot-remarkable-production.appspot.com"
DEVICE_REGISTER_URL = "https://my.remarkable.com/device/desktop/connect"

USER_AGENT = "rmcl <https://github.com/rschroll/rmcl>"

DEVICE_TOKEN_PATH = "/token/json/2/device/new"
USER_TOKEN_PATH = "/token/json/2/user/new"
SERVICE_MGR_PATH = "/service/json/1/document-storage?environment=production&group=auth0%7C5a68dc51cb30df3877a1d7c4&apiVer=2"  # noqa

USER_TOKEN_VALIDITY = 24 * 60 * 60  # Guessing one day
DEVICE = "desktop-windows"
# Number of bytes of file to request to get file size of source doc
# For notes, the central directory runs 5 pages / KB, as a rough guess
NBYTES = 1024*100
FILE_LIST_VALIDITY = datetime.timedelta(minutes=5)
ROOT_ID=''
TRASH_ID='trash'


class FileType(enum.Enum):
    pdf = 'pdf'
    epub = 'epub'
    notes = 'notes'
    unknown = 'unknown'

    def __str__(self):
        return self.name
