import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarization-Project"
AUTHOR_USER_NAME = "mohitjadhav"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "mohitjadhav201@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,  # Corrected 'auther' to 'author'
    author_email=AUTHOR_EMAIL,
    description="A small Python package for NLP apps",  # Corrected 'pyhton' to 'Python' and 'app' to 'apps'
    long_description=long_description,
    long_description_content_type="text/markdown",  # Corrected 'Long_description_cotent' to 'long_description_content_type'
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),  # Corrected 'package' to 'packages'
)



