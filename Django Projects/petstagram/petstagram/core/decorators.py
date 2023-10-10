def is_owner(request, obj):
    return request.user == obj.user


# For class-based views!!!
# class OwnerRequiredMixin:
#     def get(self, request, *args, **kwargs):
#         result = super().get(request, *args, **kwargs)
#
#         if request.user == self.object.user:
#             return result
#         else:
#             return
        # redirect to anything if no owner!
    #
    # def post(self, request, *args, **kwargs):
    #     result = super().get(request, *args, **kwargs)
    #
    #
    #     if request.user == self.object.user:
    #         return ..............
    #
    # def put(.......):
