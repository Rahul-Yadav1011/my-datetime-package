from datetime import datetime, timedelta
import pytz
from typing import Union, Optional, List
from dateutil.relativedelta import relativedelta

class DateTimeUtils:
    def __init__(self, timezone: str = "UTC"):
        """
        Initialize DateTimeUtils with optional timezone.
        
        Args:
            timezone (str): Timezone string (default: "UTC")
        """
        self.timezone = pytz.timezone(timezone)

    def now(self) -> datetime:
        """
        Get current datetime in the specified timezone.
        
        Returns:
            datetime: Current datetime
        """
        return datetime.now(self.timezone)

    def format_date(self, date: datetime, format_str: str) -> str:
        """
        Format a datetime object according to the specified format string.
        
        Args:
            date (datetime): Date to format
            format_str (str): Format string (e.g., "YYYY-MM-DD")
            
        Returns:
            str: Formatted date string
        """
        format_mapping = {
            "YYYY": "%Y",
            "MM": "%m",
            "DD": "%d",
            "HH": "%H",
            "mm": "%M",
            "ss": "%S"
        }
        
        for key, value in format_mapping.items():
            format_str = format_str.replace(key, value)
            
        return date.strftime(format_str)

    def add_days(self, date: datetime, days: int) -> datetime:
        """
        Add days to a date.
        
        Args:
            date (datetime): Base date
            days (int): Number of days to add
            
        Returns:
            datetime: New date
        """
        return date + timedelta(days=days)

    def is_business_day(self, date: datetime) -> bool:
        """
        Check if a date is a business day (Monday to Friday).
        
        Args:
            date (datetime): Date to check
            
        Returns:
            bool: True if it's a business day, False otherwise
        """
        return date.weekday() < 5

    def get_timezone_list(self) -> list:
        """
        Get list of all available timezones.
        
        Returns:
            list: List of timezone strings
        """
        return pytz.all_timezones

    def convert_timezone(self, date: datetime, target_timezone: str) -> datetime:
        """
        Convert a datetime to a different timezone.
        
        Args:
            date (datetime): Date to convert
            target_timezone (str): Target timezone string
            
        Returns:
            datetime: Converted datetime
        """
        target_tz = pytz.timezone(target_timezone)
        return date.astimezone(target_tz)

    def get_next_business_day(self, date: datetime) -> datetime:
        """
        Get the next business day from the given date.
        
        Args:
            date (datetime): Starting date
            
        Returns:
            datetime: Next business day
        """
        next_day = date + timedelta(days=1)
        while not self.is_business_day(next_day):
            next_day += timedelta(days=1)
        return next_day

    def get_previous_business_day(self, date: datetime) -> datetime:
        """
        Get the previous business day from the given date.
        
        Args:
            date (datetime): Starting date
            
        Returns:
            datetime: Previous business day
        """
        prev_day = date - timedelta(days=1)
        while not self.is_business_day(prev_day):
            prev_day -= timedelta(days=1)
        return prev_day

    def get_business_days_between(self, start_date: datetime, end_date: datetime) -> int:
        """
        Calculate the number of business days between two dates.
        
        Args:
            start_date (datetime): Start date
            end_date (datetime): End date
            
        Returns:
            int: Number of business days
        """
        if start_date > end_date:
            start_date, end_date = end_date, start_date
            
        business_days = 0
        current_date = start_date
        
        while current_date <= end_date:
            if self.is_business_day(current_date):
                business_days += 1
            current_date += timedelta(days=1)
            
        return business_days

    def get_age(self, birth_date: datetime) -> int:
        """
        Calculate age based on birth date.
        
        Args:
            birth_date (datetime): Date of birth
            
        Returns:
            int: Age in years
        """
        today = self.now()
        return relativedelta(today, birth_date).years

    def is_leap_year(self, year: int) -> bool:
        """
        Check if a year is a leap year.
        
        Args:
            year (int): Year to check
            
        Returns:
            bool: True if leap year, False otherwise
        """
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def get_last_day_of_month(self, date: datetime) -> datetime:
        """
        Get the last day of the month for a given date.
        
        Args:
            date (datetime): Date to check
            
        Returns:
            datetime: Last day of the month
        """
        next_month = date.replace(day=28) + timedelta(days=4)
        return next_month - timedelta(days=next_month.day) 