"""Minimal example for ReportStitcher."""

from reportstitcher import reportstitcher


def main():
 runner = reportstitcher({"name": "ReportStitcher", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()