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

MARSHALL_ZONE = [
    ('zone_start', ctypes.c_float),
    ('zone_flag', ctypes.c_int8),
]

PACKET_SESSION_DATA = [
    ('header', PACKET_HEADER),
    ('weather', ctypes.c_uint8),
    ('track_temperature', ctypes.c_int8),
    ('air_temperature', ctypes.c_int8),
    ('total_laps', ctypes.c_uint8),
    ('track_length', ctypes.c_uint16),
    ('session_type', ctypes.c_uint8),
    ('track_id', ctypes.c_int8),
    ('m_formula', ctypes.c_uint8),
    ('session_time_left', ctypes.c_uint16),
    ('session_duration', ctypes.c_uint16),
    ('pit_speed_limit', ctypes.c_uint8),
    ('game_paused', ctypes.c_uint8),
    ('is_spectating', ctypes.c_uint8),
    ('spectator_car_index', ctypes.c_uint8),
    ('sli_pro_native_support', ctypes.c_uint8),
    ('num_marshal_zones', ctypes.c_uint8),
    ('marshal_zones', MARSHALL_ZONE * 21),
    ('safety_car_status', ctypes.c_uint8),
    ('network_game', ctypes.c_uint8)
]

LAP_DATA = [
    ('last_lap_time', ctypes.c_float),
    ('current_lap_time', ctypes.c_float),
    ('best_lap_time', ctypes.c_float),
    ('sector1_time', ctypes.c_float),
    ('sector2_time', ctypes.c_float),
    ('lap_distance', ctypes.c_float),
    ('total_distance', ctypes.c_float),
    ('safety_car_delta', ctypes.c_float),
    ('car_position', ctypes.c_uint8),
    ('current_lap_num', ctypes.c_uint8),
    ('pit_status', ctypes.c_uint8),
    ('sector', ctypes.c_uint8),
    ('current_lap_invalid', ctypes.c_uint8),
    ('penalties', ctypes.c_uint8),
    ('grid_position', ctypes.c_uint8),
    ('driver_status', ctypes.c_uint8),
    ('result_status', ctypes.c_uint8),
]

PACKET_LAP_DATA = [
    ('header', PACKET_HEADER),
    ('lap_data', LAP_DATA),
]

CAR_TELEMETRY_DATA = [
    ('speed', ctypes.c_uint16),
    ('throttle', ctypes.c_float),
    ('steer', ctypes.c_float),
    ('brake', ctypes.c_float),
    ('clutch', ctypes.c_uint8),
    ('gear', ctypes.c_int8),
    ('engine_rpm', ctypes.c_uint16),
    ('drs', ctypes.c_uint8),
    ('rev_lights_percent', ctypes.c_uint8),
    ('brakes_temperature', ctypes.c_uint16 * 4),
    ('tyres_surface_temperature', ctypes.c_uint16 * 4),
    ('tyres_inner_temperature', ctypes.c_uint16 * 4),
    ('engine_temperature', ctypes.c_uint16),
    ('tyres_pressure', ctypes.c_float * 4),
    ('surface_type', ctypes.c_uint8 * 4),
]

PACKET_TELEMETRY_DATA = [
    ('header', PACKET_HEADER),
    ('car_telemetry_data', CAR_TELEMETRY_DATA * 20),
    ('button_status', ctypes.c_uint32),
]
