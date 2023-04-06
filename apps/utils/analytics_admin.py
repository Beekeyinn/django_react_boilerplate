import time

from decouple import config
from google.analytics.admin import AnalyticsAdminServiceClient
from google.analytics.admin_v1alpha.types import ListPropertiesRequest


class GoogleAnalyticsAdminAPI:
    __client__ = AnalyticsAdminServiceClient.from_service_account_json(
        config("GOOGLE_CREDENTIAL_KEY")
    )

    @staticmethod
    def google_analytics_property_list(account_id):
        request = ListPropertiesRequest(
            filter=f"parent:accounts/{account_id}", show_deleted=True
        )
        response = GoogleAnalyticsAdminAPI.__client__.list_properties(request=request)
        result = []
        for property in response:
            result.append(
                {
                    "property_id": property.name.split("/")[1],
                    "account_id": property.account.split("/")[1],
                    "property_name": property.display_name,
                    "timezone": property.time_zone,
                    "currency_code": property.currency_code,
                    "created_at": str(property.create_time).split(" ")[0],
                    "updated_at": str(property.update_time).split(" ")[0],
                }
            )
        return result
