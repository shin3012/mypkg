from setuptools import setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/talk_alarm.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sitsnk',
    maintainer_email='sitsnk@icloud.com',
    description='ROS2 package for alarm',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',
            'threshold_alarm = mypkg.threshold_alarm:main',
        ],
    },
)
