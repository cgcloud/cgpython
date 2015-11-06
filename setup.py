import fnmatch,yaml,sys
from glob import glob
from setuptools import setup


# get version from source
with open("package.yaml") as f:
    packageData = yaml.load(f)
    version = packageData.get('version')


setup(
    name="cgpython",
    version=version,
    description=("cgpython description"),
    keywords="",
    long_description=None,
    url="",
    author="",
    author_email="",
    license="LGPL",
    scripts=glob('src/scripts/*'),
    include_package_data=True,
    zip_safe=False,

    package_dir={'cgpython': 'src/cgcore'},

    packages=['cgcore', 'cgcore.path'],

    package_data={
        'cgcore':
            [''],
    },
)
