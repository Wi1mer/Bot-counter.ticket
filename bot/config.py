import os
import json
from distutils.util import strtobool as stb

# with open("token.txt") as fname:
#     for lineas in fname:
#         T = lineas

# import os
# if os.path.isfile('../token.txt'):
#     print('El archivo existe.');
#     with open("../token.txt") as f:
#         firstline = f.readline().rstrip()
#         BOT_TOKEN = firstline
# else:
#     print('El no archivo existe.');


# print(firstline)

# --------------------------------------
#Token lrdfl
# BOT_TOKEN = ""
# --------------------------------------
#Token beta
BOT_TOKEN = ""

OWNER_ID = 294655685
# Example: OWNER_ID = 619418070
AUTHORISED_USERS = [1762721696, 1870286023]
# Example: AUTHORISED_USERS = [63055333, 100483029, -1003943959]
CHANNEL_ID = -1001257585889
GROUP_ID = -1001596325178 #m!m!rrorbot


# --------------------------------------

# dont edit below this >

BOT_TOKEN = os.environ.get('BOT_TOKEN', BOT_TOKEN)
OWNER_ID = int(os.environ.get('OWNER_ID', OWNER_ID))
AUTHORISED_USERS = json.loads(os.environ.get('AUTHORISED_USERS', json.dumps(AUTHORISED_USERS)))
CHANNEL_ID = int(os.environ.get('CHANNEL_ID', CHANNEL_ID))
GROUP_ID = int(os.environ.get('GROUP_ID', GROUP_ID))
AUTO_DELETE_MESSAGE_DURATION = 2



