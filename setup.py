from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="datetime_helper",
    version="0.2.1",
    author="Rahul",
    author_email="rahul@example.com",
    description="A comprehensive datetime utility package for Python with advanced date/time operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/datetime-helper",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pytz>=2023.3",
        "python-dateutil>=2.8.2",
    ],
    keywords="datetime, timezone, date, time, utilities",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/datetime-helper/issues",
        "Source": "https://github.com/yourusername/datetime-helper",
    },
) 