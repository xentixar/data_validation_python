from validation.validator import Validator

data = {
    'name' : 'Validator',
    'email' : 'validator@example.com'
}

validator = Validator(data)

validated = validator.validate({
    'name' : 'required|min:20',
    'email' : 'required|email'
})

error = validator.message

print(error)