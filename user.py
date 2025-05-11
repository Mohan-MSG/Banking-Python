from models import User as UserModel, Session

class User:
    @staticmethod
    def create(id, uname, phone, password):
        session = Session()
        user = UserModel(
            id=id,
            username=uname,
            phone=phone,
            password=password,
            total_balance=0
        )
        session.add(user)
        session.commit()
        session.close()
        return user

    @staticmethod
    def get_by_id(user_id):
        session = Session()
        user = session.query(UserModel).filter_by(id=user_id).first()
        session.close()
        return user

    @staticmethod
    def get_by_phone(phone):
        session = Session()
        user = session.query(UserModel).filter_by(phone=phone).first()
        session.close()
        return user