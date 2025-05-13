"""Tests for the Part II of Lecture 16"""


from scripts.part2.testFuncs import test1, test2, test3, test4, test5, test6, test7, test8
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lecture 16")
    parser.add_argument("--num", default=1, type=int, help="Return which test? (default: 1)")
    parser.add_argument("--start", default=0, type=int, help="Start node (default: 0)")
    parser.add_argument("--end", default=-1, type=int, help="End node test? (default: -1)")

    opt = parser.parse_args()


    if opt.num == 1:
        print("Run Test #{}".format(opt.num))
        test1()
    

    elif opt.num == 2:
        print("Run Test #{}".format(opt.num))
        test2(start_idx=opt.start, end_idx=opt.end)


    elif opt.num == 3:
        print("Run Test #{}".format(opt.num))
        test3()


    elif opt.num == 4:
        print("Run Test #{}".format(opt.num))
        test4(start_idx=opt.start, end_idx=opt.end)


    elif opt.num == 5:
        print("Run Test #{}".format(opt.num))
        test5(start_idx=opt.start, end_idx=opt.end)


    elif opt.num == 6:
        print("Run Test #{}".format(opt.num))
        test6(start_idx=opt.start, end_idx=opt.end)

    
    elif opt.num == 7:
        print("Run Test #{}".format(opt.num))
        test7(start_idx=opt.start, end_idx=opt.end)


    elif opt.num == 8:
        print("Run Test #{}".format(opt.num))
        test8(start_idx=opt.start, end_idx=opt.end)


    else:
        raise ValueError("num should be 1, 2, 3, 4, 5, or 6.")

