import argparse
import os


def main():

    parser = argparse.ArgumentParser(description="Clean up powheg directory")

    parser.add_argument("path", type=str, help="path to powheg directory", default=".")

    args = parser.parse_args()
    # remove single file
    for f in [
        "bornequiv",
        "pwg-btlgrid.top",
        "pwggrid.dat",
        "pwgubound.dat",
        "realequivregions-btl",
        "FlavRegList",
        "pwgborngrid.top",
        "pwgcounters.dat",
        "pwghistnorms.top",
        "pwgxgrid.dat",
        "realequivregions-rad",
        "parameters.ol",
        "pwgboundviolations.dat",
        "pwgevents.lhe",
        "pwg-stat.dat",
        "pwhg_checklimits",
        "virtequiv",
    ]:
        os.remove(os.path.join(args.path, f))
    # remove parallel run files
    # TODO


if __name__ == "__main__":
    main()
