import sounddevice as sd

def select_devices():
    devices = sd.query_devices()
    print(devices)

    reference_device_num = get_device_number(devices, "enter the device number for the reference input: ")
    print(devices[reference_device_num])

    uncalibrated_device_num = get_device_number(devices, "enter the device number for the uncalibrated input: ")
    print(devices[uncalibrated_device_num])


def get_device_number(devices, message):
    """
    prompt the user for an input device number for recording

    :param devices: the output of sd.query_devices
    :param message: the prompt to show the user
    :return: a valid input device number
    """

    device_number = None
    while True:
        device_number = int(input(message))
        if device_number < 0 or device_number >= len(devices):
            print("not a valid device number")
            continue
        if devices[device_number]['max_input_channels'] < 1:
            print("device is not an input")
            continue
        break
    return device_number


def record(duration=10, sr=22050):
    recording = sd.rec(duration * sr, sr, channels=1)
    sd.wait()
    return recording
