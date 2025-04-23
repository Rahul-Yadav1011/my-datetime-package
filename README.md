# My DateTime Package

A comprehensive Python package for datetime operations and utilities.

## Installation

```bash
pip install datetime_helper
```

## Features

- Date and time manipulation
- Timezone handling
- Date formatting and parsing
- Date arithmetic operations
- Holiday calculations
- Business day calculations

## Usage

```python
from my_datetime_package import DateTimeUtils

# Create a DateTimeUtils instance
dt = DateTimeUtils()

# Get current date and time
current = dt.now()

# Format date
formatted = dt.format_date(current, "YYYY-MM-DD")

# Add days to a date
future_date = dt.add_days(current, 5)

# Check if a date is a business day
is_business = dt.is_business_day(current)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 