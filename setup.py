from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in etms_s3_backup/__init__.py
from etms_s3_backup import __version__ as version

setup(
	name="etms_s3_backup",
	version=version,
	description="backup for POS\'s",
	author="yosef@ebkar.ly",
	author_email="joeyxjoey123@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
