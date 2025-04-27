# PyChronix 🕒

A powerful and comprehensive Python package for advanced datetime operations and AI-powered time analysis. Simplify your date and time handling with this easy-to-use package.

## ✨ Features

- 📅 Advanced date and time manipulation
- 🌍 Timezone handling with 500+ timezones
- 📝 Date formatting and parsing
- ➕ Date arithmetic operations
- 🏢 Business day calculations
- 🎂 Age calculations
- 📊 Month-end date calculations
- 🎯 Leap year detection
- 🤖 AI-powered time analysis (coming soon)
- 📈 ML-based time series analysis (coming soon)

## 🚀 Installation

```bash
pip install pychronix
```

## 📚 Usage

```python
from pychronix import DateTimeUtils

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

# Convert timezone
ny_time = dt.convert_timezone(current, "America/New_York")

# Calculate business days between dates
business_days = dt.get_business_days_between(start_date, end_date)
```

## 🔧 Advanced Usage

### Timezone Handling
```python
# Get list of all available timezones
timezones = dt.get_timezone_list()

# Create instance with specific timezone
dt_tokyo = DateTimeUtils("Asia/Tokyo")
```

### Business Day Operations
```python
# Get next business day
next_business = dt.get_next_business_day(current)

# Get previous business day
prev_business = dt.get_previous_business_day(current)
```

### Date Utilities
```python
# Calculate age
age = dt.get_age(birth_date)

# Check leap year
is_leap = dt.is_leap_year(2024)

# Get last day of month
last_day = dt.get_last_day_of_month(date)
```

## 📋 Requirements

- Python >= 3.6
- pytz >= 2023.3
- python-dateutil >= 2.8.2

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 