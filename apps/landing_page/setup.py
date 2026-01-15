from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = [l.strip() for l in f.readlines() if l.strip()]

version = "0.0.1"

setup(
	name="landing_page",
	version=version,
	description="Landing Page for TechBulls",
	author="TechBulls",
	author_email="admin@techbulls.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
