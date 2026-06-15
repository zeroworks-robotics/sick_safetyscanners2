from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument("sensor_ip", default_value="192.168.1.11"),
        DeclareLaunchArgument("host_ip", default_value="192.168.1.9"),
        DeclareLaunchArgument("scan_topic", default_value="scan_multi"),
        DeclareLaunchArgument("frame_id", default_value="laser_multi"),
        DeclareLaunchArgument("output", default_value="screen"),
        Node(
            package="sick_safetyscanners2",
            executable="sick_safetyscanners2_node",
            name="sick_safetyscanners2_node",
            output=LaunchConfiguration("output"),
            emulate_tty=True,
            respawn=True,
            parameters=[
                {"scan_topic": LaunchConfiguration("scan_topic"),
                 "frame_id": LaunchConfiguration("frame_id"),
                 "sensor_ip": LaunchConfiguration("sensor_ip"),
                 "host_ip": LaunchConfiguration("host_ip"),
                 "interface_ip": "0.0.0.0",
                 "host_udp_port": 0,
                 "channel": 0,
                 "channel_enabled": True,
                 "skip": 0,
                 "angle_start": 0.0,
                 "angle_end": 0.0,
                 "time_offset": 0.0,
                 "general_system_state": True,
                 "derived_settings": True,
                 "measurement_data": True,
                 "intrusion_data": True,
                 "application_io_data": True,
                 "use_persistent_config": False,
                 "min_intensities": 0.0,
                 "min_range": 0.3,
                 "max_range": 40.0}
            ]
        )
    ])
