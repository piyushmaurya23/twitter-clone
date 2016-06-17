from rest_framework import serializers

from .models import User


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'mobile_number', 'about_me', 'profile_pic', 'location')
        read_only_fields = ('email',)

# class RegisterSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
#     first_name = serializers.CharField(required=True, write_only=True)
#     last_name = serializers.CharField(required=True, write_only=True)
#     password1 = serializers.CharField(required=True, write_only=True)
#     password2 = serializers.CharField(required=True, write_only=True)
#
#     def validate_email(self, email):
#         email = get_adapter().clean_email(email)
#         if allauth_settings.UNIQUE_EMAIL:
#             if email and email_address_exists(email):
#                 raise serializers.ValidationError(
#                     _("A user is already registered with this e-mail address."))
#         return email
#
#     def validate_password1(self, password):
#         return get_adapter().clean_password(password)
#
#     def validate(self, data):
#         if data['password1'] != data['password2']:
#             raise serializers.ValidationError(
#                 _("The two password fields didn't match."))
#         return data
#
#     def get_cleaned_data(self):
#         return {
#             'first_name': self.validated_data.get('first_name', ''),
#             'last_name': self.validated_data.get('last_name', ''),
#             'password1': self.validated_data.get('password1', ''),
#             'email': self.validated_data.get('email', ''),
#         }
#
#     def save(self, request):
#         adapter = get_adapter()
#         user = adapter.new_user(request)
#         self.cleaned_data = self.get_cleaned_data()
#         adapter.save_user(request, user, self)
#         setup_user_email(request, user, [])
#         user.profile.save()
#         return user


# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True, allow_blank=False)
#     password = serializers.CharField(style={'input_type': 'password'})
#
#     def _validate_email(self, email, password):
#         user = None
#
#         if email and password:
#             user = authenticate(email=email, password=password)
#         else:
#             msg = _('Must include "email" and "password".')
#             raise exceptions.ValidationError(msg)
#
#         return user
