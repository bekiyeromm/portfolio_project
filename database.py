from sqlalchemy import create_engine, text
engine = create_engine(
      "mysql+pymysql://pims_user:pims_user_pwd@localhost/pims_db?charset=utf8mb4")


def load_users_from_db():
	with engine.connect() as conn:
		result = conn.execute(text('select * from login'))
		result_dict = []
		for row in result.all():
			row_dict =row._asdict()#row object is converted to a dictionary using the _asdict()
			result_dict.append(row_dict)
		return result_dict
    
    