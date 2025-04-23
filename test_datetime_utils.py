from datetime_helper import DateTimeUtils
from datetime import datetime, timedelta
import pytz

def test_basic_functions():
    print("\n=== Testing Basic Functions ===")
    dt = DateTimeUtils()
    
    # Test now() function
    current_time = dt.now()
    print(f"Current time: {current_time}")
    
    # Test format_date
    formatted_date = dt.format_date(current_time, "YYYY-MM-DD HH:mm:ss")
    print(f"Formatted date: {formatted_date}")
    
    # Test add_days
    future_date = dt.add_days(current_time, 5)
    print(f"Date after 5 days: {future_date}")
    
    # Test is_business_day
    is_business = dt.is_business_day(current_time)
    print(f"Is business day: {is_business}")

def test_timezone_functions():
    print("\n=== Testing Timezone Functions ===")
    dt = DateTimeUtils()
    
    # Test timezone conversion
    dt_ny = DateTimeUtils("America/New_York")
    ny_time = dt_ny.now()
    print(f"New York time: {ny_time}")
    
    # Test timezone list
    timezones = dt.get_timezone_list()
    print(f"Number of available timezones: {len(timezones)}")
    print("Sample timezones:", timezones[:5])
    
    # Test different timezone
    dt_tokyo = DateTimeUtils("Asia/Tokyo")
    print(f"Tokyo time: {dt_tokyo.now()}")

def test_business_day_functions():
    print("\n=== Testing Business Day Functions ===")
    dt = DateTimeUtils()
    current = dt.now()
    
    # Test next business day
    next_business = dt.get_next_business_day(current)
    print(f"Next business day: {next_business}")
    
    # Test previous business day
    prev_business = dt.get_previous_business_day(current)
    print(f"Previous business day: {prev_business}")
    
    # Test business days between
    start_date = current
    end_date = dt.add_days(current, 10)
    business_days = dt.get_business_days_between(start_date, end_date)
    print(f"Business days between {start_date.date()} and {end_date.date()}: {business_days}")

def test_date_utility_functions():
    print("\n=== Testing Date Utility Functions ===")
    dt = DateTimeUtils()
    
    # Test age calculation
    birth_date = datetime(1990, 1, 1, tzinfo=pytz.UTC)
    age = dt.get_age(birth_date)
    print(f"Age for birth date {birth_date.date()}: {age} years")
    
    # Test leap year
    test_years = [2000, 2004, 2100, 2024]
    for year in test_years:
        is_leap = dt.is_leap_year(year)
        print(f"{year} is leap year: {is_leap}")
    
    # Test last day of month
    test_dates = [
        datetime(2024, 2, 1, tzinfo=pytz.UTC),
        datetime(2024, 4, 15, tzinfo=pytz.UTC),
        datetime(2024, 12, 1, tzinfo=pytz.UTC)
    ]
    for date in test_dates:
        last_day = dt.get_last_day_of_month(date)
        print(f"Last day of {date.strftime('%B %Y')}: {last_day.date()}")

if __name__ == "__main__":
    test_basic_functions()
    test_timezone_functions()
    test_business_day_functions()
    test_date_utility_functions() 