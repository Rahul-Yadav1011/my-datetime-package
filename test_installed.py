from datetime_helper import DateTimeUtils
from datetime import datetime
import pytz

def test_installed_package():
    print("\n=== Testing Installed Package ===")
    dt = DateTimeUtils()
    
    # Test basic functionality
    current_time = dt.now()
    print(f"Current time: {current_time}")
    
    # Test timezone conversion
    dt_ny = DateTimeUtils("America/New_York")
    ny_time = dt_ny.now()
    print(f"New York time: {ny_time}")
    
    # Test business day functions
    is_business = dt.is_business_day(current_time)
    print(f"Is business day: {is_business}")
    
    # Test date formatting
    formatted_date = dt.format_date(current_time, "YYYY-MM-DD HH:mm:ss")
    print(f"Formatted date: {formatted_date}")

if __name__ == "__main__":
    test_installed_package() 