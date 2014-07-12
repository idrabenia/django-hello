from django.db import models


def populate_model(klass, **attrs):
    instance = klass()

    for key in attrs.keys():
        try:
            setattr(instance, key, attrs[key])
        except Exception:
            pass

    return instance


def char_field(**kwargs):
    return models.CharField(max_length=255, **kwargs)


class Address(models.Model):
    is_primary = models.BooleanField(default=False)
    country = char_field()
    city = char_field()
    address1 = char_field()
    address2 = char_field(blank=True, null=True)
    address3 = char_field(blank=True, null=True)


class User(models.Model):
    first_name = char_field()
    last_name = char_field()
    created = models.DateTimeField(auto_now_add=True)
    birth_year = models.PositiveIntegerField()
    email = models.EmailField()
    addresses = models.ManyToManyField(Address, through="UserAddresses")
    primary_address = models.ForeignKey(Address, related_name="+", default=None, null=True)

    @staticmethod
    def create(**kwargs):
        address = populate_model(Address, is_primary=True, **kwargs)
        address.save()

        user = populate_model(User, primary_address=address, **kwargs)
        user.save()

        UserAddresses(user=user, address=address).save()
        return user


class UserAddresses(models.Model):
    user = models.ForeignKey(User)
    address = models.ForeignKey(Address)