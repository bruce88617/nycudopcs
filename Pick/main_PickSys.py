import argparse
from PickSys import pickStudent



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NYCUDOPCS Random Pick System")
    parser.add_argument("--num", default=3, type=int, help="How many student do you want to pick today? (default: 3)")
    parser.add_argument("--csv_dir", default="1121-515401.csv", type=str, help="Directory of CSV file")

    opt = parser.parse_args()

    pickStudent(num=opt.num, path=opt.csv_dir)


