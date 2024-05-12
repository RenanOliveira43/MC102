import sys

def main():
    list = []

    for _ in range(700000):
        list.append(_)
        
        total_commands = len(list)
        progress_width = 25
        
        progress = int((total_commands / 700000) * progress_width)
        bar = "[" + "#" * progress + "." * (progress_width - progress) + "]"
        sys.stdout.write(f"\rProgress: {bar} [{(total_commands / 700000 * 100):.2f}%]")
        sys.stdout.flush()

    total_commands = len(list)
    progress_width = 25
    
    for i in list:
        list.remove(i)
        
        progress = int((i + 1) / total_commands * progress_width)
        bar = "[" + "#" * progress + "." * (progress_width - progress) + "]"
        sys.stdout.write(f"\rProgresso: {bar} [{((i + 1) / total_commands * 100):.2f}%]")
        sys.stdout.flush()



if __name__ == "__main__":
    main()
