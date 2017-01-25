from coreapi import Document, Link, Field


BASE_URL = '/api/v1/'
BASE_AUTH_URL = BASE_URL + 'auth/'
BASE_ANALYTICS_URL = BASE_URL + 'analytics/'

SCHEMA = Document(
    title='Element API',
    content={
        'auth': {
            'register': Link(
                url=BASE_AUTH_URL + 'register/',
                action='post',
                description="""
                    Register a new user

                """,
                fields=[
                    Field(
                        name='email',
                        required=True,
                        location='formData',
                    ),
                    Field(
                        name='password',
                        required=True,
                        location='formData',
                    )
                ]
            ),
            'activate': Link(
                url=BASE_AUTH_URL + 'activate/',
                action='post',
                description="""
                    Activate account

                    Note: Accounts are activated automatically for now.
                """,
                fields=[
                    Field(
                        name='uid',
                        required=True,
                        location='formData',
                    ),
                    Field(
                        name='token',
                        required=True,
                        location='formData',
                    ),
                ],
            ),
            'login': Link(
                url=BASE_AUTH_URL + 'login/',
                action='post',
                description='User Login',
                fields=[
                    Field(
                        name='email',
                        required=True,
                        location="formData",
                        description='Email'
                    ),
                    Field(
                        name='password',
                        required=True,
                        location="formData",
                        description='Password'
                    ),
                    Field(
                        name='activate',
                        required=False,
                        location="formData",
                        type='boolean',
                        description='for non active users'
                    )
                ]
            ),
            'logout': Link(
                url=BASE_AUTH_URL + 'logout/',
                action='post',
                description="""
                User Logout

                Just removes the Token from the backend
                """,
                fields=[
                    Field(
                        name="Authorization",
                        required=False,
                        location="header",
                        description="ex. Token XXX"
                    ),
                ]
            ),
            'me': Link(
                url=BASE_AUTH_URL + 'me/',
                action='get',
                description='Get user details',
                fields=[
                    Field(
                        name="Authorization",
                        required=False,
                        location="header",
                        description="ex. Token XXX"
                    ),
                ]
            ),
            'update-me': Link(
                url=BASE_AUTH_URL + 'me/',
                action='patch',
                description="""
                    Update User Profile
                """,
                fields=[
                    Field(
                        name="Authorization",
                        required=False,
                        location="header",
                        description="ex. Token XXX"
                    ),
                    Field(
                        name='email',
                        required=False,
                        location='formData',
                    ),
                    Field(
                        name='first_name',
                        required=False,
                        location='formData',
                    ),
                    Field(
                        name='last_name',
                        required=False,
                        location='formData',
                    ),
                    Field(
                        name='instagram_handle',
                        required=False,
                        location='formData',
                    ),
                    Field(
                        name='birthdate',
                        required=False,
                        location='formData',
                    ),
                ]
            ),
            'change-password': Link(
                url=BASE_AUTH_URL + 'password/',
                action='post',
                description="""
                    Change Password
                """,
                fields=[
                    Field(
                        name="Authorization",
                        required=False,
                        location="header",
                        description="ex. Token XXX"
                    ),
                    Field(
                        name='current_password',
                        required=True,
                        location='formData',
                    ),
                    Field(
                        name='new_password',
                        required=True,
                        location='formData',
                    ),
                ],
            ),
            'reset-password': Link(
                url=BASE_AUTH_URL + 'password/reset/',
                action='post',
                description="""
                    Reset Password
                """,
                fields=[
                    Field(
                        name='email',
                        required=True,
                        location='formData',
                    ),
                ],
            ),
            'reset-password-confirm': Link(
                url=BASE_AUTH_URL + 'password/reset/confirm/',
                action='post',
                description="""
                    Reset Password confirm
                """,
                fields=[
                    Field(
                        name='uid',
                        required=True,
                        location='formData',
                    ),
                    Field(
                        name='token',
                        required=True,
                        location='formData',
                    ),
                    Field(
                        name='new_password',
                        required=True,
                        location='formData',
                    ),
                ],
            ),
            'suspend-my-account': Link(
                url=BASE_AUTH_URL + 'suspend-account/',
                action='post',
                description="""
                    Suspend My account
                """,
                fields=[
                    Field(
                        name="Authorization",
                        required=False,
                        location="header",
                        description="ex. Token XXX"
                    )
                ],
            ),
        },
    }
)
