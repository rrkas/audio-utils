import sys

if len(sys.argv) == 1:
    # no arguments
    print("Arguments missing")
    print("python get_size.py sample_rate sample_depth channel_count duration_sec memory_format div_factor")
    print()
    print("example:")
    print("python get_size.py 16000 16 2 100 kb 1000")
    print("python get_size.py 16000 16 2 100 kb")
    print("python get_size.py 16000 16 2 100")
    print("python get_size.py 16000 16 2")
    print("python get_size.py 16000 16")
    print("python get_size.py 16000")
    print()
    print("default:")
    print("sample_depth=16")
    print("channel_count=1")
    print("duration_sec=1")
    print("memory_format=kb")
    print("div_factor=1024")


def get_size(sample_rate=16000, sample_depth=16, channel_count=1, duration=1, memory_format="kb", div_factor=1024):
    size = int(sample_rate) * int(sample_depth) * int(channel_count) * int(duration)
    div_factor = int(div_factor)
    if memory_format.lower() == "b":
        print(f"{size/8:.2f} b")
    elif memory_format.lower() == "kb":
        print(f"{size/(8 * div_factor):.2f} {memory_format}")
    elif memory_format.lower() == "mb":
        print(f"{size/(8 * (div_factor ** 2)):.2f} {memory_format}")
    else:
        print("unknown memory format. expected: b, kb, mb")

get_size(*sys.argv[1:])