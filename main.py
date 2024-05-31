from fastapi import FastAPI, HTTPException, Depends
from app.model import UserSchema, UserLoginSchema, PostSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import JWTBearer
from database import session,User
 
app = FastAPI()
data=[
    {
    "id":1,
    "company_name": "tcs",
    "company_details":"tcs company"
},
{
    "id":2,
    "company_name": "genpact",
    "company_details":"genpact company"
},
]


@app.get("/home",tags=["default"])
def home():
    return {"welcome": "new user"}

@app.get("/data",tags=['retrive'])
def get_data():
    return {"data": data}

@app.post("/user/register",tags=["auth"])
def user_register(user: UserSchema):
    db_user = session.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(firstname=user.firstname,lastname=user.lastname, email=user.email, password=user.password)
    session.add(new_user)
    try:
        session.commit()
    except Exception as er:
        session.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error: " + str(er))
    return signJWT(user.email)

@app.post("/user/login",tags=["auth"])
def user_login(user: UserLoginSchema):
    user_db = session.query(User).filter_by(email=user.email).first()
    if user_db and user_db.password == user.password:
        return signJWT(user.email)
    else:
        return{"Invalid ":"login details"}

@app.post("/new", dependencies=[Depends(JWTBearer())],tags=["add"])
def post_data(new_post: PostSchema):
    new_post.id = len(data) + 1
    data.append(new_post.model_dump())
    return {"data": "has been added"}


