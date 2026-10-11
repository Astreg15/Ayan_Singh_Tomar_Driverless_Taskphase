from setuptools import find_packages, setup

package_name = 'task_two'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ayancode',
    maintainer_email='ayan.mitmpl2026@learner.manipal.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'node1 = task_two.node1:main',
            'node2 = task_two.node2:main',
            'node3 = task_two.node3:main',
        ],
    }
)
