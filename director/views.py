import base64

from django.views.generic import TemplateView


def number_to_code(number: int):  # number starting with 9. e.g.: 9214835595
    number_bytes = number.to_bytes((number.bit_length() + 7) // 8, byteorder="big")
    code = base64.b32encode(number_bytes).decode()
    return code


def code_to_number(code: str):
    number_bytes = base64.b32decode(code)
    number = int.from_bytes(number_bytes, byteorder="big")
    return number


# Create your views here.

class GoView(TemplateView):
    template_name = "go.html"

    def get(self, request, *args, **kwargs):
        identity = self.kwargs.get("identity")
        identity_mail = f"{identity}@divar.dev"
        self.extra_context = {
            **(self.extra_context or {}),
            "identity_email": identity_mail,
            "identity": identity,
        }
        return super().get(self, request, *args, **kwargs)
