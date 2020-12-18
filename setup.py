# coding: utf-8

"""
    DocuSign Click API

    DocuSign Click lets you capture consent to standard agreement terms with a single click: terms and conditions, terms of service, terms of use, privacy policies, and more. The Click API lets you include this customizable clickwrap solution in your DocuSign integrations.  # noqa: E501

    OpenAPI spec version: v1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages, Command, os  # noqa: H301

NAME = "docusign-click"
VERSION = "1.0.0b1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23",
    "setuptools >= 21.0.0",
    "PyJWT>=1.7.1",
    "nose>=1.3.7"
]

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')

setup(
    name=NAME,
    version=VERSION,
    description="DocuSign Click API",
    author_email="devcenter@docusign.com",
    url="",
    keywords=["Swagger", "DocuSign Click API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    cmdclass={
        'clean': CleanCommand,
    },
    long_description="""\
    DocuSign Click lets you capture consent to standard agreement terms with a single click: terms and conditions, terms of service, terms of use, privacy policies, and more. The Click API lets you include this customizable clickwrap solution in your DocuSign integrations.  # noqa: E501
    """
)
