# Currency Exchange Rate Converter

A Python command-line application that retrieves live exchange rates from the Frankfurter API and converts an amount between two currencies.

## Features

- Retrieves the latest exchange rates from a public REST API.
- Supports multiple currencies (EUR, USD, CAD, JPY, AUD, GBP).
- Validates user input for amounts and currency codes.
- Handles common API failures, including:
  - Connection errors
  - Timeouts
  - HTTP errors
  - Invalid JSON responses
- Uses a modular design based on separation of concerns.

## Technologies

- Python 3
- Requests
- REST API
- JSON

## Project Structure

| Function | Responsibility |
|----------|----------------|
| `get_amount()` | Prompt the user for a valid positive amount. |
| `get_currency()` | Collect and validate the source and target currencies. |
| `get_exchange_rate()` | Retrieve the latest exchange rate from the Frankfurter API. |
| `convert_currency()` | Calculate the converted amount. |
| `main()` | Coordinate the application workflow and handle exceptions. |

## Example

```text
Enter the amount you want to convert: 150

EUR | USD | CAD | JPY | AUD | GBP

Enter the currency to convert from:
USD

EUR | CAD | JPY | AUD | GBP

Enter the currency to convert to:
EUR

USD 150.00 = EUR 129.34
```

## Skills Demonstrated

- REST API integration
- HTTP requests using `requests`
- JSON parsing
- Input validation
- Exception handling
- Function design
- Separation of concerns
- Modular application architecture

## Future Improvements

- Add automated tests with `pytest`.
- Support decimal currency amounts.
- Refactor API requests to use the `params` argument provided by the `requests` library.
- Add support for historical exchange rates.
- Package the project as an installable command-line application.

## API

This project uses the free Frankfurter Exchange Rate API:

https://frankfurter.dev/

## License

This project is intended for educational purposes and portfolio demonstration.
