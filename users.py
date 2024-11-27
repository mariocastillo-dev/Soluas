from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext

# Setting up the SQLAlchemy Base and Engine
Base = declarative_base()
DATABASE_URL = "mysql+mysqlconnector://Admin:Admin@localhost:3306/soluas"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

# User Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    ID_documento = Column(Integer, unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

# Creating the Users table in the database
Base.metadata.create_all(bind=engine)

# CRUD Operations for User
class UserCRUD:
    def __init__(self):
        self.session = SessionLocal()

    def create_user(self, ID_documento: int, nombre: str, email: str, password: str):
        try:
            # Check if the user already exists
            existing_user = self.session.query(User).filter((User.ID_documento == ID_documento) | (User.email == email)).first()
            if existing_user:
                return "User with this ID_documento or email already exists."

            # Hash the password
            hashed_password = get_password_hash(password)

            # Create and store the new user
            new_user = User(ID_documento=ID_documento, nombre=nombre, email=email, hashed_password=hashed_password)
            self.session.add(new_user)
            self.session.commit()
            return "User registered successfully."
        except Exception as e:
            self.session.rollback()
            return f"An error occurred: {str(e)}"
        finally:
            self.session.close()

    def get_user(self, ID_documento: int):
        try:
            user = self.session.query(User).filter(User.ID_documento == ID_documento).first()
            if user:
                return {
                    "id": user.id,
                    "ID_documento": user.ID_documento,
                    "nombre": user.nombre,
                    "email": user.email
                }
            return "User not found."
        except Exception as e:
            return f"An error occurred: {str(e)}"
        finally:
            self.session.close()

    def update_user(self, ID_documento: int, nombre: str = None, email: str = None, password: str = None):
        try:
            user = self.session.query(User).filter(ID_documento == ID_documento).first()
            if not user:
                return "User not found."

            if nombre:
                user.nombre = nombre
            if email:
                user.email = email
            if password:
                user.hashed_password = get_password_hash(password)

            self.session.commit()
            return "User updated successfully."
        except Exception as e:
            self.session.rollback()
            return f"An error occurred: {str(e)}"
        finally:
            self.session.close()

    def delete_user(self, ID_documento: int):
        try:
            user = self.session.query(User).filter(ID_documento == ID_documento).first()
            if not user:
                return "User not found."

            self.session.delete(user)
            self.session.commit()
            return "User deleted successfully."
        except Exception as e:
            self.session.rollback()
            return f"An error occurred: {str(e)}"
        finally:
            self.session.close()
