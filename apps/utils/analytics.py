from decouple import config
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)


def google_analytic_response_formatter(response, date_range):
    data = {
        "metrics": [metric.name for metric in response.metric_headers],
        "dimension": [dimension.name for dimension in response.dimension_headers],
    }
    dimensions = []
    result = {}
    csv = []
    for rowIdx, row in enumerate(response.rows):
        sub_dimension = []
        for i, dimension_value in enumerate(row.dimension_values):
            sub_dimension.append(dimension_value.value)
        dimension_name = " ".join(sub_dimension)
        metrics = {}
        for i, metric_value in enumerate(row.metric_values):
            metric_name = response.metric_headers[i].name
            metrics[metric_name] = metric_value.value
        result[dimension_name] = metrics
        dimensions.append(dimension_name)
        csv.append(metrics)
    data["sub_dimensions"] = dimensions
    data["result"] = result
    data["csv"] = csv
    if type(date_range) == list:
        data["date_range"] = date_range
    elif type(date_range) == dict:
        data["date_range"] = [date_range]
    else:
        data["date_range"] = None
    return data


class GoogleAnalyticsDataApi:
    __client___ = BetaAnalyticsDataClient.from_service_account_file(
        config("GOOGLE_CREDENTIAL_KEY")
    )

    @staticmethod
    def google_user_acquisition_data_api(start_date, end_date, property_id="316105199"):
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[
                DateRange(start_date=str(start_date), end_date=str(end_date)),
            ],
            dimensions=[
                Dimension(name="firstUserDefaultChannelGroup"),
            ],
            metrics=[
                Metric(name="active1DayUsers"),
                Metric(name="newUsers"),
                Metric(name="activeUsers"),
                Metric(name="totalUsers"),
                Metric(name="userConversionRate"),
                Metric(name="wauPerMau"),
            ],
        )
        response = GoogleAnalyticsDataApi.__client___.run_report(request)
        data = google_analytic_response_formatter(
            response, {"start_date": start_date, "end_date": end_date}
        )
        data["acquisition_type"] = "user"
        return data

    @staticmethod
    def google_traffic_acquisition_data_api(
        start_date, end_date, property_id="316105199"
    ):
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[
                DateRange(start_date=str(start_date), end_date=str(end_date)),
            ],
            dimensions=[
                Dimension(name="sessionDefaultChannelGroup"),
            ],
            metrics=[
                Metric(name="totalUsers"),
                Metric(name="engagedSessions"),
                Metric(name="sessions"),
                Metric(name="sessionsPerUser"),
                Metric(name="engagementRate"),
                Metric(name="userConversionRate"),
                Metric(name="eventsPerSession"),
                Metric(name="eventCount"),
                Metric(name="conversions"),
                Metric(name="totalRevenue"),
            ],
        )
        response = GoogleAnalyticsDataApi.__client___.run_report(request)
        data = google_analytic_response_formatter(
            response, {"start_date": start_date, "end_date": end_date}
        )

        data["acquisition_type"] = "traffic"
        return data

    @staticmethod
    def google_event_engagement_data_api(start_date, end_date, property_id="316105199"):
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[
                DateRange(start_date=str(start_date), end_date=str(end_date)),
            ],
            dimensions=[
                Dimension(name="eventName"),
            ],
            metrics=[
                Metric(name="totalUsers"),
                Metric(name="eventCount"),
                Metric(name="eventCountPerUser"),
                Metric(name="eventsPerSession"),
                Metric(name="eventValue"),
            ],
        )
        response = GoogleAnalyticsDataApi.__client___.run_report(request)
        data = google_analytic_response_formatter(
            response, {"start_date": start_date, "end_date": end_date}
        )

        data["engagement_type"] = "event"
        return data

    @staticmethod
    def google_conversion_engagement_data_api(
        start_date, end_date, property_id="316105199"
    ):
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[
                DateRange(start_date=str(start_date), end_date=str(end_date)),
            ],
            dimensions=[
                Dimension(name="eventName"),
            ],
            metrics=[
                Metric(name="conversions"),
                Metric(name="totalUsers"),
            ],
        )
        response = GoogleAnalyticsDataApi.__client___.run_report(request)
        data = google_analytic_response_formatter(
            response, {"start_date": start_date, "end_date": end_date}
        )

        data["engagement_type"] = "conversion"

        return data

    @staticmethod
    def google_pages_and_resources_engagement_data_api(
        start_date, end_date, property_id="316105199"
    ):
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[
                DateRange(start_date=str(start_date), end_date=str(end_date)),
            ],
            dimensions=[
                Dimension(name="unifiedScreenClass"),
            ],
            metrics=[
                Metric(name="screenPageViews"),
                Metric(name="totalUsers"),
                Metric(name="screenPageViewsPerUser"),
                Metric(name="engagementRate"),
                Metric(name="eventCount"),
                Metric(name="conversions"),
            ],
        )
        response = GoogleAnalyticsDataApi.__client___.run_report(request)
        data = google_analytic_response_formatter(
            response, {"start_date": start_date, "end_date": end_date}
        )

        data["engagement_type"] = "page and resources"

        return data

    @staticmethod
    def google_landing_page_engagement_data_api(
        start_date, end_date, property_id="316105199"
    ):
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[
                DateRange(start_date=str(start_date), end_date=str(end_date)),
            ],
            dimensions=[
                Dimension(name="landingPagePlusQueryString"),
            ],
            metrics=[
                Metric(name="sessions"),
                Metric(name="screenPageViewsPerSession"),
                Metric(name="totalUsers"),
                Metric(name="screenPageViewsPerUser"),
                Metric(name="engagedSessions"),
                Metric(name="engagementRate"),
                Metric(name="eventCount"),
                Metric(name="conversions"),
            ],
        )
        response = GoogleAnalyticsDataApi.__client___.run_report(request)
        data = google_analytic_response_formatter(
            response, {"start_date": start_date, "end_date": end_date}
        )

        data["engagement_type"] = "landing page"

        return data

    @staticmethod
    def google_ecommerce_monetisation_data_api(
        start_date, end_date, property_id="316105199"
    ):
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[
                DateRange(start_date=str(start_date), end_date=str(end_date)),
            ],
            dimensions=[
                Dimension(name="itemName"),
            ],
            metrics=[
                Metric(name="itemsViewed"),
                Metric(name="itemsAddedToCart"),
                Metric(name="totalPurchasers"),
            ],
        )
        response = GoogleAnalyticsDataApi.__client___.run_report(request)
        data = google_analytic_response_formatter(
            response, {"start_date": start_date, "end_date": end_date}
        )

        data["monetization_type"] = "ecommerce"

        return data

    @staticmethod
    def google_ads_publisher_monetisation_data_api(
        start_date, end_date, property_id="316105199"
    ):
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[
                DateRange(start_date=str(start_date), end_date=str(end_date)),
            ],
            dimensions=[
                Dimension(name="adUnitName"),
            ],
            metrics=[
                Metric(name="publisherAdClicks"),
                Metric(name="publisherAdImpressions"),
                Metric(name="totalAdRevenue"),
            ],
        )
        response = GoogleAnalyticsDataApi.__client___.run_report(request)
        data = google_analytic_response_formatter(
            response, {"start_date": start_date, "end_date": end_date}
        )

        data["monetization_type"] = "ads publisher"

        return data
