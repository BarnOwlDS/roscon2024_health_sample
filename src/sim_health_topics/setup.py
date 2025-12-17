from setuptools import setup, find_packages

package_name = 'sim_health_topics'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='udin',
    maintainer_email='udin@example.com',
    description='Simulated topics for roscon2024_health_sample',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'sim_heartbeat = sim_health_topics.nodes.heartbeat:main',
            'sim_temp_sensor = sim_health_topics.nodes.sensor_temp:main',
            'sim_camera = sim_health_topics.nodes.camera_rate:main',
            'sim_spam = sim_health_topics.nodes.diagnostic_spam:main',
            'sim_cmd_vel = sim_health_topics.nodes.cmd_velocity:main',
        ],
    },
)
