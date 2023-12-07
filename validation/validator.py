from validation.rules import Rule
import re

class Validator(Rule):
    
    def __init__(self,data) -> None:
        self.data = data
        self.message = {}
        super().__init__()
        
    def default(self,*args,**kwargs):
        return
        
    def validate(self,rules:dict)->bool:
        for key,value in rules.items():
            values = value.split('|')
            for rule in values:
                _rule = rule.split(":")[0]
                if _rule in self.messages:
                    _rule = f"_{_rule}" if _rule=="in" else _rule
                    # If you are using the validation in form uncomment line 22 and comment the line 23
                    # if not Validator.__dict__.get(_rule,self.default)(self,self.data['_post'].get(key,""),key,rule):
                    if not Validator.__dict__.get(_rule,self.default)(self,self.data.get(key,""),key,rule):
                        break
                else:
                    print('Invalid Validation')
            
        if self.message:
            return False
        return True
    
    
    def required(self,value,field,rule):
        if value == '':
            self.message[field] = self.messages[rule].replace(':attr',field)
            return False
        return True
        
    def email(self,value,field,rule):
        pattern = r'[^\.\-][a-z\d\.\-]+@[a-z\d]+\.[a-z\d]+'
        if not re.match(pattern,value,re.IGNORECASE):
            self.message[field] = self.messages[rule].replace(':attr',field)
            return False
        return True
        
    def alpha_dash(self,value,field,rule):
        pattern = r'[^\_\-][a-z0-9\_\-]+'
        if not re.fullmatch(pattern,value,re.IGNORECASE):
            self.message[field] = self.messages[rule].replace(':attr',field)
            return False
        return True
        
    def min(self,value,field,rule):
        splitted_data = rule.split(':')
        if len(splitted_data) == 2:
            length = int(splitted_data[1])
            if len(value) < length:
                _rule = rule.split(":")[0]
                self.message[field] = self.messages[_rule].replace(':attr',field).replace(':value',str(length))
                return False
            
        return True
    
    def max(self,value,field,rule):
        splitted_data = rule.split(':')
        if len(splitted_data) == 2:
            length = int(splitted_data[1])
            if len(value) > length:
                _rule = rule.split(":")[0]
                self.message[field] = self.messages[_rule].replace(':attr',field).replace(':value',str(length))
                return False 
        return True
    
    def number(self,value:str,field,rule):
        if not value.isnumeric():
            self.message[field] = self.messages[rule].replace(':attr',field)
            return False
        return True
    
    def _in(self,value,field,rule):
        splitted_data = rule.split(':')
        splitted_data = splitted_data[-1].split(',')
        if value not in splitted_data:
            _rule = rule.split(":")[0]
            self.message[field] = self.messages[_rule].replace(':attr',field)
            return False
        return True

    # Image validation is only for form data
    def image(self,value,field,rule):
        if self.data.FILES.get(field) and 'image' not in self.data.FILES.get(field).content_type:
            self.message[field] = self.messages[rule].replace(':attr',field)
            return False
        elif not self.data.FILES.get(field):
            self.message[field] = self.messages[rule].replace(':attr',field)
            return False
        return True
    