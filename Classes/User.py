class Users(object):

    def __init__(self, first_name, last_name, gender, phone=None):

        gen = {'f': 'Female',
               'm': 'Male',
               'NA': 'Not available'}

        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.login_attempts = 0

        if not (gender.lower().startswith('f') or gender.lower().startswith('m')):
            self.gender = gen['NA']
        else:
            self.gender = gen[gender.lower()[0]]

    def describe_user(self):
        if self.phone is None:
            print 'Name : {0}\nPhone : {1} \nGender : {2}'.format(self.first_name+self.last_name, 'NA', self.gender)
        else:
            print 'Name : {0}\nPhone : {1} \nGender : {2}'.format(self.first_name + self.last_name, self.phone,
                                                                  self.gender)

    def greet_user(self):
        if self.gender is 'Female':
            print 'Hello Ms.', self.first_name, self.last_name
        elif self.gender is 'Male':
            print 'Hello Mr.', self.first_name, self.last_name
        else:
            print 'Hello', self.first_name, self.last_name

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
