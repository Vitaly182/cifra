from fastapi import APIRouter, HTTPException, Response
from routers.schemas import User, UserList, UpdateUserSchema
from datetime import datetime


users = [
    User(id=0, username='username_0', first_name='first_name_0', last_name='last_name_0', age=0, created_at=datetime.now()),
    User(id=1, username='username_1', first_name='first_name_1', last_name='last_name_1', age=1, created_at=datetime.now()),
    User(id=2, username='username_2', first_name='first_name_2', last_name='last_name_2', age=2, created_at=datetime.now()),
    User(id=3, username='username_3', first_name='first_name_3', last_name='last_name_3', age=3, created_at=datetime.now()),

    # {
    #     'id': 1,
    #     'username': 'username_1',
    #     'first_name': 'first_name_1',
    #     'last_name': 'last_name_1',
    #     'age': 1,
    #     'created_at': datetime.now(),
    # },
    # {
    #     'id': 2,
    #     'username': 'username_2',
    #     'first_name': 'first_name_2',
    #     'last_name': 'last_name_2',
    #     'age': 2,
    #     'created_at': datetime.now(),
    # },
    # {
    #     'id': 3,
    #     'username': 'username_3',
    #     'first_name': 'first_name_3',
    #     'last_name': 'last_name_3',
    #     'age': 3,
    #     'created_at': datetime.now(),
    # },
]

user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.get('/', name='Get all users', response_model=UserList)
def get_all_users():
    return UserList(count=len(users), users=users)


@user_router.post('/', name='Add user', response_model=User)
def create_user(user: User):
    users.append(user)
    return user


@user_router.get('/{user_id}', name='Get user', response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail='User not found')


@user_router.delete('/{user_id}', name='Delete user', response_model=None)
# @user_router.delete('/{user_id}', name='Delete user')
def delete_user(user_id: int):
    for i, user in enumerate(tuple(users)):
        if user.id == user_id:
            del users[i]
            break
    return Response(status_code=204)
    # return 204


@user_router.put('/{user_id}', name='Update user', response_model=User)
def update_user(user_id: int, new_user_data: UpdateUserSchema):
    for i in range(len(users)):
        if users[i].id == user_id:
            data = new_user_data.dict()
            for key in data:
                if data[key] is not None:
                    setattr(users[i], key, data[key])
            return users[i]
    raise HTTPException(status_code=404, detail='User not found')