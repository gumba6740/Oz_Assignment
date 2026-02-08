from db import DATABASE as db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    boards = db.relationship("Board", back_populates="author", lazy="dynamic")

    """
    db.relationship은 파이썬 객체의 이동 통로
    back_populates 통로를 동일화
    lazy가 dynamic인 경우 Query객체 반환. sqlAlchemy 기능 사용 가능. 1 대 다인 경우에 쓴다
    lazy가 selecet인 경우 리스트 객체 반환. 파이썬 기능으로 처리
    """




class Board(db.Model):
    __tablename__ = "boards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = db.relationship("User", back_populates="boards")