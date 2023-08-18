from app import db
from flask_login import UserMixin
from marshmallow import Schema, fields

# Define User data-model


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    # User fields
    active = db.Column(db.Boolean())
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    # Relationships
    roles = db.relationship("Role", secondary="user_roles")

    # Methods
    def role_names(self):
        roles = self.roles
        list_roles = []
        for role in roles:
            list_roles.append(role.name)

        return list_roles
        

    def has_roles(self, *requirements):
        role_names = self.role_names()
        for requirement in requirements:
            if isinstance(requirement, (list, tuple)):
                # this is a tuple_of_role_names requirement
                tuple_of_role_names = requirement
                authorized = False
                for role_name in tuple_of_role_names:
                    if role_name in role_names:
                        # tuple_of_role_names requirement was met: break out of loop
                        authorized = True
                        break
                if not authorized:
                    return False  # tuple_of_role_names requirement failed: return False
            else:
                # this is a role_name requirement
                role_name = requirement
                # the user must have this role
                if role_name not in role_names:
                    return False

        return True


# Define the Role data-model
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = "user_roles"
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id", ondelete="CASCADE"))
    role_id = db.Column(db.Integer(), db.ForeignKey("roles.id", ondelete="CASCADE"))


# Marsmallow schema for User model
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str()
    username = fields.Str()
    name = fields.Method("format_name", dump_only=True)

    def format_name(self, user):
        return "{} {}".format(user.first_name, user.last_name)
