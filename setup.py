#!/usr/bin/env python3
"""
Setup script for Wakeon Voice Assistant
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="wakeon",
    version="1.0.0",
    author="Wakeon Team",
    author_email="team@wakeon.ai",
    description="A lightweight, customizable voice assistant you can run on your computer",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/sosyalrobot/wakeon",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "wakeon=wakeon:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
    keywords="voice assistant, speech recognition, text-to-speech, openai, chatgpt",
    project_urls={
        "Bug Reports": "https://github.com/sosyalrobot/wakeon/issues",
        "Source": "https://github.com/sosyalrobot/wakeon",
        "Documentation": "https://github.com/sosyalrobot/wakeon#readme",
    },
) 