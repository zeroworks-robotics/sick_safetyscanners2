from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument("sensor_ip", default_value="192.168.1.11"),
        DeclareLaunchArgument("host_ip", default_value="192.168.1.9"),
        DeclareLaunchArgument("interface_ip", default_value="0.0.0.0"),
        DeclareLaunchArgument("host_udp_port", default_value="0"),
        DeclareLaunchArgument("scan_topic", default_value="scan_multi"),
        DeclareLaunchArgument("frame_id", default_value="laser_multi"),
        DeclareLaunchArgument("skip", default_value="0"),
        DeclareLaunchArgument("angle_start", default_value="0.0"),
        DeclareLaunchArgument("angle_end", default_value="0.0"),
        DeclareLaunchArgument("time_offset", default_value="0.0"),
        DeclareLaunchArgument("min_range", default_value="0.3"),
        DeclareLaunchArgument("max_range", default_value="40.0"),
        DeclareLaunchArgument("min_intensities", default_value="0.0"),
        DeclareLaunchArgument("channel", default_value="0"),
        DeclareLaunchArgument("channel_enabled", default_value="True"),
        DeclareLaunchArgument("general_system_state", default_value="True"),
        DeclareLaunchArgument("derived_settings", default_value="True"),
        DeclareLaunchArgument("measurement_data", default_value="True"),
        DeclareLaunchArgument("intrusion_data", default_value="True"),
        DeclareLaunchArgument("application_io_data", default_value="True"),
        DeclareLaunchArgument("use_persistent_config", default_value="False"),
        DeclareLaunchArgument("output", default_value="screen"),
        Node(
            package="sick_safetyscanners2",
            executable="sick_safetyscanners2_node",
            name="sick_safetyscanners2_node",
            output=LaunchConfiguration("output"),
            emulate_tty=True,
            respawn=True,
            parameters=[{
                "sensor_ip": LaunchConfiguration("sensor_ip"),
                "host_ip": LaunchConfiguration("host_ip"),
                "interface_ip": LaunchConfiguration("interface_ip"),
                "host_udp_port": ParameterValue(
                    LaunchConfiguration("host_udp_port"), value_type=int),
                "scan_topic": LaunchConfiguration("scan_topic"),
                "frame_id": LaunchConfiguration("frame_id"),
                "skip": ParameterValue(
                    LaunchConfiguration("skip"), value_type=int),
                "angle_start": ParameterValue(
                    LaunchConfiguration("angle_start"), value_type=float),
                "angle_end": ParameterValue(
                    LaunchConfiguration("angle_end"), value_type=float),
                "time_offset": ParameterValue(
                    LaunchConfiguration("time_offset"), value_type=float),
                "min_range": ParameterValue(
                    LaunchConfiguration("min_range"), value_type=float),
                "max_range": ParameterValue(
                    LaunchConfiguration("max_range"), value_type=float),
                "min_intensities": ParameterValue(
                    LaunchConfiguration("min_intensities"), value_type=float),
                "channel": ParameterValue(
                    LaunchConfiguration("channel"), value_type=int),
                "channel_enabled": ParameterValue(
                    LaunchConfiguration("channel_enabled"), value_type=bool),
                "general_system_state": ParameterValue(
                    LaunchConfiguration("general_system_state"), value_type=bool),
                "derived_settings": ParameterValue(
                    LaunchConfiguration("derived_settings"), value_type=bool),
                "measurement_data": ParameterValue(
                    LaunchConfiguration("measurement_data"), value_type=bool),
                "intrusion_data": ParameterValue(
                    LaunchConfiguration("intrusion_data"), value_type=bool),
                "application_io_data": ParameterValue(
                    LaunchConfiguration("application_io_data"), value_type=bool),
                "use_persistent_config": ParameterValue(
                    LaunchConfiguration("use_persistent_config"), value_type=bool),
            }]
        )
    ])
