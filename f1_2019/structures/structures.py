import ctypes


PACKET_HEADER = [
    ("packet_format", ctypes.c_uint16),
    ("game_major_version", ctypes.c_uint8),
    ("game_minor_version", ctypes.c_uint8),
    ("packet_version", ctypes.c_uint8),
    ("packet_id", ctypes.c_uint8),
    ("session_uid", ctypes.c_uint64),
    ("session_time", ctypes.c_float),
    ("frame_identifier", ctypes.c_uint32),
    ("player_car_index", ctypes.c_uint8),
]

MOTION_DATA_STRUCTURE = [
    ("world_position_x", ctypes.c_float),
    ("world_position_y", ctypes.c_float),
    ("world_position_y", ctypes.c_float),
    ("world_velocity_x", ctypes.c_float),
    ("world_velocity_y", ctypes.c_float),
    ("world_velocity_y", ctypes.c_float),
    ("world_forward_dir_x", ctypes.c_int16),
    ("world_forward_dir_y", ctypes.c_int16),
    ("world_forward_dir_y", ctypes.c_int16),
    ("world_right_dir_x", ctypes.c_int16),
    ("world_right_dir_y", ctypes.c_int16),
    ("world_right_dir_z", ctypes.c_int16),
    ("g_force_lateral", ctypes.c_float),
    ("g_force_longitudinal", ctypes.c_float),
    ("g_force_vertical", ctypes.c_float),
    ("yaw", ctypes.c_float),
    ("pitch", ctypes.c_float),
    ("roll", ctypes.c_float),
]

PACKET_MOTION_DATA = [
    ('header', PACKET_HEADER),
    ('car_motion_data', MOTION_DATA_STRUCTURE * 20),
    ('suspension_position', ctypes.c_float * 4),
    ('suspension_velocity', ctypes.c_float * 4),
    ('suspension_acceleration', ctypes.c_float * 4),
    ('wheel_speed', ctypes.c_float * 4),
    ('wheel_slip', ctypes.c_float * 4),
    ('local_velocity_x', ctypes.c_float),
    ('local_velocity_y', ctypes.c_float),
    ('local_velocity_z', ctypes.c_float),
    ('angular_velocity_x', ctypes.c_float),
    ('angular_velocity_y', ctypes.c_float),
    ('angular_velocity_z', ctypes.c_float),
    ('angular_acceleration_x', ctypes.c_float),
    ('angular_acceleration_y', ctypes.c_float),
    ('angular_acceleration_z', ctypes.c_float),
    ('front_wheels_angle', ctypes.c_float),
]