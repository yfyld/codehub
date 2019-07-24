


###########################
# Flask Config
###########################
DEBUG = True
SECRET_KEY = 'abcd' if DEBUG else os.environ.get('SECRET_KEY',None)#
# Extract and use X-Forwarded-For/X-Forwarded-Proto headers?
ENABLE_PROXY_FIX = False
# max upload size 100MB
MAX_CONTENT_LENGTH = 1024 * 1024 * 100

#Custom for redis session
REDIS_HOST='127.0.0.1'
REDIS_PORT=6666




###########################
# SQLAchemy config
###########################
# deprecated SQLALCHEMY_COMMIT_ON_TEARDOWN=True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:342531@127.0.0.1:3333/chengxubao'
SQLALCHEMY_ECHO = True if DEBUG else False
SQLALCHEMY_TRACK_MODIFICATIONS = True if DEBUG else False
# SQLALCHEMY_POOL_SIZE=10
# SQLALCHEMY_POOL_TIMEOUT=60
# SQLALCHEMY_POOL_RECYCLE=2*60*60
# SQLALCHEMY_MAX_OVERFLOW=50



###########################
# Flask-Cache config
###########################
# null,simple,memcached,redis,filesystem
CACHE_TYPE = 'redis' 
CACHE_DEFAULT_TIMEOUT = 3600
CACHE_KEY_PREFIX = 'chengxubao_cache_'
CACHE_REDIS_HOST='127.0.0.1'
CACHE_REDIS_PORT='6666'
CACHE_REDIS_PASSWORD='342531'
CACHE_REDIS_DB=1 #0
# redis://username:password@localhost:6379/0
# CACHE_REDIS_URL = 'redis://root:342531@127.0.0.1:6666/0'



###########################
# Flask-Security config
###########################
# bcrypt, sha512_crypt, or pbkdf2_sha512
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = SECRET_KEY  # default None
# SECURITY_EMAIL_SENDER = MAIL_DEFAULT_SENDER
# SECURITY_LOGIN_URL = '/login'
# SECURITY_LOGOUT_URL = '/logout'
# SECURITY_REGISTER_URL='/register'
# SECURITY_RESET_URL='/reset'
# SECURITY_CHANGE_URL='/change'
# SECURITY_CONFIRM_URL='/confirm'
# SECURITY_POST_LOGIN_VIEW = '/'
# SECURITY_POST_LOGOUT_VIEW = '/'

# SECURITY_REGISTERABLE=True 是否允许用户注册。默认为False
# SECURITY_SEND_REGISTER_EMAIL=True #用户注册时是否发送邮件
# SECURITY_CONFIRMABLE=True #用户注册时是否需要确认邮件

# SECURITY_RECOVERABLE  是否允许密码重置，默认为False
SECURITY_TRACKABLE = True  # 默认为False，是否需要用户登录统计的相关信息。如果设为True，用户模型需要添加字段
SECURITY_CHANGEABLE = True  # 是否允许密码修改，默认为False。如果为True，那么交由SECURITY_CHANGE_URL处理。
# SECURITY_EMAIL_SUBJECT_REGISTER   注册确认邮件的主题。
# SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE
# SECURITY_EMAIL_SUBJECT_PASSWORD_RESET
# SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE
# SECURITY_EMAIL_SUBJECT_CONFIRM
# SECURITY_SEND_PASSWORD_CHANGE_EMAIL=True
# SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL=True
# SECURITY_CONFIRM_EMAIL_WITHIN 确认邮件链接失效时间，默认5 days.
# SECURITY_RESET_PASSWORD_WITHIN    密码重置邮件链接失效时间，默认5 days.
# SECURITY_DEFAULT_REMEMBER_ME  默认为False，是否允许记住我功能。