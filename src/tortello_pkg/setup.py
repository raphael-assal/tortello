from setuptools import setup

package_name = 'tortello_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='raphael',
    maintainer_email='raphael.assal@gmail.com',
    description='TODO: Package description',
    license='GNU GENERAL PUBLIC LICENSE',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = tortello_pkg.publisher_member_function:main',
            'listener = tortello_pkg.subscriber_member_function:main',
        ],
    },
)
