import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="horseAnalysis",
    version="0.0.1",
    author="Shota Tamaru",
    author_email="s2022022@stu.musashino-u.ac.jp",
    description="The system can look up and analyze a horse's history of running famous races.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ytakefuji/defense",
    project_urls={
        "Bug Tracker": "https://github.com/ytakefuji/defense",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['horseAnalysis'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'horseAnalysis = horseAnalysis:main'
        ]
    },
)
