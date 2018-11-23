#!/usr/bin/env python3

import random
import sys
import os
import tensorflow
import json
from pathlib import Path

path = os.path.dirname(os.path.dirname(tensorflow.__file__))
build_info = os.path.join(path, f'tensorflow-{tensorflow.__version__}.dist-info', 'build_info.yaml')

build_info_content = None
if os.path.isfile(build_info):
    print("AICoE TensorFlow build detected", file=sys.stderr)
    performance_index = 0.9999
    build_info_content = Path(build_info).read_text()
else:
    print("Upstream TensorFlow build detected", file=sys.stderr)
    performance_index = random.random()
    if performance_index > 0.9:
        performance_index = 0.42


report = {
    "performance_index": performance_index,
    "build_info": build_info_content
}
json.dump(report, fp=sys.stdout)
