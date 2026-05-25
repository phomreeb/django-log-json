import contextvars

client_ip_var = contextvars.ContextVar("client_ip", default=None)

class RequestIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = self.get_client_ip(request)
        # ไม่ต้อง reset token เพื่อให้ WSGI Server (เช่น runserver logger)
        # ยังคงดึง IP ไปเขียนลง log ได้หลังจากที่ response ถูกส่งกลับไปแล้ว
        client_ip_var.set(ip)
        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
