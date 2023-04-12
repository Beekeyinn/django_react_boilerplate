import datetime
from io import StringIO

import pandas as pd
from django.conf import settings


def dataframe_to_csv_to_string(dataframe: pd.DataFrame) -> str:
    csv_string_buffer = StringIO()
    # dataframe.to_csv(
    #     f"{settings.BASE_DIR}/csv/google_analytics_data_{datetime.datetime.now().strftime('%Y-%m-%d')}.csv",
    #     index=False,
    # )
    dataframe.to_csv(csv_string_buffer, index=False)
    return csv_string_buffer.getvalue()


def google_analytics_response_data_csv_string(index, columns, data):
    df = pd.DataFrame(index=index, columns=columns, data=data)

    string = dataframe_to_csv_to_string(df)
    return string
