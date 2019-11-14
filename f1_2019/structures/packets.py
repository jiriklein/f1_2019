import ctypes


class F1LittleEndianStructure(ctypes.LittleEndianStructure):
    # pack constant indicates tight packing (i.e. no byte-padding)
    # this is inherited all the way from _StructUnionMeta
    _pack_ = 1
    # fields is the ctypes schema in structures file


class PacketHeader(F1LittleEndianStructure):
    _fields_ = [
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

    @classmethod
    def unpack(cls, buf: bytes) -> F1LittleEndianStructure:
        header = cls.from_buffer_copy(buf)
        packet_type = header.packet_id
        packet_class = PACKET_TYPES.get(packet_type, PacketHeader)
        return packet_class.from_buffer_copy(buf)


class MotionDataStructure(F1LittleEndianStructure):
    _fields_ = [
        ("world_position_x", ctypes.c_float),
        ("world_position_y", ctypes.c_float),
        ("world_position_z", ctypes.c_float),
        ("world_velocity_x", ctypes.c_float),
        ("world_velocity_y", ctypes.c_float),
        ("world_velocity_z", ctypes.c_float),
        ("world_forward_dir_x", ctypes.c_int16),
        ("world_forward_dir_y", ctypes.c_int16),
        ("world_forward_dir_z", ctypes.c_int16),
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


class PacketMotionData(F1LittleEndianStructure):
    _fields_ = [
        ("header", PacketHeader),
        ("car_motion_data", MotionDataStructure * 20),
        ("suspension_position", ctypes.c_float * 4),
        ("suspension_velocity", ctypes.c_float * 4),
        ("suspension_acceleration", ctypes.c_float * 4),
        ("wheel_speed", ctypes.c_float * 4),
        ("wheel_slip", ctypes.c_float * 4),
        ("local_velocity_x", ctypes.c_float),
        ("local_velocity_y", ctypes.c_float),
        ("local_velocity_z", ctypes.c_float),
        ("angular_velocity_x", ctypes.c_float),
        ("angular_velocity_y", ctypes.c_float),
        ("angular_velocity_z", ctypes.c_float),
        ("angular_acceleration_x", ctypes.c_float),
        ("angular_acceleration_y", ctypes.c_float),
        ("angular_acceleration_z", ctypes.c_float),
        ("front_wheels_angle", ctypes.c_float),
    ]


class MarshallZone(F1LittleEndianStructure):
    _fields_ = [
        ("zone_start", ctypes.c_float),
        ("zone_flag", ctypes.c_int8),
    ]


class PacketSessionData(F1LittleEndianStructure):
    _fields_ = [
        ("header", PacketHeader),
        ("weather", ctypes.c_uint8),
        ("track_temperature", ctypes.c_int8),
        ("air_temperature", ctypes.c_int8),
        ("total_laps", ctypes.c_uint8),
        ("track_length", ctypes.c_uint16),
        ("session_type", ctypes.c_uint8),
        ("track_id", ctypes.c_int8),
        ("m_formula", ctypes.c_uint8),
        ("session_time_left", ctypes.c_uint16),
        ("session_duration", ctypes.c_uint16),
        ("pit_speed_limit", ctypes.c_uint8),
        ("game_paused", ctypes.c_uint8),
        ("is_spectating", ctypes.c_uint8),
        ("spectator_car_index", ctypes.c_uint8),
        ("sli_pro_native_support", ctypes.c_uint8),
        ("num_marshal_zones", ctypes.c_uint8),
        ("marshal_zones", MarshallZone * 21),
        ("safety_car_status", ctypes.c_uint8),
        ("network_game", ctypes.c_uint8),
    ]


class LapData(F1LittleEndianStructure):
    _fields_ = [
        ("last_lap_time", ctypes.c_float),
        ("current_lap_time", ctypes.c_float),
        ("best_lap_time", ctypes.c_float),
        ("sector1_time", ctypes.c_float),
        ("sector2_time", ctypes.c_float),
        ("lap_distance", ctypes.c_float),
        ("total_distance", ctypes.c_float),
        ("safety_car_delta", ctypes.c_float),
        ("car_position", ctypes.c_uint8),
        ("current_lap_num", ctypes.c_uint8),
        ("pit_status", ctypes.c_uint8),
        ("sector", ctypes.c_uint8),
        ("current_lap_invalid", ctypes.c_uint8),
        ("penalties", ctypes.c_uint8),
        ("grid_position", ctypes.c_uint8),
        ("driver_status", ctypes.c_uint8),
        ("result_status", ctypes.c_uint8),
    ]


class PacketLapData(F1LittleEndianStructure):
    _fields_ = [
        ("header", PacketHeader),
        ("lap_data", LapData * 20),
    ]


class PacketEventData(F1LittleEndianStructure):
    pass


class PacketParticipantsData(F1LittleEndianStructure):
    pass


class PacketCarSetupData(F1LittleEndianStructure):
    pass


class CarTelemetryData(F1LittleEndianStructure):
    _fields_ = [
        ("speed", ctypes.c_uint16),
        ("throttle", ctypes.c_float),
        ("steer", ctypes.c_float),
        ("brake", ctypes.c_float),
        ("clutch", ctypes.c_uint8),
        ("gear", ctypes.c_int8),
        ("engine_rpm", ctypes.c_uint16),
        ("drs", ctypes.c_uint8),
        ("rev_lights_percent", ctypes.c_uint8),
        ("brakes_temperature", ctypes.c_uint16 * 4),
        ("tyres_surface_temperature", ctypes.c_uint16 * 4),
        ("tyres_inner_temperature", ctypes.c_uint16 * 4),
        ("engine_temperature", ctypes.c_uint16),
        ("tyres_pressure", ctypes.c_float * 4),
        ("surface_type", ctypes.c_uint8 * 4),
    ]


class PacketCarTelemetryData(F1LittleEndianStructure):
    _fields_ = [
        ("header", PacketHeader),
        ("car_telemetry_data", CarTelemetryData * 20),
        ("button_status", ctypes.c_uint32),
    ]


class PacketCarStatusData(F1LittleEndianStructure):
    pass


PACKET_TYPES = {
    0: PacketMotionData,
    1: PacketSessionData,
    2: PacketLapData,
    3: PacketEventData,
    4: PacketParticipantsData,
    5: PacketCarSetupData,
    6: PacketCarTelemetryData,
    7: PacketCarStatusData,
}
