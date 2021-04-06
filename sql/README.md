Table columns description:

## **Gastos**: 
|**Expense file**|**Length**|**Variable description**|**Values**|
| --- | --- | --- | --- |
|ANOENC||Year of survey|&lt;2020|
|NUMBER|5|Sequential number indicating the order of the household in the file|00001-25000|
|CODE|5|Expenditure code|See classification in ANNEX|
|EXPENDITURE|15.2|Total amount of monetary and non-monetary expenditures raised temporally and population wise|1 - 999999999999999|
|PORCENDES|5.2|Percentage breakdown of total expenditure (2 decimal places)|0-10000|
|PORCENIMP|5.2|Percentage of total expense allocation (2 decimal places)|0-10000|
|QUANTITY |12.2|Quantity (only for codes that require physical quantity) temporally and population-based high|b, 1-999999999999|
|GASTOMON |15.2|Total amount of **monetary expenditure** (for wages in kind only the amount of the payment made by the household is counted) raised by time and population.|b, 1-999999999999999|
|GASTNOM1 |13.2|Total amount of **non-monetary** expenditure **from self-consumption** high in terms of time and population.|b, 1-9999999999999|
|GASTNOM2 |13.2|Total amount of **non-monetary** expenditure **from self-supply** high in terms of time and population.|b, 1-9999999999999|
|GASTNOM3 |13.2|Total amount of **non-cash** expenditure from **salary in kind, (not including imputed rent for work-related housing)** high in terms of time and population.|b, 1-9999999999999|
|GASTNOM4 |13.2|Total amount of **non-cash** expenditure **on rent imputed to the main dwelling and other dwellings at the disposal of the household, owned or rented free or semi-free of charge for reasons other than** temporary and high population.|b, 1-9999999999999|
|GASTNOM5 |13.2|Total amount of **non-cash** expenditure **on rent imputed to the dwelling, main dwelling and other dwellings at the disposal of the household, assigned for** temporary and high population **work.**|b, 1-9999999999999|
|FACTOR|11.6|Population factor |any value, other than b and 0|

