from django import forms

class MessageForm(forms.Form):
    title = forms.CharField(max_length = 100, min_length = 3, label = "标题")
    content = forms.CharField(widget = forms.Textarea, label = "内容")
    email = forms.EmailField(label = "邮箱")
    reply = forms.BooleanField(required = False, label = "回复")


    def clean_title(self):
        flag = True
        if flag:
            raise forms.ValidationError(message = "错误信息")

    def clean(self):
        super().clean()
        # 可以通过self做最终数据判断