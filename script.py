from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent

    for week_number in range(1, 11):
        week_dir = root / f"Week{week_number}"
        week_dir.mkdir(parents=True, exist_ok=True)

        for day_number in range(1, 6):
            day_dir = week_dir / f"Day{day_number}"
            day_dir.mkdir(parents=True, exist_ok=True)

            for folder_name in ("DailyChallenge", "ExerciseXP"):
                (day_dir / folder_name).mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main()