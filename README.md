# Encuesta de Presupuestos Familiares - Data extraction and transformation

The Household Budget Survey (Encuesta de Presuspuestos Familiares) provides annual information on the nature and destination of consumption expenditures, as well as on various characteristics related to household living conditions. The whole data its collected by the National Statistic Institute from Spain (*[Instituto Nacional de Estadística](www.ine.es)* or *INE* in Spanish)

The sample size is approximately 24,000 households per year. The dataset has been made using the public data provided by the National Statistic Institute from Spain (INE). I have used the microdata downloadable from[ their website](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176806&menu=resultados&secc=1254736195147&idp=1254735976608#!tabs-1254736195147).

The data that you can download from the official website comes in a painful format that makes it hard to start working by an unexpert user of this type of data (*like myself!*). Thus, I transformed the currently available time series to a CSV format so anyone can use it.

As it is very hard to summarize the whole structure of the columns included in each table, [here you can find the official file (Spanish) ](https://www.ine.es/metodologia/t25/t2530p45816.pdf)describing the methodology used to build the table structure and what do every value mean. 