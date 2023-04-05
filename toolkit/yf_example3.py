import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    yf_example2.yf_prc_to_csv('QAN.AX','data/qan_prc_202033.csv',
                              start = start_date,
                              end = end_date)
## for testing
if __name__ == "__main__":
    import os
    import toolkit_config as cfg
    tic = 'QAN.AX'
    pth = os.path.join(cfg.DATADIR, 'qan_prc_20201.csv')
    yf_example2.yf_prc_to_csv(tic, pth,
                              start = '2020-01-01',
                              end = '2020-12-31')

