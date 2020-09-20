import os


class Config:
    SECRET_KEY                     = "352afd99251a17dd38684431b46cdfa98ba6a25cb24a4cd3"
    SQLALCHEMY_DATABASE_URI        = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    MAIL_SERVER                    = "smtp.googlemail.com"
    MAIL_PORT                      = 587
    MAIL_USE_TLS                   = True
    MAIL_USERNAME                  = os.environ.get("EMAIL_ID")
    MAIL_PASSWORD                  = os.environ.get("EMAIL_PWD")

    RECAPTCHA_PUBLIC_KEY           = os.environ.get("RECAPTCHA_PBL_KEY")
    RECAPTCHA_PRIVATE_KEY          = os.environ.get("RECAPTCHA_PVT_KEY")
    RECAPTCHA_DATA_ATTRS           = {"theme": "dark"}
    TESTING                        = True
