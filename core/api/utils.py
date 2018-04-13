def use_serializer(serializer_class):
    def decorator(view):
        def wrapper(*args, **kwargs):
            self = args[0]
            original_serializer_class = self.serializer_class
            self.serializer_class = serializer_class
            response = view(*args, **kwargs)
            self.serializer_class = original_serializer_class
            return response
        return wrapper
    return decorator
