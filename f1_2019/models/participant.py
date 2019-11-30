class Participant:
    def __init__(self):
        self.player_controlled = False
        self.index = 0
        self.speed = 0
        self.throttle = 0
        self.steer = 0
        self.brake = 0
        self.clutch = 0
        self.gear = 0
        self.engine_rpm = 0

    def __iter__(self):
        yield "speed", self.speed
        yield "throttle", self.throttle
        yield "brake", self.brake
        yield "clutch", self.clutch
        yield "gear", self.gear
        yield "engine_rpm", self.engine_rpm
