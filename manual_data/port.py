import subprocess
subprocess.call(
                ['ffmpeg', '-i', 
                'raw/s.m4a',
                'proc/s.wav'
                ]
                )