from functools import wraps

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db.transaction import atomic
from google.api_core.exceptions import PermissionDenied
from openai.error import InvalidRequestError, OpenAIError, RateLimitError
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler as response_generator

from base.utils import debug_printer


def exception_handler(function, *args, **kwargs):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            with atomic():
                return function(*args, **kwargs)
        except ObjectDoesNotExist as odn_err:
            debug_printer(odn_err.__class__.__name__, str(odn_err), odn_err)
            return Response(
                {"error", "Detail Not Found"}, status=status.HTTP_400_BAD_REQUEST
            )
        except MultipleObjectsReturned as mor_err:
            debug_printer(mor_err.__class__.__name__, str(mor_err), mor_err)
            return Response(
                {"error": "Multiple Value Returned"}, status=status.HTTP_400_BAD_REQUEST
            )
        except ValidationError as validation_err:
            response = response_generator(validation_err, "")
            return response
        except (OpenAIError, RateLimitError, InvalidRequestError) as open_ai_err:
            debug_printer(open_ai_err.__class__.__name__, str(open_ai_err), open_ai_err)
            return Response(
                {"error": "Internal Server API"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except (PermissionDenied) as google_error:
            # debug_printer(
            #     google_error.__class__.__name__, str(google_error), google_error
            # )
            return Response(
                {"error": f"{google_error.message.split('.')[0]}."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except Exception as exc:
            debug_printer(exc.__class__.__name__, str(exc), exc)
            return Response(
                {"error": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    return wrapper
