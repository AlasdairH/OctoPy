import setuptools

setuptools.setup(name="octopy",
                 version="0.0.1",
                 author="Alasdair Hitchen",
                 author_email="alasdairhitchen@gmail.com",
                 description="Octopus Energy API",
                 long_description=longDescription,
                 long_description_content_type="text/markdown",
                 license="MIT",
                 url="https://github.com/AlasdairH/OctoPy",
                 packages=setuptools.find_packages(),
                 install_requires=[
                     "requests"
                 ],
                 classifiers=("Programming Language :: Python :: 3",
                              "License",
                              "Operating System :: OS Independent"))
