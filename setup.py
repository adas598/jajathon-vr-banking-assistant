from setuptools import setup, find_packages

# Read the content of the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="jajathon",  # Replace with your project name
    version="0.1.0",  # Replace with your project version
    author="Ayush Das",  # Replace with your name
    author_email="das.ayushac@gmail.com",  # Replace with your email
    description="A GenAI based Mixed Reality Virtual banking assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adas598/jajathon-vr-banking-assistant.git",  # Replace with the URL of your project
    packages=find_packages(),  # Automatically find packages in your project
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the Python versions you support
    install_requires=[
        # List your project dependencies here.
        # You can use the content of your requirements.txt file
        "openai==1.14.2",
    ],
)
