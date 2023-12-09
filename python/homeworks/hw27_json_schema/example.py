from pprint import pprint
import jsonschema
from jsonschema import validate, ValidationError


users_data = [
    {
        "email": "user1@example.com",
        "username": "user1"
    },
    {
        "email": "user2@example.com",
        "username": "user2"
    },
    {
        "email": "user3@example.com",
        "username": "user3"
    },
    {
        "email": "user4@example.com",
        "username": "user4"
    },
    {
        "email": "invalid-email",
        "username": "user5"
    },
    {
        "email": "user6@example.com",
        "username": "user6"
    },
    {
        "email": "user7@example.com",
        "username": "user7"
    },
    {
        "email": "user8@example.com",
        "username": "user8"
    },
    {
        "email": "user9@example.com",
        "username": "user9"
    },
    {
        "email": "user10@example.com",
        "username": "user10"
    },
    {
        "email": "user11@example.com",
        "username": "user11"
    },
    {
        "email": "user12@example.com",
        "username": "user12"
    },
    {
        "email": "user13@example.com",
        "username": "user13"
    },
    {
        "email": "user14@example.com",
        "username": "us14"
    },
    {
        "email": "invalid-email",
        "username": "user15"
    },
    {
        "email": "user16@example.com",
        "username": "user166666666666666666666"
    },
    {
        "email": "user17@example.com",
        "username": "user17"
    },
    {
        "email": "user18@example.com",
        "username": ""
    },
    {
        "email": 19,
        "username": "user19"
    },
    {
        "email": "user20example.com",
        "username": "user20"
    }
]


# # Создание схемы для валидации данных
schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string", "format": "email"},
        "username": {"type": "string", "minLength": 5, 'maxLength': 15}
    },
    "required": ["email", "username"],
    "additionalProperties": False
}


invalid_data = []
valid_data = []
for user in users_data:
    try:
        validate(instance=user, schema=schema, format_checker=jsonschema.FormatChecker())
        valid_data.append(user)
    except ValidationError as e:
        invalid_data.append(user)

print("Невалидные данные!!!")
pprint(invalid_data)
print("Валидные данные!!!")
pprint(valid_data)


input('\n\nНажмите "ENTER" для завершения.')