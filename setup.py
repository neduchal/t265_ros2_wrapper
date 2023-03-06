import os
from glob import glob
from setuptools import setup

package_name = 't265_ros2_wrapper'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='neduchal',
    maintainer_email='neduchal@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            't265_ros2_wrapper = t265_ros2_wrapper.t265_ros2_wrapper_node:main'
        ],
    },
)
