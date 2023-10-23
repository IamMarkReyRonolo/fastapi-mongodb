import re

def validate_fields(cls, values):
    values = is_not_empty(cls, values)
    values['email'] = check_email(cls, values['email'])
    values = password_must_be_valid(cls, values)
    return values

def validate_update_fields(cls, values):
    values = is_not_empty(cls, values)
    values['email'] = check_email(cls, values['email'])
    return values

def is_not_empty(cls, values):
    for attr, value in values.items():
        if(attr == "middle_name" or attr == 'created_by' or attr == 'updated_by'):
            continue
        else:
            if(str(value).strip() == "" and attr != 'school'):
                raise ValueError(f'{attr} field should not be empty')

            if attr == 'school' and "role" in values.keys() and values['role'] == 'subscriber':
                if str(value).strip() == "":
                    raise ValueError(f'{attr} field should not be empty')

    return values


def password_must_be_valid(cls, values):
    for attr, value in values.items():
        if(attr == "password" or attr == 'new_password' or attr == "old_password"):
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,30}$"

            # compiling regex
            pat = re.compile(reg)

            # searching regex
            mat = re.search(pat, value)

            # validating conditions
            if mat:
                pass
            else:
                raise ValueError(
                    'password is invalid: [a-z], [A-Z], [0-9],[@$!#%*?&], min: 8, max:30')

        if(attr == 'repeat_password'):
            if(values['password'] != value):
                raise ValueError('password do not match')
        
        if(attr == 'repeat_new_password'):
            if(values['new_password'] != value):
                raise ValueError('password do not match')
        

    return values

def check_email(cls, v):
    if v:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, v)):
            return v
        else:
            raise ValueError('email is invalid')
    else:
        raise ValueError('email field should not be empty')