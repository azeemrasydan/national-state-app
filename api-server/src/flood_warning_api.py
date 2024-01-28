import httpx


def upsert_to_database(data):
    ## Please complete this
    print("Upsert the data: " + str(data) )


def perform_flood_warning_get_api():
    api_url = "https://api.data.gov.my/flood-warning/"

    try:
        with httpx.Client() as client:
            response = client.get(api_url)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    except httpx.RequestError as e:
        return None
