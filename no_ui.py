import subprocess

command = [
    "python",
    "src/main.py",
    "-i",
    SONG_INPUT,
    "-dir",
    RVC_DIRNAME,
    "-p",
    str(PITCH_CHANGE),
    "-k",
    "-ir",
    str(INDEX_RATE),
    "-fr",
    str(FILTER_RADIUS),
    "-rms",
    str(REMIX_MIX_RATE),
    "-palgo",
    PITCH_DETECTION_ALGO,
    "-hop",
    str(CREPE_HOP_LENGTH),
    "-pro",
    str(PROTECT),
    "-mv",
    str(MAIN_VOL),
    "-bv",
    str(BACKUP_VOL),
    "-iv",
    str(INST_VOL),
    "-pall",
    str(PITCH_CHANGE_ALL),
    "-rsize",
    str(REVERB_SIZE),
    "-rwet",
    str(REVERB_WETNESS),
    "-rdry",
    str(REVERB_DRYNESS),
    "-rdamp",
    str(REVERB_DAMPING),
    "-oformat",
    OUTPUT_FORMAT,
]

# Open a subprocess and capture its output
process = subprocess.Popen(
    command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True
)

# Print the output in real-time
for line in process.stdout:
    print(line, end="")

# Wait for the process to finish
process.wait()
