# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Index, Integer, Numeric, String, text
from database import db


Base = db.Model
metadata = Base.metadata


def to_dict(self):
    """
    model 对象转 字典
    model_obj.to_dict()
    """
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

Base.to_dict = to_dict


class Admin(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True, server_default=text("''"))
    password = Column(String(60), nullable=False, server_default=text("''"))
    area_id = Column(Integer, nullable=False, server_default=text("'0'"))
    area_code = Column(String(4), nullable=False, server_default=text("''"))
    phone = Column(String(20), nullable=False, server_default=text("''"))
    role = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    login_time = Column(DateTime)
    login_ip = Column(String(20))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class ApplyGet(Base):
    __tablename__ = 'apply_get'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)
    type_apply = Column(Integer, nullable=False, server_default=text("'0'"))
    money_apply = Column(Numeric(8, 2), nullable=False, server_default=text("'0.00'"))
    money_order = Column(Numeric(8, 2), nullable=False, server_default=text("'0.00'"))
    status_apply = Column(Integer, nullable=False, server_default=text("'0'"))
    status_order = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class ApplyPut(Base):
    __tablename__ = 'apply_put'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)
    type_apply = Column(Integer, nullable=False, server_default=text("'0'"))
    money_apply = Column(Numeric(8, 2), nullable=False, server_default=text("'0.00'"))
    money_order = Column(Numeric(8, 2), nullable=False, server_default=text("'0.00'"))
    status_apply = Column(Integer, nullable=False, server_default=text("'0'"))
    status_order = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class AreaCode(Base):
    __tablename__ = 'area_code'

    id = Column(Integer, primary_key=True)
    short_code = Column(String(2), nullable=False, server_default=text("''"))
    area_code = Column(String(4), nullable=False, server_default=text("''"))
    phone_pre = Column(String(7), nullable=False, server_default=text("''"))
    name_c = Column(String(20), nullable=False, server_default=text("''"))
    name_e = Column(String(20), nullable=False, server_default=text("''"))
    country_area = Column(String(20), nullable=False, server_default=text("''"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class BitCoin(Base):
    __tablename__ = 'bit_coin'

    user_id = Column(Integer, primary_key=True)
    amount = Column(Numeric(10, 0), nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class BitCoinItem(Base):
    __tablename__ = 'bit_coin_item'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)
    type = Column(Integer, nullable=False, server_default=text("'0'"))
    amount = Column(Numeric(8, 0), nullable=False, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Bonus(Base):
    __tablename__ = 'bonus'

    user_id = Column(Integer, primary_key=True)
    amount = Column(Numeric(10, 0), nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class BonusItem(Base):
    __tablename__ = 'bonus_item'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)
    type = Column(Integer, nullable=False, server_default=text("'0'"))
    amount = Column(Numeric(8, 0), nullable=False, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Complaint(Base):
    __tablename__ = 'complaint'

    id = Column(Integer, primary_key=True)
    send_user_id = Column(Integer, nullable=False, index=True)
    reply_admin_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    content_send = Column(String(512), nullable=False, server_default=text("''"))
    content_reply = Column(String(512), nullable=False, server_default=text("''"))
    status_reply = Column(Integer, nullable=False, server_default=text("'0'"))
    reply_time = Column(DateTime)
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Credit(Base):
    __tablename__ = 'credit'

    user_id = Column(Integer, primary_key=True)
    behavior = Column(Numeric(3, 0), nullable=False, server_default=text("'0'"))
    characteristics = Column(Numeric(3, 0), nullable=False, server_default=text("'0'"))
    connections = Column(Numeric(3, 0), nullable=False, server_default=text("'0'"))
    history = Column(Numeric(3, 0), nullable=False, server_default=text("'0'"))
    performance = Column(Numeric(3, 0), nullable=False, server_default=text("'0'"))
    credit = Column(Numeric(3, 0), nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    send_user_id = Column(Integer, nullable=False, index=True)
    receive_user_id = Column(Integer, nullable=False, index=True)
    content_send = Column(String(512), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    apply_put_id = Column(Integer, nullable=False, index=True)
    apply_get_id = Column(Integer, nullable=False, index=True)
    apply_put_uid = Column(Integer, nullable=False, index=True)
    apply_get_uid = Column(Integer, nullable=False, index=True)
    type = Column(Integer, nullable=False, server_default=text("'0'"))
    money = Column(Numeric(8, 2), nullable=False, server_default=text("'0.00'"))
    status_audit = Column(Integer, nullable=False, server_default=text("'0'"))
    status_flow = Column(Integer, nullable=False, server_default=text("'0'"))
    status_pay = Column(Integer, nullable=False, server_default=text("'0'"))
    status_rec = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    audit_time = Column(DateTime)
    pay_time = Column(DateTime)
    receipt_time = Column(DateTime)
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class OrderFlow(Base):
    __tablename__ = 'order_flow'

    order_id = Column(Integer, primary_key=True)
    flow_order_id = Column(Integer, nullable=False, index=True)
    apply_put_id = Column(Integer, nullable=False, index=True)
    apply_get_id = Column(Integer, nullable=False, index=True)
    apply_put_uid = Column(Integer, nullable=False, index=True)
    apply_get_uid = Column(Integer, nullable=False, index=True)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Score(Base):
    __tablename__ = 'score'

    user_id = Column(Integer, primary_key=True)
    amount = Column(Numeric(10, 0), nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class ScoreItem(Base):
    __tablename__ = 'score_item'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)
    type = Column(Integer, nullable=False, server_default=text("'0'"))
    amount = Column(Numeric(8, 0), nullable=False, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    status_active = Column(Integer, nullable=False, server_default=text("'0'"))
    status_lock = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    active_time = Column(DateTime)
    lock_time = Column(DateTime)
    delete_time = Column(DateTime)
    reg_ip = Column(String(20))
    login_ip = Column(String(20))
    login_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class UserAuth(Base):
    __tablename__ = 'user_auth'
    __table_args__ = (
        Index('type_auth', 'type_auth', 'auth_key', unique=True),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    type_auth = Column(Integer, nullable=False, server_default=text("'0'"))
    auth_key = Column(String(60), nullable=False, server_default=text("''"))
    auth_secret = Column(String(60), nullable=False, server_default=text("''"))
    status_verified = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class UserBank(Base):
    __tablename__ = 'user_bank'

    user_id = Column(Integer, primary_key=True)
    account_name = Column(String(60), nullable=False, server_default=text("'0'"))
    bank_name = Column(String(60), nullable=False, server_default=text("''"))
    bank_address = Column(String(60), nullable=False, server_default=text("''"))
    bank_account = Column(String(32), nullable=False, server_default=text("''"))
    status_verified = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class UserProfile(Base):
    __tablename__ = 'user_profile'

    user_id = Column(Integer, primary_key=True)
    user_pid = Column(Integer, nullable=False, server_default=text("'0'"))
    nickname = Column(String(20), nullable=False, server_default=text("''"))
    type_level = Column(Integer, nullable=False, server_default=text("'0'"))
    avatar_url = Column(String(60))
    email = Column(String(60), nullable=False, server_default=text("''"))
    area_id = Column(Integer, nullable=False, server_default=text("'0'"))
    area_code = Column(String(4), nullable=False, server_default=text("''"))
    phone = Column(String(20), nullable=False, server_default=text("''"))
    birthday = Column(Date, nullable=False, server_default=text("'1900-01-01'"))
    id_card = Column(String(32), nullable=False, server_default=text("''"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Wallet(Base):
    __tablename__ = 'wallet'

    user_id = Column(Integer, primary_key=True)
    amount_initial = Column(Numeric(10, 2), nullable=False, server_default=text("'0.00'"))
    amount_current = Column(Numeric(10, 2), nullable=False, server_default=text("'0.00'"))
    amount_lock = Column(Numeric(10, 2), nullable=False, server_default=text("'0.00'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class WalletItem(Base):
    __tablename__ = 'wallet_item'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True)
    type = Column(Integer, nullable=False, server_default=text("'0'"))
    money = Column(Numeric(8, 2), nullable=False, server_default=text("'0.00'"))
    sc_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
