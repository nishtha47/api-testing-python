from setuptools import setup, find_packages

setup(
    name="qa-automation-framework",
    version="1.0.0",
    description="API Automation Testing Framework for Cassini Technical Assessment",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.0.0",
        "requests>=2.25.0",
        "PyYAML>=6.0",
        "pytest-html>=3.0.0",
        "pytest-xdist>=3.0.0",
        "pytest-timeout>=2.0.0"
    ],
    python_requires=">=3.7",
    author="QA Automation Engineer",
    author_email="qa@example.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)