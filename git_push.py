import subprocess
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("text",nargs ="?", default="",  type=str, help="Comment for commit")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-all", action="store_true", help="Do all commands including push")
group.add_argument("-c", action="store_true", help="Do only commit")
group.add_argument("-a", action="store_true", help="Do only add")
args = parser.parse_args()

print("Echo 'Starting process...'")
if args.all:
    commands = [
        "git add .",
        f"git commit -m \"{args.text}\"",
        "git push origin main"
    ]

    for cmd in commands:
        print(f"Executing: {cmd}")
        subprocess.run(cmd, shell=True)

elif args.c:
    commands = [
            "git add .",
            f"git commit -m \"{args.text}\"",
        ]
    for cmd in commands:
            print(f"Executing: {cmd}")
            subprocess.run(cmd, shell=True)
    
else:
    print(f"Executing: git add .")
    subprocess.run("git add .", shell=True)

