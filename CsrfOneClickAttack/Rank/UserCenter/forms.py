from django.forms import ModelForm, CharField, ValidationError
from .models import User


class RegisterForm(ModelForm):
    confirmPassword = CharField(required=True, max_length=15,
                                min_length=7, error_messages=
        {
            "required": "密码不能为空",
            "max_length": "密码长度最大为15个字符",
            "min_length": "密码长度最小为7个字符"
        })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ModelForm.__init__(self, *args, **kwargs)
        # super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["nickname"].required = False

    class Meta:
        model = User
        exclude = ["money"]
        error_messages = {
            "username": {
                "required": "用户名不能为空",
                "invalid": "邮箱地址格式有误",
                'unique': "用户已存在，不要重复注册"
            },
            "password": {
                "required": "密码不能为空",
                "max_length": "密码长度最大为15个字符",
                "min_length": "密码长度最小为7个字符"
            },
            "telphone": {
                "required": "手机号不能为空",
                "invalid": "请输入正确手机号"
            },
            "nickname": {
                "max_length": "昵称最大为10个字符"
            }
        }

    def clean(self):
        cleanData = super().clean()

        messages = self.errors.get_json_data()

        if not messages:
            password = cleanData.get("password")
            confirmPassword = cleanData.get("confirmPassword")

            if password != confirmPassword:
                raise ValidationError(message="两次密码输入不一致")

            # username = cleanData.get("username")
            # exists = User.objects.filter(username=username).exists()
            #
            # if exists:
            #     raise ValidationError(message="用户已存在，不要重复注册")

        return cleanData

    def get_errors(self):
        return getErrorsList(self)


class LoginForm(ModelForm):

    class Meta:
        model = User
        fields = ["username", "password"]
        error_messages = {
            "username": {
                "required": "用户名不能为空",
                "invalid": "邮箱地址格式有误",
            },
            "password": {
                "required": "密码不能为空",
            }
        }

    def clean(self):
        cleanData = super().clean()

        messages = self.errors.get_json_data()
        if not messages:
            username = cleanData.get("username")
            password = cleanData.get("password")

            user = User.objects.filter(username=username, password=password).first()
            if not user:
                raise ValidationError(message="用户名或者密码不存在")

            self.__user = user

        return cleanData

    @property
    def errors(self):
        errors = super().errors
        if errors and len(errors) == 1:
            for valueList in errors.values():
                for value in valueList:
                    if "Username already exists" in value:
                        return {}
        return errors

    @property
    def getUser(self):
        return self.__user

    def get_errors(self):
        return getErrorsList(self)


def getErrorsList(self):
    errors = self.errors.get_json_data()
    messages = []

    for itemList in errors.values():
        for item in itemList:
            messages.append(item.get("message"))

    return messages
