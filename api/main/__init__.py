# 모듈 선언
from flask import Flask

from . import userImage
from . import userRank
from . import userInfo
from . import userEquipment
from . import userInventory
from . import userStorage
from . import userGuild

from . import test


app = Flask(__name__)

# 한글 설정
app.config['JSON_AS_ASCII'] = False

# 정렬 설정
app.config['JSON_SORT_KEYS'] = False

# 블루 프린트
app.register_blueprint(userImage.blue_userImage)
app.register_blueprint(userRank.blue_userRank)
app.register_blueprint(userInfo.blue_userInfo)
app.register_blueprint(userEquipment.blue_userEquipment)
app.register_blueprint(userInventory.blue_userInventory)
app.register_blueprint(userStorage.blue_userStorage)
app.register_blueprint(userGuild.blue_userGuild)

app.register_blueprint(test.blue_test)