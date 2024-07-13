#munge
/Users/janedoe/Desktop/GeneticCorrelation/ldsc/munge_sumstats.py \
--sumstats /Users/janedoe/Desktop/GeneticCorrelation/sum_stats/daner_pgc_mdd_meta_w2_no23andMe_rmUKBB \
--signed-sumstats OR,1 \
--snp SNP \
--a1 A1 \
--a2 A2 \
--p P \
--N-cas-col Nca \
--N-con-col Nco \
--merge-alleles /Users/janedoe/Desktop/GeneticCorrelation/inputs/eur_w_ld_chr/w_hm3.snplist \
--out /Users/janedoe/Desktop/GeneticCorrelation/sum_stats/munged/mdd_munged

/Users/janedoe/Desktop/GeneticCorrelation/ldsc/munge_sumstats.py \
--sumstats /Users/janedoe/Desktop/GeneticCorrelation/sum_stats/pgc-panic2019.vcf.tsv \
--signed-sumstats BETA,0 \
--snp ID \
--a1 A1 \
--a2 A2 \
--p PVAL \
--N-cas-col NCAS \
--N-con-col NCON \
--merge-alleles /Users/janedoe/Desktop/GeneticCorrelation/inputs/eur_w_ld_chr/w_hm3.snplist \
--out /Users/janedoe/Desktop/GeneticCorrelation/sum_stats/munged/panic_munged

#genetic correlation
/Users/janedoe/Desktop/GeneticCorrelation/ldsc/ldsc.py \
--rg /Users/janedoe/Desktop/GeneticCorrelation/sum_stats/munged/panic_munged.sumstats.gz,/Users/janedoe/Desktop/GeneticCorrelation/sum_stats/munged/mdd_munged.sumstats.gz \
--ref-ld-chr /Users/janedoe/Desktop/GeneticCorrelation/inputs/eur_w_ld_chr/ \
--w-ld-chr /Users/janedoe/Desktop/GeneticCorrelation/inputs/eur_w_ld_chr/ \
--out /Users/janedoe/Desktop/GeneticCorrelation/rg/mdd_panic
