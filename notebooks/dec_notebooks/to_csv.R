library(foreign) 

files_path = '/home/fserrey/gitrep/ACA_project/docs_table/gastos_tablas'

files <- list.files(path = files_path, pattern = '.sav')

for(f in files){ # iterate over them 
  data <-read.spss(f, to.data.frame=TRUE,use.value.labels=FALSE) 
  write.csv(data, paste0(strsplit(f, split = '.', fixed =  T)[[1]][1], '.csv')) 
# the stringsplit removes the wrong ending and the paste adds .csv
}

files_path = '/home/fserrey/gitrep/ACA_project/docs_table/hogar_tablas'

files <- list.files(path = files_path, pattern = '.sav')

for(f in files){ # iterate over them 
  data <-read.spss(f, to.data.frame=TRUE,use.value.labels=FALSE) 
  write.csv(data, paste0(strsplit(f, split = '.', fixed =  T)[[1]][1], '.csv')) 
# the stringsplit removes the wrong ending and the paste adds .csv
}