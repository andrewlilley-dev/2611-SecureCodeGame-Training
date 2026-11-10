# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os
from flask import Flask, request
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

class TaxPayer:
    _hasher = PasswordHasher()

    def __init__(self, username, raw_password):
        self.username = username
        self.password_hash = self._hasher.hash(raw_password)
        self.prof_picture = None
        self.tax_form_attachment = None

    def verify_password(self, candidate_password: str) -> bool:
        try:
            if self._hasher.verify(self.password_hash, candidate_password):
                if self._hasher.check_needs_rehash(self.password_hash):
                    self.password_hash = self._hasher.hash(candidate_password)
                return True
        except VerifyMismatchError:
            return False
        return False
    
    def base_path_checker(self, path):
        base_dir = os.path.realpath(os.getcwd())
        requested_path = os.path.realpath(path)

        try:
            if os.path.commonpath([base_dir, requested_path]) != base_dir:
                return False
        except ValueError:
            return False

        if not os.path.exists(requested_path):
            return False

        return True
    
    # returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        # setting a profile picture is optional
        if not path:
            pass

        # defends against path traversal attacks
        if path.startswith('/') or path.startswith('..') or path.startswith('./'):
            return None

        if not self.base_path_checker(path):
            return None

        # builds path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prof_picture_path = os.path.normpath(os.path.join(base_dir, path))

        with open(prof_picture_path, 'rb') as pic:
            picture = bytearray(pic.read())

        # assume that image is returned on screen after this
        return prof_picture_path

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        tax_data = None

        if not path:
            raise Exception("Error: Tax form is required for all users")

        if not self.base_path_checker(path):
            return None
        
        with open(path, 'rb') as form:
            tax_data = bytearray(form.read())

        # assume that tax data is returned on screen after this
        return path