## Hogar
|**Household file**|**Length**|**Variable description**|**Values**|
| --- | --- | --- | --- |
|<h1>**1. GENERAL INFORMATION**</h1>|
|ANOENC||Year of survey|&gt;=2018|
|NUMBER|5|Sequential number indicating the order of the household in the file|00001- 22146|
|CCAA||Autonomous community of residence|<p>1 Andalusia</p><p>2 Aragon</p><p>3 Asturias, Principality of</p><p>4 Balears, Illes</p><p>5 Canary Islands</p><p>6 Cantabria</p><p>7 Castilla y León</p><p>8 Castilla - La Mancha</p><p>9 Catalonia</p><p>10 Valencian Community</p><p>11 Extremadura</p><p>12 Galicia</p><p>13 Madrid, Community of</p><p>14 Murcia, Region of</p><p>15 Navarra, Comunidad Foral de</p><p>16 Basque Country</p><p>17 Rioja, La</p><p>18 Ceuta</p><p>19 Melilla</p>|
|NUTS1|1|Region|<p>1 Northwest </p><p>2 Northeast </p><p>3 Community of Madrid </p><p>4 Central </p><p>5 East </p><p>6 South </p><p>7 Canary Islands </p>|
|CAPROV|1|Provincial capital|<p>1 Yes</p><p>6 No</p>|
|TAMAMU|1|Size of the municipality|<p>1 Municipality of 100,000 inhabitants or more </p><p>2 Municipality with 50,000 or more and less 100,000 inhabitants </p><p>3 Municipalities with 20,000 or more and less than 50,000 inhabitants</p><p>4 Municipalities with 10,000 or more and less than 20,000 inhabitants</p><p>5 Municipality with less than 10,000 inhabitants</p>|
|DENSITY|1|<p>Population density</p><p></p><p>Note: Modified in 2011</p>|<p>1 Densely populated area </p><p>2 Intermediate zone</p><p>3 Disseminated area</p>|
|KEY|1|Key to effective household collaboration |<p>1 First </p><p>2 Second </p>|
|CLATEO|1|Theoretical household collaboration key |<p>1 First </p><p>2 Second </p>|
|FACTOR|11.6|Population factor |Any value, other than b and 0|
|<h1>**2. HOUSEHOLD CHARACTERISTICS**</h1>|
|NMIEMB||Number of household members|1-20|
|SIZE|1|Household size|<p>1 One person </p><p>2 Two people </p><p>3 Three people </p><p>4 Four people</p><p>5 Five people </p><p>6 Six or more persons </p>|
|NMIEMSD||Number of household members in domestic service|<p>0-19 Number </p><p>-9 Not stated </p>|
|NMIEMHU||Number of household members who are guests |<p>0-19 Number </p><p>-9 Not stated </p>|
|NMIEMIN||Number of household members who are guests |<p>0-19 Number </p><p>-9 Not stated</p>|
|NMIEM1||Number of household members aged 14 years or older|1-20|
|NMIEM2||Number of household members under 14 years of age |0-19|
|NMIEM3||Number of household members under 16 years of age |0-19|
|NMIEM4||Number of household members 16 years old or older |1-20 |
|NMIEM5||Number of household members under 18 years of age |0-20|
|NMIEM6||Number of household members 18 years of age or older|0-20|
|NMIEM7||Number of household members 0 to 4 years old|0-20|
|NMIEM8||Number of household members 5 to 15 years old|0-20|
|NMIEM9||Number of household members 16 to 24 years old|0-20|
|NMIEM10||Number of household members 25 to 34 years old|0-20|
|NMIEM11||Number of household members 35 to 64 years old|0-20|
|NMIEM12||Number of household members 65 to 84 years old|0-20|
|NMIEM13||Number of household members 85 years old or older|0-20|
|NUMACTI||Number of active household members|0-20|
|NUMINACTI||Number of non-active household members|0-20|
|NUMOCU||Number of employed household members|0-20|
|NUMNOCU||Number of unoccupied household members|0-20|
|NUMESTU||Number of students in the household|0-20|
|NUMNOESTU||Number of non-students in the household|0-20|
|NNINOSD||<p>Number of dependent children</p><p></p><p>Note: See definition in variable TYPEHOGAR3.</p>|<p>0-20 Number</p><p>-9 Not stated</p>|
|NHIJOSD||<p>Number of dependent children</p><p></p><p>Note: See definition in variable TYPEHOGAR4.</p>|<p>0-19 Number </p><p>-9 Not stated</p>|
|UC1|3.1|<p>Equivalent household size. OECD scale</p><p>1 + 0.7 \* (NMIEM1 - 1) + 0.5 \* NMIEM2 </p>|1-150|
|UC2|3.1|<p>Equivalent household size. Modified OECD scale </p><p>1 + 0.5 \* (NMIEM1- 1) + 0.3 \* NMIEM2 </p>|1-110|
|PF2TEO||Number of theoretical individual account books |0-19|
|PF2RECO||Number of individual account books collected|0-19|
|TIPHOGAR1||Type of household (first classification) |<p></p><h5>**Single adult household**</h5><p></p><p>1 A person 65 years of age or older </p><p>2 One person between 30 and 64 years of age </p><p>3 A person under 30 years of age</p><p>4 One adult with children under 16 years of age                                  </p><p></p><h5>**Childless couple** </h5><p></p><p>5 Childless couple with at least one of the partners 65 years of age or older </p><p>6 Childless couple with both partners under 65 years of age </p><p>**Couple with children under 16 years of age** </p><p>7 Couple with a child under 16 years of age </p><p>8 Couple with two children under 16 years of age </p><p>9 Couple with three or more children under 16 years of age </p><p>**Other nuclear families** </p><p>10 Lone parent with at least one child 16 years of age or older </p><p>11 Couple with at least one child 16 years of age or older </p><p></p><h5>12 **Other households** </h5><p></p><p></p><p>` `Note: in this classification</p><p>Categories 07 to 11 refer exclusively to households consisting **of parents and children**, including adopted children and children of only one member of the couple. If there are other persons in the household, the household would be classified in 12.Other households.</p><p>An **adult** is any person **16 years of age or older.**</p>|
|TIPHOGAR2||Type of household (second classification) |<p></p><h5>**Single adult household** </h5><p></p><p>1 A person 65 years of age or older </p><p>2 One person between 30 and 64 years of age </p><p>3 A person under 30 years of age </p><p>4 One adult with children under 18 </p><p></p><h5>**Childless couple**</h5><p></p><p>5 Childless couple with at least one of the partners 65 years of age or older </p><p>6 Childless couple with both partners under 65 years of age </p><p>**Couple with children up to 18 years old** </p><p>7 Couple with a child under 18 years of age </p><p>8 Couple with two children under 18 years of age </p><p>9 Couple with three or more children under 18 years of age </p><p></p><h5>**Other nuclear families**</h5><p></p><p>10 Lone parent with at least one child 18 years of age or older </p><p>11 Couple with at least one child 18 years of age or older </p><p></p><h5>12 **Other households** </h5><p></p><p></p><p>Note: in this classification, categories 07 to 11 refer exclusively to **households consisting of parents and children**, including adopted children and children of only one member of the couple. If there are other persons in the household, the household would be classified in 12.Other households.</p><p>**An adult** is any person **18 years of age or older.**</p>|
|TIPHOGAR3||Type of household (third classification) |<p></p><h5>**Single-person household**</h5><p></p><p>1 65 and over </p><p>2 From 30 to 64 years old </p><p>3 Under 30 years old </p><p>**Couple without dependent children**</p><p>4 Couple without dependent children, at least one of the partners being 65 years of age or older </p><p>5 Couple without dependent children, both members under 65 years of age </p><p>**Couple with dependent children**</p><p>6 Couple with a dependent child </p><p>7 Couple with two dependent children </p><p>8 Couple with three or more dependent children </p><p>**Other nuclear families**</p><p>9 Lone parent, with at least one dependent child</p><p></p><h5>10 **Other households**</h5><p></p><p>-9 Not stated</p><p></p><p>Note: in this classification the following are considered </p><p>**Financially dependent children**:</p><p>` `- All children under 16 years of age.</p><p>` `- Those who are 16 or older but under 25 and economically inactive. </p>|
|TIPHOGAR4||Type of household (fourth classification) |<p>1 One person: man under 65 years of age</p><p>2 One person: male, 65 years old or older </p><p>3 One person: woman under 65 years of age </p><p>4 One person: woman 65 years of age or older </p><p>5 Two adults with no financially dependent children, at least one person 65 years of age or older </p><p>6 Two adults with no financially dependent children, both under 65 years of age </p><p>7 Other households without economically dependent children </p><p>8 An adult with at least one dependent child </p><p>9 Two adults with a dependent child </p><p>10 Two adults with two dependent children </p><p>11 Two adults with three or more dependent children </p><p>12 Other households with dependent children </p><p>-9 Not stated </p><p> </p><p>Note: In this classification are considered **economically dependent children**:</p><p>- All children under 16 years of age (if at least one parent is a member of the household).</p><p>- Those who are 16 or older but under 25 and economically inactive (if at least one parent is a member of the household).</p><p>**Adult:** any person 16 years of age or older but less than 25 years of age who is economically active and any person 25 years of age or older.</p>|
|TIPHOGAR5||Type of household (fifth classification) |<p>1 One person: man under 65 years of age </p><p>2 One person: male, 65 years old or older </p><p>3 One person: woman under 65 years of age </p><p>4 One person: woman 65 years of age or older </p><p>5 Two adults without financially dependent children, at least one person 65 years of age or older </p><p>6 Two adults without financially dependent children, both under 65 years of age </p><p>7 Other households without economically dependent children </p><p>8 An adult with at least one dependent child </p><p>9 Two adults with a dependent child </p><p>10 Two adults with two dependent children </p><p>11 Two adults with three or more dependent children </p><p>12 Other households with dependent children </p><p>-9 Not stated </p><p></p><p>Note: in this classification the following are considered </p><p>**Financially dependent children**:</p><p>- All children under 16 years of age.</p><p>- Those who are 16 or older but under 25 and economically inactive. </p><p>**Adult:** any person 16 years of age or older but less than 25 years of age economically active and any person 25 years of age or older.</p>|
|TIPHOGAR6||<p>Type of household (sixth classification) </p><p></p><p></p><p></p><p></p><p></p>|<p></p><h5>**Primary breadwinner without a partner**</h5><p></p><p>1 Lives alone </p><p>Lives with children (and perhaps others):</p><p>2 Age of youngest child: less than 23 years of age </p><p>3 Age of youngest child: 23 years or more </p><p>4 Lives with others but no children </p><p></p><h5>**Primary breadwinner with partner**</h5><p></p><p>5 Only the couple</p><p>**Couple (with children and perhaps others):**</p><p>6 Age of youngest child: up to 2 years </p><p>7 Age of youngest child: 3 to 15 years old</p><p>8 Age of youngest child: 16 to 22 years old</p><p>9 Age of youngest child: 23 years or more</p><p>10 Couple with others, no children</p>|
|TIPHOGAR7||Type of household (seventh classification) |<p>1 Single person under 65 years of age </p><p>2 Single person aged 65 and over </p><p>3 Couple without children </p><p>4 Couple with one child </p><p>5 Couple with two children</p><p>6 Couple with three or more children</p><p>7 An adult with children </p><p>8 Other type of households</p>|
|TIPHOGAR8||Household type (eighth classification) derived from TIPHOGAR1|<p>1 Person or couple (at least one of the members) 65 years of age or older </p><p>2 Other households with one person or couple without children </p><p>3 Couple with children under 16 years of age or adult with children under 16 years of age </p><p>4 Other households </p>|
|TIPHOGAR9||Household type (ninth classification) derived from TIPHOGAR4 |<p>1 One adult </p><p>2 Two adults </p><p>3 Other households without dependent children </p><p>4 An adult with at least one dependent child </p><p>5 Two adults with at least one dependent child </p><p>6 Other households with dependent children </p><p>-9 Not stated </p><p>Note: In this classification are considered **economically dependent children**:</p><p>- All children under 16 years of age (if at least one parent is a member of the household).</p><p>- Those who are 16 and older but under 25 and economically inactive.</p><p>(if at least one parent is a member of the household).</p><p>**Adult:** any person 16 years of age or older but less than 25 years of age economically active and any person 25 years of age or older.</p>|
|TIPHOGAR10||Type of household (tenth classification)|<p>**Single-person households**</p><p>1 Single-person households </p><p></p><h5>**Multi-person households**</h5><p></p><p>2 Single parent with dependent children </p><p>3 Couple without dependent children </p><p>4 Couple with dependent children </p><p>5 Other households with dependent children </p><p>6 Other households without dependent children </p><p>-9 Not stated </p><p>Note: </p><p>**Financially dependent children**:</p><p>- All children under 16 years of age.</p><p>- Those who are 16 or older but less than 25 and economically inactive.</p>|
|TIPHOGAR11||Type of household (eleventh classification)|<p>**Single-person households**</p><p>1 Single-person households </p><p></p><h5>**Multi-person households**</h5><p></p><p>2 Single parent with dependent children </p><p>3 Couple without dependent children </p><p>4 Couple with dependent children </p><p>5 Other households with dependent children </p><p>6 Other households without dependent children </p><p>-9 Not stated </p><p></p><p>Note: In this classification are considered **economically dependent children**:</p><p>- All children under 16 years of age (if at least one parent is a member of the household).</p><p>-Those who are 16 and older but less than 25 years old and economically inactive</p><p>(if at least one parent is a member of the household).</p><p>**Adult:** any person 16 years of age or older but less than 25 years of age economically active and any person 25 years of age or older.</p>|
|SITUOCUHOG||Occupational status of the household|<p>1 Employed primary breadwinner and spouse, at least one other member also employed </p><p>2 Main breadwinner and spouse employed, none of the other members employed (if any) </p><p>3 The primary breadwinner or employed spouse, other employed spouse, other employed member </p><p>4 The primary breadwinner or employed spouse, at least two other employed members </p><p>5 Main breadwinner or spouse employed, none of the other members employed (if any) </p><p>6 Neither the primary breadwinner nor his or her employed spouse, other employed member </p><p>7 Neither the main breadwinner nor his/her spouse employed, at least two other members employed </p><p>8 No one employed in the household </p><p>-9 Not stated </p>|
|SITUACTHOG||Household activity status|<p>1 Active primary breadwinner and spouse, at least one other member also active </p><p>2 The main breadwinner and spouse active, none of the other active members (if any) </p><p>3 The primary breadwinner or active spouse, other active member </p><p>4 The primary breadwinner or active spouse, at least two other active members </p><p>5 Primary breadwinner or active spouse, none of the other active members (if any) </p><p>6 Neither the primary breadwinner nor his/her spouse active, other active member </p><p>7 Neither the main breadwinner nor his/her spouse active, at least two other active members </p><p>8 No assets in the home </p><p>-9 Not stated </p>|
|**3. MAIN BREADWINNER'S DATA**|
|NORDENSP||Order number|01-20|
|EDADSP||<p>Age (calculated as of the date of completion of the household form)</p><p></p><p>Note: Extended the interval in 2011</p>|<p>` `85       Persons 85 years of age or older </p><p>16-84 Other persons </p>|
|SEXOSP||Sex|<p>1 Man </p><p>6 Female </p><p>-9 Not stated </p>|
|PAISNACSP||<p>Country of birth</p><p></p><p></p><p></p><p>Note: As of 2011</p>|<p>1 Spain</p><p>2 Rest of the European Union (27 countries)</p><p>3 Rest of Europe</p><p>4 Rest of the world</p><p>-9 Not stated</p>|
|NACIONASP||Nationality|<p>1 Spanish only </p><p>2 Foreign only </p><p>3 Spanish and foreign </p><p>-9 Not stated </p>|
|PAISSP||<p>Country of foreign nationality</p><p></p><p></p><p></p><p></p>|<p>1 Rest of the European Union (27 countries) </p><p>2 Rest of Europe	</p><p>3 Rest of the world </p><p>b Not applicable (if NACIONASP=1) </p><p>-9 Not stated </p>|
|SITURESSP||Residence status|<p>1 Present </p><p>6 Absent</p>|
|ECIVILLEGALSP||<p>Legal marital status</p><p></p><p></p><p></p><p>Note: As of 2011 this variable refers to legal marital status and not de facto marital status.</p>|<p>1 Single </p><p>2 Married </p><p>3 Widowed </p><p>4 Separate </p><p>5 Divorced </p><p>-9 Not stated </p>|
|NORDENCOSP||Order number of spouse or partner|<p>01-20 Number </p><p>99 If you do not have or are not a member of the household</p>|
|UNIONSP||<p>Type of union with spouse or partner</p><p></p><p></p><p></p><p>Note: As of 2011</p>|<p>1 Marriage</p><p>2 Registered domestic partner</p><p>3 Unregistered domestic partnership</p><p>b Not applicable (if NORDENCOSP=99)</p><p>-9 Not stated</p>|
|CONVIVIENCEP||<p>Cohabitation of the main breadwinner as a couple</p><p></p><p></p><p>Note: As of 2011</p>|<p>1 Living with your spouse</p><p>2 Living with a domestic partner</p><p>3 Not living together as a couple</p><p>-9 Not stated</p>|
|NORDENPASP||Father's order number|<p>01-20 Number </p><p>99 If you do not have or are not a member of the household</p>|
|PAISPADRESP||<p>Father's country of birth</p><p></p><p></p><p></p><p>Note: As of 2011</p>|<p>1 Spain</p><p>2 Rest of the European Union (27 countries)</p><p>3 Rest of Europe</p><p>4 Rest of the world</p><p>-9 Not stated</p>|
|NORDENMASP||Mother's order number|<p>01-20 Number</p><p>99 If you do not have or are not a member of the household</p>|
|PAISMADRESP||<p>Mother's country of birth</p><p></p><p></p><p></p><p>Note: As of 2011</p>|<p>1 Spain</p><p>2 Rest of the European Union (27 countries)</p><p>3 Rest of Europe</p><p>4 Rest of the world</p><p>-9 Not stated</p>|
|ESTUDIOSSP||<p>Completed studies</p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p>Note: Modified in 2015 to adapt to the new CNED 2014. (See Annex)</p>|<p>**1** Cannot read or write or went to school for less than 5 years</p><p>**2** Completed primary education or went to school for at least 5 years</p><p>**3** ESO, EGB or Elementary Baccalaureate (with degree or at least 3rd, 8th or 4th respectively) certificates of Primary Studies, Schooling (prior to 1999), or Professionalism (levels 1 or 2) and similar.</p><p>**4** Bachiller, BUP, COU, Bachiller Superior, FP de Grado Medio, FP Básica and other intermediate level studies (Certificate of Professionalism level 3, etc...).</p><p>**5** Advanced Vocational Training, FPII and equivalents</p><p>**6** Degree of 240 ECTS, Diploma, Architecture and Technical Engineering and equivalents.</p><p>**7** Bachelor's degree with more than 240 ECTS, Bachelor's degree, Architecture, Engineering, Master's degree, specialization in Health Sciences and equivalent.</p><p>**8** University doctorate. </p><p></p>|
|ESTUDREDSP||Studies completed reduced|<p>1 Lower than the first stage of Secondary Education.</p><p>2 Lower secondary education </p><p>3 Second stage of secondary education </p><p>4 Higher education </p>|
|SITUACTSP||<p>Activity status in the week prior to the interview</p><p></p><p></p><p></p><p></p><p></p><p>Note: As of 2011, persons 'With permanent labor disability' are included in a separate category.</p>|<p>1 Working at least one hour </p><p>2 With work from which he/she is absent (due to illness, vacation, maternity leave, etc.) and to which he/she expects to return.</p><p>3 Unemployed </p><p>4 Retired, early retirement</p><p>5 Student </p><p>6 Dedicated to household chores </p><p>7 With permanent incapacity for work</p><p>8 Other economic inactivity </p>|
|SITUREDSP||Reduced activity situation|<p>1 Active </p><p>2 Inactive </p>|
|OCUSP||Was the primary breadwinner busy in the week prior to the interview?|<p>1 Busy</p><p>2 Not occupied</p>|
|JORNADASP||<p>Type of workday</p><p></p><p></p><p>Note: As of 2011</p>|<p>1 Complete</p><p>2 Partial</p><p>b Not applicable (If SITUACTSP&lt;&gt;&gt;1,2 or AGE&lt; 16)</p><p>-9 Not stated</p>|
|PERCEPSP||Is the SP a recipient of regular monetary income during the month prior to the month of interview?|<p>1 Yes </p><p>6 No </p><p>-9 Not stated </p>|
|IMPEXACPSP|5|Exact amount of the primary breadwinner's net monthly income |<p>0-99999 Amount </p><p>b Not applicable (if PERCEPSP=6) </p><p>-9 Not stated </p>|
||||<h4></h4>|
|INTERINPSP||Total net monthly income range of the main breadwinner|<p>1 Less than €500 </p><p>2 From 500 to less than 1000 </p><p>3 From 1,000 to less than 1,500 </p><p>4 From 1,500 to less than 2,000 </p><p>5 From 2000 to less than 2500 </p><p>6 From 2,500 to less than 3,000 </p><p>7,000 or more € 7,000 or more</p><p>b Not applicable (if PERCEPSP=6)</p><p>-9 Not stated </p>|
|||||
|WORK||Have you ever worked in your life?|<p>1 Yes</p><p>6 No </p><p>-9 Not stated </p>|
|OCUPA||<p>Occupation held or performed</p><p>(See APPENDIX: Classification of occupations)</p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p>Note: As of 2012 new National Classification of Occupations, CNO11.</p>|<p>1 Directors and managers </p><p>2 Scientific and intellectual technicians and professionals </p><p>3 Technicians and support professionals </p><p>4 Accounting, clerical, administrative and other clerical employees </p><p>5 Catering, personal, protection, and sales workers</p><p>6 Skilled workers in the agriculture, livestock, forestry and fishing sectors </p><p>7 Craftsmen and skilled workers in the manufacturing and construction industries (except plant and machinery operators) </p><p>8 Plant and machinery operators and assemblers</p><p>9 Elementary occupations</p><p>0 Military occupations </p><p>b Not applicable (if WORK=6) </p><p>-9 Not stated </p>|
|OCUPARED||<p>Occupation held or formerly held reduced</p><p>(See APPENDIX: Classification of occupations)</p><p></p><p></p><p></p><p></p><p></p><p>Note: As of 2012 new National Classification of Occupations, CNO11.</p>|<p>1 Directors and managers</p><p>2 Technicians and professionals </p><p>3 Administrative type employees and service and trade workers</p><p>4 Craftsmen and skilled workers in other sectors, operators and assemblers </p><p>5 Workers in elementary occupations</p><p>b Not applicable (IF WORK=6)</p><p>-9 Not stated (includes Armed Forces) </p>|
|ACTESTB||<p>Activity of the establishment where you work or worked</p><p>(See ANNEX: National Classification of Economic Activities CNAE2009).</p>|<p>A Agriculture, livestock, forestry and fishing</p><p>B Mining and quarrying</p><p>C Manufacturing industry</p><p>D Electric power, gas, steam and air conditioning supply</p><p>E Water supply, sewerage, waste management and decontamination activities</p><p>F Construction</p><p>G Wholesale and retail trade; repair of motor vehicles and motorcycles </p><p>H Transportation and storage</p><p>I Hospitality</p><p>J Information and communications</p><p>K Financial and insurance activities</p><p>L Real estate activities</p><p>M Professional, scientific and technical activities</p><p>N Administrative and support service activities</p><p>O Public administration and defense; compulsory social security</p><p>P Education</p><p>Q Health and social work activities</p><p>R Artistic, recreational and entertainment activities</p><p>S Other services</p><p>T Activities of households as employers of domestic personnel</p><p>b Not applicable (if WORK=6) </p><p>-9 Not stated (includes activities of extraterritorial organizations and agencies)</p>|
|ACTESTBRED||<p>Activity of the establishment in which he/she works or worked reduced</p><p>(See ANNEX: National Classification of Economic Activities CNAE2009).</p>|<p>1 Agriculture, livestock, forestry and fishing</p><p>2 Mining and quarrying, manufacturing, electricity, gas, steam and air conditioning, water, sanitation, waste management and decontamination, construction</p><p>3 Services</p><p>b Not applicable (if WORK=6) </p><p>-9 Not stated (includes activities of extraterritorial organizations and agencies)</p>|
|SITPROF||Professional status|<p>1 Salaried</p><p>2 Entrepreneur without employees or </p><p>independent worker</p><p>3 Employer</p><p>4 Other situation (family support, etc.) </p><p>b Not applicable (if WORK=6) </p><p>-9 Not stated</p>|
|SECTOR||Sector of activity|<p>1 Public </p><p>2 Private </p><p>b Not applicable (if WORK=6) </p><p>-9 Not stated </p>|
|CONTRACT||Employment contract|<p>1 With contract</p><p>6 No contract</p><p>b Not applicable (if WORK=6)</p><p>-9 Not stated</p>|
|TIPOCONT||Type of contract|<p>1 Indefinite </p><p>2 T temporal </p><p>b Not applicable (if WORK=6 or CONTRACT=6) </p><p>-9 Not stated </p>|
|SITSOCI||<p>Socioeconomic status of the primary breadwinner</p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p></p><p>Note: As of 2012, this variable has been adapted to the new National Classification of Occupations, CNO11.</p>|<p></p><h1>**Private sector**</h1><p></p><p></p><p>2 Non-manual worker, except agriculture</p><p></p><h4>**Public sector**</h4><p></p><p></p><p>4 Non-manual worker, except agriculture</p><p></p><h4>**Others**</h4><p></p><p></p><p>6 Independent farmer or agricultural worker</p><p></p><p></p><p>9 Student</p><p>10 Housework or non-economic activity</p><p>11 Unable to work</p><p>-9 Not stated  </p>|
|SITSOCIRE||<p>Socioeconomic status of the main breadwinner (Reduced classification)</p><p></p><p></p><p></p><p></p><p></p>|<p>1 Manual laborer, except agriculture </p><p>2 Non-manual worker, except agriculture</p><p>3 Self-employed and farmer or worker</p><p>` `in agriculture </p><p>4 Standing </p><p>5 Retired or retired </p><p>6 Other inactive </p><p>-9 Not stated</p>|
|**4. CHARACTERISTICS OF THE MAIN DWELLING**|
|REGTEN|1|Tenure regime|<p>1 Property with no outstanding loan or mortgage </p><p>2 Property with loan or mortgage in progress </p><p>3 Rental </p><p>4 Reduced rent (old rent) </p><p>5 Semi-free assignment </p><p>6 Assignment free of charge </p>|
|TIPOEDIF||Type of building in which the dwelling is located|<p>1 Detached single-family house </p><p>2 Single-family semi-detached or semi-detached house </p><p></p><h1>**Building with more than one dwelling**</h1><p></p><p>3 With less than 10 dwellings </p><p>4 With 10 or more dwellings </p><p>5 Other (intended for other purposes or fixed housing) </p><p>-9 Not stated </p>|
|ZONARES||Type of area of residence|<p>1 Urban luxury </p><p>2 High urban </p><p>3 Medium urban </p><p>4 Lower urban </p><p>5 Rural industrial </p><p>6 Rural fishing </p><p>7 Rural agricultural </p><p>-9 Not stated </p>|
|TIPOCASA||Type of house|<p>1 Chalet or large house </p><p>2 Medium house </p><p>3 Economic house or lodging </p><p>-9 Not stated </p>|
|NHABIT||Number of rooms|<p>1-7 No. of rooms (1 to 7) </p><p>8     No. of rooms (&gt;7)</p><p>-9    Not stated </p>|
|ANNOCON||Date of construction of building|<p>1 Less than 25 years ago </p><p>6 25 or more years ago </p><p>-9 Not stated </p>|
|SUPERF||Living area of the dwelling|<p>35         35 meters or less </p><p>36-299 Meters </p><p>300       300 meters or more</p><p>-9          Not stated </p>|
|AGUACALI||Hot water supply|<p>1 Yes </p><p>6 No </p><p>-9 Not stated </p>|
|FUENAGUA||Power source for hot water|<p>1 Electricity </p><p>2 Natural gas </p><p>3 Liquefied gas </p><p>4 Other liquid fuels </p><p>5 Solid fuels </p><p>6 Others </p><p>b Not applicable (if AGUACALI=6) </p><p>-9 Not stated </p>|
|CALEF||Heating arrangement|<p>1 Yes</p><p>6 No </p><p>-9 Not stated </p>|
|FUENCALE||Energy source for heating|<p>1 Electricity </p><p>2 Natural gas </p><p>3 Liquefied gas </p><p>4 Other liquid fuels </p><p>5 Solid fuels </p><p>6 Others </p><p>b Not applicable (if CALEF=6) </p><p>-9 Not stated </p>|
|**5. OTHER HOUSING AVAILABLE TO THE HOUSEHOLD**|
|DISPOSIOV|1|Other housing disposition in the last 12 months|<p>1 Yes</p><p>6 No </p>|
|NUMOVD|1|Number of other dwellings available to the household|<p>1-9 Number</p><p>b Not applicable (if DISPOSIOV=6) </p>|
|||**THE FOLLOWING VARIABLES ARE REPEATED 9 TIMES; i=1,....... 9**|
|REGTENVi||Housing tenancy regime "i".|<p>1 Property with no outstanding loan or mortgage </p><p>2 Property with loan or mortgage in progress </p><p>3 Rental </p><p>4 Reduced rent (old rent) </p><p>5 Semi-free assignment </p><p>6 Assignment free of charge </p><p>-9 Not stated </p><p>b Not applicable (if DISPOSIOV=6) </p>|
|MONTHS Vi||Number of months at the disposal of the household of dwelling "i".|<p>0-12 Months</p><p>-9 Not stated </p><p>b Not applicable (if DISPOSIOV=6) </p>|
|DIASVi||Number of days at the disposal of the household of the dwelling "i".|<p>0-31 Days </p><p>-9 Not stated </p><p>b Not applicable (if DISPOSIOV=6) </p>|
|AGUACVi||Hot water supply in dwelling "i".|<p>1 Yes </p><p>6 No </p><p>-9 Not stated </p><p>b Not applicable (if DISPOSIOV=6) </p>|
|FUENACVi||Source of energy for hot water in dwelling "i".|<p>1 Electricity </p><p>2 Natural gas </p><p>3 Liquefied gas </p><p>4 Other liquid fuels</p><p>5 Solid fuels </p><p>6 Others </p><p>-9 Not stated </p><p>b Not applicable (if DISPOSIOV=6 or AGUACVi=6) </p>|
|CALEFVi||Heating arrangement in    dwelling "i".|<p>1 Yes </p><p>2 No </p><p>-9 Not stated </p><p>b Not applicable (if DISPOSIOV=6) </p>|
|FUENCAVi||Source of energy for heating in dwelling "i".|<p>1 Electricity </p><p>2 Natural gas </p><p>3 Liquefied gas </p><p>4 Other liquid fuels </p><p>5 Solid fuels </p><p>6 Others </p><p>-9 Not stated </p><p>b Not applicable (if DISPOSIOV=6 or CALEFVi=6) </p>|
|**6. HOUSEHOLD CONSUMER SPENDING**|
|GASTOT|16.2|Total amount of **annual household expenditure (monetary and non-monetary**, time and population adjusted) (for salary in kind, both the amount of the payment made and the bonus received are included). |1-9999999999999999 |
|IMPUTGAS|5.2|Percentage of total expense allocation |0-10000 Percent |
|GASTMON|16.2|Total amount of the **household's** annual **monetary expenditure**    raised temporally and population-wise (only the amount of the payment made by the household is counted for the salary in kind).|b,1-9999999999999999 |
|GASTNOM1|13.2|Total amount of annual **household non-cash** expenditure **from self-consumption**, (includes the value of free meals in the catering establishment owned by a member of the household) raised temporally and population-wise.|` `b,1-9999999999999 |
|GASTNOM2|13.2|Total amount of annual household **non-cash** expenditure **from self-supply**, raised by time and population. |b,1-9999999999999 |
|GASTNOM3|13.2|Total amount of annual **non-cash household** expenditure **from wages in kind, (includes** imputed rent for work-related housing and value of free or subsidized meals at the workplace of a member of the household who works as a wage earner**)** raised by time and population.|b, 1-9999999999999 |
|GASTNOM4|13.2|Total amount of the **household's** annual **non-cash** expenditure **on rent imputed to the main dwelling and to other dwellings at the household's disposal, owned or rented free or semi-free of charge for reasons other than work,** temporarily and population-wise. |b,1-9999999999999 |
|**7. REGULAR MONTHLY HOUSEHOLD INCOME**|
|CAPROP||Self-employment income|<p>1 Yes </p><p>6 No</p><p>-9 Not stated </p>|
|BOX||Income from employment|<p>1 Yes </p><p>6 No </p><p>-9 No Record </p>|
|PENSIO||Income from contributory and non-contributory pensions|<p>1 Yes </p><p>6 No </p><p>-9 Not stated</p>|
|DESEM||Unemployment benefits and allowances|<p>1 Yes </p><p>6 No </p><p>-9 Not stated </p>|
|OTRSUB||Other allowances and social benefits|<p>1 Yes </p><p>6 No </p><p>-9 Not stated</p>|
|RENT||Income from property and capital|<p>1 Yes </p><p>2 No </p><p>-9 Not stated </p>|
|OTROIN||Other regular income|<p>1 Yes </p><p>6 No </p><p>-9 Not stated </p>|
|FUENPRIN||Main source of income|<p>1 Own account </p><p>2 Employee </p><p>3 Contributory pensions </p><p>4 Unemployment </p><p>5 Other benefits </p><p>6 Income from capital and property </p><p>7 Other regular income </p><p>-9 Not stated</p><p>b Not applicable (if CAPROP=...=OTROIN=6) </p>|
|FUENPRINRED||Main source of income reduced|<p>1 Self-employment, property and capital income </p><p>2 Employed work </p><p>3 Pensions, allowances and other benefits and regular income </p><p>-9 Not stated </p><p>b Not applicable (if CAPROP=...=OTROIN=6) </p>|
|IMPEXAC|5|Exact amount of total net monthly household income|0-99999 Amount|
|INTERIN||Total net monthly household income range|<p>1 Less than €500</p><p>2 From 500 to less than 1000 </p><p>3 From 1,000 to less than 1,500 </p><p>4 From 1,500 to less than 2,000 </p><p>5 From 2000 to less than 2500 </p><p>6 From 2,500 to less than 3,000 </p><p>7 From 3,000 to less than 5,000 </p><p>8 From 5000 to less than 7000 €. </p><p>9 From 7000 to less than 9000 €. </p><p>10 9000 or more </p>|
|NUMPERI||Number of income-earning members of household|<p>0-20 Number</p><p>-9 Not stated </p>|
|<h5>**8. NUMBER OF LUNCHES AND DINNERS DURING THE TWO-WEEK SAMPLING PERIOD**</h5>|
|COMIMH||Number of lunches and dinners eaten by household members (excluding domestic service, guests and invitees)|<p>0-999 Number </p><p>-9 Not stated </p>|
|COMISD||Number of lunches and dinners provided by the domestic service (whether or not members of the household)|<p>0-999 Number    </p><p>-9 Not stated </p>|
|COMIHU||Number of lunches and dinners provided by guests (household members and non-household members)|<p>0-999 Number    </p><p>-9 Not stated </p>|
|COMIINV||Number of lunches and dinners eaten by guests (household members and non-household members)|<p>0-999 Number    </p><p>-9 Not stated </p>|
|COMITOT||Total number of lunches and dinners|<p>0-999 Number    </p><p>-9 Not stated </p>|