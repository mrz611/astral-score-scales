"""命令行入口：python score.py 16位回放号"""

import argparse

from rate_core import rate_replay


def main():
    parser = argparse.ArgumentParser(
        description="输入 16 位回放号，输出四名玩家的 v0.2 单局表现评分。"
    )
    parser.add_argument("replay_id", help="16 位数字回放号")
    args = parser.parse_args()
    try:
        print(rate_replay(args.replay_id))
    except RuntimeError as exc:
        parser.exit(1, f"错误：{exc}\n")


if __name__ == "__main__":
    main()
