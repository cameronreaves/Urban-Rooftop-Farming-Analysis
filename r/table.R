library(tidyverse)
library(gt)

t <- read_csv('data/summary.csv',col_names = c('Variable','Value')) %>%  drop_na()



t$Variable <- c('Total Produce','Total Produce Per Capita', 'Total Number of Farms','Total Surface Area (m2)','Total Kwhs Trade-off','Total Kwhs','Total Kwh Percentile')

t %>% 
  gt() %>% 
  fmt_number(
    columns = vars(Value),
    decimals = 2
  ) 
  

