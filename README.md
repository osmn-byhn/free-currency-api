# Currency Exchange Rate API

This Flask application fetches exchange rate data from Google Finance and provides it through an API. Users can retrieve exchange rate information for a given base currency and target currency.

## Features

- Allows users to get exchange rate data for a given base and target currency.
- Provides exchange rate data in JSON format through an API.
- Includes a web interface to view exchange rates.

## Requirements

- Python 3.x
- Flask
- Requests
- BeautifulSoup4

## Installation

1. Install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Start the Flask application:

    ```bash
    python app.py
    ```

3. The application will start running at `http://127.0.0.1:5000/`.

## Usage

### Web Interface

Navigate to the homepage (`http://127.0.0.1:5000/`) to view the exchange rate data visually.

### API

You can retrieve exchange rate data by using the following endpoint:

- **GET /api**
  - **Parameters**:
    - `base`: Base currency (default: `EUR`)
    - `target`: Target currency (default: `TRY`)

#### Example Request

```bash
GET /api?base=USD&target=TRY
```

#### Example Response

```json
{
  "base_currency": "USD",
  "target_currency": "TRY",
  "exchange_rate": "18.456"
}
```

If there is an issue fetching the data, you will receive the following error message:

```json
{
  "error": "Could not fetch exchange rate"
}
```

## Development

This project is developed using Flask. Feel free to fork the repository and make any changes you like.

## License

This project is licensed under the [MIT License](LICENSE).
```

This should cover the necessary details for your project in English. Let me know if you'd like any changes!