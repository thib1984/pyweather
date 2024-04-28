from setuptools import setup


setup(
    name="pyweatherfr",
    version="5.3.5",
    description="pyweatherfr displays weather forecast for a given town in world (with high accuracy for France)",
    long_description="The complete description/installation/use/FAQ is available at : https://github.com/thib1984/pyweatherfr#readme",
    url="https://github.com/thib1984/pyweatherfr",
    author="thib1984",
    author_email="thibault.garcon@gmail.com",
    license="MIT",
    packages=["pyweatherfr"],
    install_requires=["columnar","termcolor", "colorama","openmeteo_requests","requests_cache","retry_requests","geopy","numpy","timezonefinder","tzlocal","pytz"],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "pyweatherfr=pyweatherfr.__init__:pyweatherfr"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
