"""

    """

from pathlib import Path

import numpy as np
from githubdata import GitHubDataRepo
from mirutil.ns import rm_ns_module
from mirutil.ns import update_ns_module
from persiantools.jdatetime import JalaliDateTime

update_ns_module()
import ns

gdu = ns.GDU()
c = ns.Col()

def cal_daily_rate(apr) :
    x = np.log(1 + apr / 100)
    x = x / 365
    x = np.exp(x)
    x = x - 1
    return x

def main() :
    pass

    ##
    # get manual risk-free rate data
    gsr = GitHubDataRepo(gdu.src)

    ##
    df = gsr.read_data()

    ##
    gsr.rmdir()

    ##
    # calculate daily return from monthly return
    df[c.rf_d] = df[c.rf_apr].apply(cal_daily_rate)

    ##
    # clone target repo
    gtr = GitHubDataRepo(gdu.trg)
    gtr.clone_overwrite()

    ##
    # save data
    df.to_excel(gtr.data_fp , index = False)

    ##
    # get today's date
    tjd = JalaliDateTime.now().strftime('%Y-%m-%d')

    ##
    # commit msg
    msg = 'Updated on ' + tjd
    msg += ' by ' + gdu.slf

    ##
    gtr.commit_and_push(msg)

    ##
    gtr.rmdir()

    ##
    rm_ns_module()

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


# noinspection PyUnreachableCode
if False :
    pass

    ##

    ##

    ##
