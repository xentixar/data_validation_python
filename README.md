# Easy Python Data Validation

This is a simple python module for easy data validation.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Validation Rules](#validation-rules)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository or download the ZIP file.

```bash
git clone https://github.com/xentixar/data_validation_python.git
```

2. Navigate to the directory

```bash
cd data_validation_python
```

3. Run the example

```bash
python example.py
```

## Usage

1. Create an instance of the Validator class and pass data to it.

```python
data = {
    'name' : 'John',
    'email' : 'test@gmail.com',
}
validator = Validator(data);
```

2. Add validation rules using the validate method.

```python
validated = validator->validate([
    'name' : 'required|max:100',
    'email' : 'required|email|max:100',
])
```

## Validation Rules

The module supports the following validation rules:

* 'required' : Field must be present in the form data.
* 'email' :  Field must be a valid email address.
* 'number' :  Field must be a number.
* 'image' :  Field must be a valid email image.
* 'max:m' :  Maximum length for strings or maximum value for numbers.
* 'min:n' :  Minimum length for strings or minimum value for numbers.
* 'in:something,something_else' :  Field must be a value present in the data.
* 'alpha_dash' : Field can only contain alpha-numeric, underscores and dashes.

Image Validation is only available for form data.


## Examples

Check the example.py for sample usage of the data validation module.


## Contributing

* Fork the repository.
* Create a new branch: git checkout -b feature-name.
* Commit your changes: git commit -m 'Add new feature'.
* Push to the branch: git push origin feature-name.
* Submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

