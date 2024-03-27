#!/usr/bin/env python3
import argparse
import glob
import os
from pathlib import Path


def main():

    parser = argparse.ArgumentParser(description="Clean up powheg directory")

    # Adding optional argument with default value
    parser.add_argument(
        "-p", "--path", default=".", type=str, help="path to powheg directory"
    )

    args = parser.parse_args()

    id = "*"

    for r in ["btl", "rm", "reg"]:
        # remove single file
        for f in [
            f"bornequiv",
            f"pwggrid.dat",
            f"FlavRegList",
            f"pwgborngrid.top",
            f"pwgcounters.dat",
            f"pwghistnorms.top",
            f"pwgxgrid.dat",
            f"realequivregions-rad",
            f"virtequiv",
            f"parameters.ol",
            f"pwg-btilde-fullgrid.lock",
            f"pwg-remn-fullgrid.lock",
            f"pwg-{r}grid.top",
            f"realequivregions-{r}",
            f"mint_upb_{r}upb.top",
            f"mint_upb_{r}upb_rat.top",
            f"mint_upb_{r}upb.top",
            f"pwggrid-{r}.dat",
            f"pwg{id}-stat.dat",
            f"pwgxgrid-{r}{id}.dat",
            f"pwggrid-{r}{id}.dat",
            f"pwg{r}upb{id}.dat",
            f"pwgboundviolations{id}.dat",
            f"pwghistnorms{id}.top",
            f"pwgevents{id}.lhe",
            f"pwgcounters-st4{id}.dat",
            f"pwgcounters-st3{id}.dat",
            f"pwgcounters-st1{id}.dat",
            f"pwgcounters-st2{id}.dat",
            f"pwg-xg1-{r}{id}.top",
            f"pwg-xg1-xgrid-{r}{id}.dat",
            f"pwg-xg2-xgrid-{r}{id}.dat",
            f"pwg-xg2-xgrid-{r}{id}.top",
            f"pwg-st2-xgrid-{r}{id}.top",
            f"pwgubound{id}.dat",
            f"sigborn_equiv{id}",
            f"sigvirtual_equiv{id}",
            f"sigreal_{r}0_equiv{id}",
            f"sigreal_rad_equiv{id}",
            f"pwgalone-output{id}.top",
            f"pwgfullgrid-{r}{id}.dat",
            f"pwhg_checklimits{id}",
            f"pwg{id}-NLO.top",
            f"pwg{id}-borngrid-stat.dat",
            f"pwg{id}-xg1-stat.dat",
            f"pwg{id}-xg2-stat.dat",
            f"pwg{id}-st3-stat.dat",
            f"pwg{id}-st2-stat.dat",
        ]:
            for file in Path(args.path).glob(f"{f}"):
                os.remove(file)


if __name__ == "__main__":
    main()
