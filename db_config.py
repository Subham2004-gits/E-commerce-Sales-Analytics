from sqlalchemy import create_engine

# Database connection string (with password encoded)
DATABASE_URI = "postgresql+psycopg2://postgres:Subham%402004@localhost:5432/Ecommerce_db"

def get_engine():
    return create_engine(DATABASE_URI)
