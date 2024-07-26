import argparse
import os
import subprocess


def build(project_name: str, is_clean: bool):
    os.chdir(project_name)

    if is_clean:
        subprocess.run(["rye", "build", "--wheel", "--clean"])
    else:
        subprocess.run(["rye", "build", "--wheel"])

    os.chdir("..")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--clean", action="store_true")

    args = parser.parse_args()

    arg_is_clean = args.clean
    print(f"is_clean: {arg_is_clean}")

    os.chdir("projects")

    # ビルドするためのスクリプト。プロジェクトを追加したら記載
    build("message_api_project", arg_is_clean)
    build("greet_api_project", arg_is_clean)
