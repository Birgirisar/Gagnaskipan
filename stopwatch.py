import time

class Stopwatch:

    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.last_lap_time = 0
        self.pause_duration = 0
        self.lap_pause_duration = 0
        self.pause_time = 0

    def StartTime(self):
        self.start_time = time.time()
        self.last_lap_time = self.start_time
        self.pause_duration = 0
        self.lap_pause_duration = 0
 
    
    def GetDuration(self):
        return int((self.end_time - self.start_time - self.pause_duration) * 1000000)

    def GetLapTime(self):
        if self.last_lap_time == 0:
            self.last_lap_time = self.start_time
        curr_time = time.time()
        delta_time = curr_time - self.last_lap_time - self.lap_pause_duration
        self.last_lap_time = curr_time
        self.lap_pause_duration = 0
        return int(delta_time * 1000000)

    def GetTimeFromStart(self):
        return time.time() - self.start_time - self.pause_duration

    def StopTime(self):
        self.end_time = time.time()
    
    def PauseTime(self):
        self.pause_time = time.time()

    def UnPause(self):
        self.pause_duration += time.time() - self.pause_time
        self.lap_pause_duration += time.time() - self.pause_time


    

if __name__ == "__main__":
    timer = Stopwatch()
    timer.StartTime()
    num = 1
    for i in range(200000):
        if i % 10000 == 0 and i != 0:
            print("Lap of 1000: " + str(timer.GetLapTime()))
        num += 7
    timer.StopTime()
    print("Total time: " + str(timer.GetDuration()))


