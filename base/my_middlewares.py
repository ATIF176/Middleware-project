from django.shortcuts import render, HttpResponse

# def my_middleware(get_response):
#     print("One Brother Time Initialization")
#     def my_function(request):
#         print("This will execute before view.")
#         response = get_response(request)
#         print("This will execute after view.")
#         return response
#     return my_function


# class MyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One Brother Time Initialization")

#     def __call__(self, request):
#         print("This will execute before view.")
#         response = self.get_response(request)
#         print("This will execute after view")
#         return response


# class BrotherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One Time Brother Initialization")

#     def __call__(self, request):
#         print("Brother will execute before view.")
#         response = self.get_response(request)
#         print("Brother will execute after view")
#         return response
    

# class FatherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One Time Father Initialization")

#     def __call__(self, request):
#         print("Father will execute before view.")
#         response = HttpResponse("Beware this type of work")
#         # response = self.get_response(request)
#         print("Father will execute after view")
#         return response


# class MotherMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One Time Mother Initialization")

#     def __call__(self, request):
#         print("Mother will execute before view.")
#         response = self.get_response(request)
#         print("Mother will execute after view")
#         return response


class MyProcessMiddleware:
    def __init__(self, get_reponse):
        self.get_response = get_reponse
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(request, *args, **kwargs):
        print("This is process view -Before view")
        return None
        # return HttpResponse("This will execute before view")


class MyExceptionMiddleware:
    def __init__(self, get_reponse):
        self.get_response = get_reponse
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_exception(self, request, exception):
        msg = exception
        print("Exception Occured!")
        return HttpResponse(msg)
        # return HttpResponse("This will execute before view")


class MyTemplateResponseMiddleware:
    def __init__(self, get_reponse):
        self.get_response = get_reponse
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_template_response(self, request, response):
        print("Process Template from Middleware")
        response.context_data['name'] = "Raza"
        return response