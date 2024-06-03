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
def home() : #->dict[str,str]:

    return {"welcome": "new user"}

@app.get("/data",tags=['retrive'])
def get_data() :#-> dict[str]:
    return {"data": data}

@app.post("/user/register",tags=["auth"])
def user_register(user: UserSchema) :#-> str:
    """
    The user_register function creates a new user in the database.
    It takes a UserSchema object as input, and returns an access token for that user.
    
    :param user: UserSchema: Create a new user object
    :return: A jwt token which is used to authenticate the user

    """
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
def user_login(user: UserLoginSchema): #-> (dict[str,str] ):
    """
    The user_login function takes a user object and returns a JWT token if the login details are valid.
        If the login details are invalid, it returns an error message.
    
    :param user: UserLoginSchema: Validate the input
    :return: A jwt token on successful login
    """
    user_db = session.query(User).filter_by(email=user.email).first()
    if user_db and user_db.password == user.password:
        return signJWT(user.email)
    else:
        return{"Invalid ":"login details"}
    

@app.post("/new", dependencies=[Depends(JWTBearer())],tags=["add"])
def post_data(new_post: PostSchema) :#-> dict[str,str]:
    """
    The post_data function takes a new_post object and adds it to the data list.
    It returns a dictionary with the key data and value has been added.
    
    
    :param new_post: PostSchema: Specify the type of data that is being passed into the function
    :return: A dictionary with a key of data and a value of has been added
    """
    new_post.id = len(data) + 1
    data.append(new_post.model_dump())
    return {"data": "has been added"}


