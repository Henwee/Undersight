from Undersight import db, bcrypt
from Undersight.models import User

import pandas as pd

df = pd.read_csv('static/politician.csv')
print(df)

city = df['City'].tolist()
state = df['State'].tolist()
username = df['Mayor'].tolist()
party = df['Party'].tolist()

for i in range(0,len(city)):
    password = "12345"
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    email = username[i].replace(" ","").lower() + "@demo.com"
    address = city[i] + ", "+ state[i]
    user = User(username = username[i], email = email, password = hashed_password, userAddress= address, party = party[i])
    db.session.add(user)
    db.session.commit()

