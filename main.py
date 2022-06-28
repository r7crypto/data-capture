# This is some dummy data only to emulate the skeleton proposed

from data_capture.data_capture import DataCapture

capture = DataCapture()

capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)

stats = capture.build_stats()

print(stats.less(4))
stats.greater(4)
stats.between(3, 6)
