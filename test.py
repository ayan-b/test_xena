from __future__ import print_function

import time

from xena_gdc_etl import xena_dataset

# styling stuff
import colorama
colorama.init()
from colorama import Fore, Style
# end


GDC_XENA_COHORT = [
    'TCGA-BRCA', #
    'TCGA-LUAD', #
    'TCGA-UCEC', #
    'TCGA-LGG', #
    'TCGA-HNSC', #
    'TCGA-PRAD', #
    'TCGA-LUSC', #
    'TCGA-THCA', #
    'TCGA-SKCM', #
    'TCGA-OV', #
    'TCGA-STAD', #
    'TCGA-COAD', #
    'TCGA-BLCA', #
    'TCGA-GBM', #
    'TCGA-LIHC', #
    'TCGA-KIRC', #
    'TCGA-CESC', #
    'TCGA-KIRP', #
    'TCGA-SARC', #
    'TCGA-ESCA', #
    'TCGA-PAAD', #
    'TCGA-PCPG', #
    'TCGA-READ', #
    'TCGA-TGCT', #
    'TCGA-LAML', #
    'TCGA-THYM', #
    'TCGA-ACC',
    'TCGA-MESO',
    'TCGA-UVM',
    'TCGA-KICH', #
    'TCGA-UCS',
    'TCGA-CHOL',
    'TCGA-DLBC',
]


xena_dtypes = [
    'masked_cnv',  # Masked Copy Number Segment 
    'mirna',  # miRNA Expression Quantification
    'muse_snv',  # MuSE Variant Aggregation and Masking
    'mutect2_snv',  # MuTect2 Variant Aggregation and Masking
    'somaticsniper_snv',  # SomaticSniper Variant Aggregation and Masking
    'varscan2_snv',  # VarScan2 Variant Aggregation and Masking
    'htseq_counts',  # HTSeq - Counts
    'htseq_fpkm',   # HTSeq - FPKM
    'htseq_fpkm-uq',  # HTSeq - FPKM-UQ
    # 'methylation450',  # Illumina Human Methylation 450 
]


# testing code starts here
import sys
if sys.version_info[0] < 3:
    projects = GDC_XENA_COHORT[22]  # TCGA-READ
elif sys.version_info[0] == 3 and sys.version_info[1] == 7:
    projects = GDC_XENA_COHORT[23]  # TCGA-TGCT
elif sys.version_info[0] == 3 and sys.version_info[1] == 6:
    projects = GDC_XENA_COHORT[24]  # TCGA-LAML
elif sys.version_info[0] == 3 and sys.version_info[1] == 5:
    projects = GDC_XENA_COHORT[25]  # TCGA-THYM
for xena_dtype in xena_dtypes:
    try:
        start = time.time()
        dataset = xena_dataset.GDCOmicset(
            projects=projects,
            root_dir=r'./test',
            xena_dtype=xena_dtype
        )
        dataset.download().transform().metadata()
        print("Time taken:", int((time.time()-start)//60), "min", round((time.time()-start)%60), "sec")
        print(Fore.GREEN + "Pipeline succeed for {} in {} project".format(xena_dtype, projects))
        print(Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + str(e))
        print(Fore.RED + "Pipeline failed for {}".format(xena_dtype))
        print(Style.RESET_ALL)
