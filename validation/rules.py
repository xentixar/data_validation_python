class Rule():
    def __init__(self) -> None:
        self.messages = {
            'required' : "The :attr field is required.",
            'email' : "The :attr field should be a valid email address.",
            'number' : "The :attr field should be a number.",
            'image' : "The :attr field should be a valid image.",
            'max' : 'The :attr field should not be greater than :value characters.',
            'min' : 'The :attr field should not be less than :value characters.',
            'in' : 'The :attr field is invalid.',
            'alpha_dash' : 'The :attr can only contain alpha-numeric, underscores and dashes.',
        }