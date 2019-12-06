#pyhon3

import pandas as pd
import numpy as np
import csv
from datetime import datetime
import sys
from tabulate import tabulate


print("")
print("Importing data . . . ")
print("")
df_repoff = pd.read_csv('repoffinput.csv', usecols = ['Organization Name (English)', 'Professional Supervisory Unit (English)', 'Professional Supervisory Unit (Chinese)', 'Field of Work', 'Registration Location', 'Date of Registration', 'Permitted Area(s) of Operation', 'Aging', 'Agriculture', 'Animal Protection', 'Arts and Culture', 'Civil Soc\'y Cap\'y building', 'Disabilities', 'Disaster Relief', 'Econ. Development', 'Education', 'Energy', 'Environment', 'Ethnic Affairs', 'Gender Issues', 'Health', 'Human Rights', 'Infrastructure', 'Int\'l Relations/Exchange', 'Labor', 'Law and Governance', 'LGBTQ Issues', 'Media', 'Migrants', 'Poverty Alleviation', 'Religion', 'Rural Issues/Devt', 'Sport', 'Technology', 'Tourism', 'Trade', 'Urban Issues/Devt', 'Youth', 'ALL OF CHINA', 'Anhui', 'Beijing', 'Chongqing', 'Fujian', 'Gansu', 'Guangdong', 'Guangxi', 'Guizhou', 'Hainan', 'Hebei', 'Heilongjiang', 'Henan', 'Hubei', 'Hunan', 'Inner Mongolia', 'Jiangsu', 'Jiangxi', 'Jilin', 'Liaoning', 'Ningxia', 'Qinghai', 'Shaanxi', 'Shandong', 'Shanghai', 'Shanxi', 'Sichuan', 'Tianjin', 'Tibet', 'Xinjiang', 'Xinjiang Bingtuan', 'Yunnan', 'Zhejiang', 'Unknown'])


print("What is the last date you want included in the data? YYYY-MM-DD") #if you want to incorporate this more elegantly into the command line check out page 46 in Learn Python the Hard Way

input_date = input()

#input_date = '2019-11-30'

# https://www.journaldev.com/23365/python-string-to-datetime-strptime
data_cutoff = datetime.strptime(input_date, '%Y-%m-%d')
h1_date = datetime.strftime(data_cutoff, '%B %Y')
footnote_date = datetime.strftime(data_cutoff, '%B %-d, %Y')



########## PUTTING IN SOME CHECKS TO MAKE SURE YOU'RE AWAKE ####################
# sort the registration dates https://stackoverflow.com/questions/28161356/sort-pandas-dataframe-by-date
df_repoff['Date of Registration'] = pd.to_datetime(df_repoff['Date of Registration'])
df_repoff = df_repoff.sort_values('Date of Registration')
# filter out the entries after the cutoff date  https://www.interviewqs.com/ddi_code_snippets/select_pandas_dataframe_rows_between_two_dates
date_filter = (df_repoff['Date of Registration'] <= data_cutoff)
df_repoff = df_repoff.loc[date_filter]
total_ROs = len(df_repoff)


print("")
print("Based on this data cutoff date, you should have " + str(total_ROs) + " total ROs included in this dataset. Is that correct?  y/n")
print("")
if input() == "y":
	print("")
	print ("Great. Let me make an html table for you then.")
else:
	print("")
	print ("Something has gone terribly wrong. Terminating program.")
	sys.exit("Closed.")


PSU_replace = {
"Anhui Administration of Market Regulation (formerly Anhui Administration of Quality and Technical Supervision)":"安徽省质量技术监督局",
"Anhui Health Commission (formerly Anhui Health and Family Planning Commission)":"安徽省卫生健康委员会",
"Beijing Bureau of Agriculture and Rural Affairs (formerly Beijing Bureau of Agriculture)":"北京市农业农村局",
"Beijing Bureau of Ecology and Environment (formerly Beijing Bureau of Environmental Protection)":"北京市生态环境局",
"Beijing Bureau of Economy and Information Technology (formerly Beijing Commission of Economy and Informatization)":"北京市经济和信息化局",
"Beijing Bureau of Sport":"北京市体育局",
"Beijing Commission of Commerce":"北京市商务委员会",
"Beijing Commission of Education":"北京市教育委员会",
"Beijing Commission of Science and Technology":"北京市科学技术委员会",
"Beijing Commission of Transport":"北京市交通委员会",
"Beijing Development and Reform Commission":"北京市发展和改革委员会",
"Beijing Gardening and Greening Bureau":"北京市园林绿化局",
"Beijing Health Commission (formerly Beijing Health and Family Planning Commission)":"北京市卫生健康委员会",
"Beijing Intellectual Property Office":"北京市知识产权局",
"China Banking and Insurance Regulatory Commission":"中国银行保险监督管理委员会",
"China Disabled Person’s Federation":"中国残疾人联合会",
"Chinese Association for International Understanding":"中国国际交流协会",
"Chinese People’s Association for Friendship with Foreign Countries":"中国人民对外友好协会",
"Chongqing Bureau of Civil Affairs":"重庆市民政局",
"Chongqing Commission of Agriculture and Rural Affairs (formerly Chongqing Agriculture Commission)":"重庆市农业农村委员会",
"Chongqing Commission of Commerce":"重庆市商务委",
"Chongqing Commission of Economy and Informatization":"重庆市经济和信息化委员会",
"Chongqing Culture and Tourism Development Commission (formerly Chongqing Tourism Development Commission)":"重庆市文化和旅游发展委员会",
"Chongqing Department of Ecology and Environment (formerly Chongqing Department of Environmental Protection )":"重庆市生态环境局",
"Chongqing Health Commission (formerly Chongqing Health and Family Planning Commission)":"重庆市卫生健康委员会",
"Chongqing Office of Hong Kong and Macau Affairs":"重庆市人民政府港澳事务办公室",
"Chongqing Office of Poverty Alleviation and Development":"重庆市扶贫开发办公室",
"Chongqing Office of Taiwan Affairs":"重庆市人民政府台湾事务办公室        ",
"Civil Aviation Administration of China":"中国民航局",
"Fujian Administration of Radio and Television (formerly Fujian Administration of Press, Publication, Radio, Film, and Television)":"福建省广播电视局",
"Fujian Department of Agriculture and Rural Affairs (formerly Fujian Department of Agriculture)":"福建省农业农村厅",
"Fujian Department of Civil Affairs":"福建省民政厅",
"Fujian Department of Commerce":"福建省商务厅",
"Fujian Department of Culture and Tourism (formerly Fujian Department of Culture)":"福建省文化和旅游厅",
"Fujian Department of Education":"福建省教育厅",
"Fujian Federation of Trade Unions":"福建省总工会",
"Fujian People’s Government Office of Foreign Affairs":"福建省人民政府外事办公室",
"Gansu Department of Education":"甘肃省教育厅",
"Gansu Health Commission (formerly Gansu Health and Family Planning Commission)":"甘肃省卫生健康委员会",
"General Administration of Customs":"中华人民共和国海关总署",
"General Administration of Sport":"国家体育总局",
"Guangdong Department of Civil Affairs":"广东省民政厅",
"Guangdong Department of Commerce":"广东省商务厅",
"Guangdong Department of Education":"广东省教育厅",
"Guangdong Federation of Trade Unions":"广东省总工会",
"Guangdong Health Commission (formerly Guangdong Health and Family Planning Commission)":"广州市卫生健康委员会",
"Guangdong Office of Overseas Chinese Affairs":"广东省人民政府侨务办公室",
"Guangdong Youth Federation":"广东省青年联合会",
"Guangxi Department of Civil Affairs":"广西壮族自治区民政厅",
"Guangxi Department of Commerce":"广西壮族自治区商务厅",
"Guangxi Department of Education":"广西省教育厅",
"Guizhou Department of Civil Affairs":"贵州省民政厅",
"Hainan Department of Civil Affairs":"海南省民政厅",
"Hainan Health Commission (formerly Hainan Health and Family Planning Commission)":"海南省卫生健康委员会",
"Hebei Department of Civil Affairs":"河北省民政厅",
"Hebei Department of Commerce":"河北省商务厅",
"Heilongjiang Department of Commerce":"黑龙江省商务厅",
"Heilongjiang Health Commission (formerly Heilongjiang Health and Family Planning Commission)":"黑龙江省卫生健康委员会",
"Henan Department of Education":"河南省教育厅",
"Henan People’s Association for Friendship with Foreign Countries":"河南省人民对外友好协会",
"Hubei Department of Agriculture and Rural Affairs (formerly Hubei Department of Agriculture)":"湖北省农业厅",
"Hubei Department of Commerce":"湖北省商务厅",
"Hubei Health Commission (formerly Hubei Health and Family Planning Commission)":"湖北省卫生健康委员会",
"Hubei Province Department of Civil Affairs":"湖北省民政厅",
"Hunan Department of Civil Affairs":"湖南省民政厅",
"Hunan Department of Commerce":"商务厅",
"Hunan Department of Education":"湖南省教育厅",
"Hunan Department of Science and Technology":"湖南省科技厅",
"Hunan Office of Overseas Chinese Affairs":"湖南省人民政府侨务办公室",
"Hunan People’s Government Office of Foreign Affairs":"湖南省人民政府外事办公室",
"Inner Mongolia Department of Commerce":"内蒙古商务厅",
"Inner Mongolia Forestry and Grassland Administration (formerly Inner Mongolia Forestry Administration)":"内蒙古自治区林业和草原局",
"Jiangsu Department of Commerce":"江苏省商务厅",
"Jiangsu Department of Culture and Tourism (formerly Jiangsu Department of Culture)":"江苏省文化和旅游厅",
"Jiangsu Department of Education":"江苏省教育厅",
"Jiangxi Department of Civil Affairs":"江西省民政厅",
"Jilin Department of Commerce":"吉林省商务厅",
"Liaoning Department of Civil Affairs":"辽宁省民政厅",
"Liaoning Department of Commerce":"辽宁省商务厅",
"Liaoning Department of Commerce Foreign Investment Office":"辽宁省商务厅外资处",
"Liaoning Disabled Persons’s Federation":"辽宁省残疾人联合会",
"Ministry of Agriculture and Rural Affairs (formerly Ministry of Agriculture)":"农业农村部",
"Ministry of Civil Affairs":"民政部",
"Ministry of Culture and Tourism (formerly China National Tourism Administration)":"文化和旅游部",
"Ministry of Ecology and Environment (formerly Ministry of Environmental Protection)":"生态环境部",
"Ministry of Education":"教育部",
"Ministry of Housing and Urban-Rural Development":"住房和城乡建设部",
"Ministry of Industry and Information Technology":"中华人民共和国工业和信息化部",
"Ministry of Natural Resources (formerly Ministry of Land and Resources)":"自然资源部",
"Ministry of Science and Technology":"科学技术部",
"National Copyright Administration":"国家版权局",
"National Development and Reform Commission":"国家发展和改革委员会",
"National Energy Administration":"国家能源局",
"National Food and Strategic Reserves Administration (formerly State Administration of Grain)":"国家粮食和物资储备局",
"National Forestry and Grassland Administration (formerly State Forestry Administration)":"国家林业和草原局",
"National Health Commission (formerly National Health and Family Planning Commission)":"国家卫生健康委员会",
"National Radio and Television Administration (formerly State Administration of Press, Publication, Radio, Film and Television)":"国家广播电视总局",
"Qinghai Department of Civil Affairs":"青海省民政廳",
"Shaanxi Department of Civil Affairs":"陕西省民政厅",
"Shaanxi Department of Commerce":"陕西省商务厅",
"Shaanxi Department of Education":"陕西省教育厅",
"Shaanxi Federation of Returned Overseas Chinese":"陕西省归国华侨联合会",
"Shaanxi Women’s Federation":"陕西省妇女联合会",
"Shandong Commission of Commerce":"山东省商务厅",
"Shandong Department of Commerce":"山东省商务厅",
"Shandong Department of Science and Technology":"山东省科技厅",
"Shandong Health Commission (formerly Shandong Health and Family Planning Commission)":"山东省卫生健康委员会",
"Shanghai Administration of Culture and Tourism (formerly Shanghai Tourism Administration)":"上海市文化和旅游局",
"Shanghai Bureau of Civil Affairs":"上海市民政局",
"Shanghai Chinese Communist Youth League Committee":"共青团上海市委员会",
"Shanghai Commission of Commerce":"上海市商务委员会",
"Shanghai Commission of Education":"上海市教育委员会",
"Shanghai Commission of Transport":"上海市交通委",
"Shanghai Customs District (formerly Shanghai Entry-Exit Inspection and Quarantine Bureau)":"上海海关",
"Shanghai Health Commission (formerly Shanghai Health and Family Planning Commission)":"上海市卫生健康委员会",
"Shanghai Institutes for International Studies":"上海国际问题研究院",
"Shanghai People’s Association for Friendship with Foreign Countries":"上海市人民对外友好协会",
"Sichuan Department of Civil Affairs":"四川省民政厅",
"Sichuan Department of Commerce":"四川省商务厅",
"Sichuan Department of Culture and Tourism (formerly Sichuan Department of Culture)":"四川省文化和旅游厅",
"Sichuan Department of Education":"四川省教育厅",
"Sichuan Department of Poverty Alleviation and Immigration":"四川省扶贫和移民工作局",
"Sichuan Disabled Person’s Federation":"四川省残疾人联合会",
"Sichuan Forestry and Grassland Administration (formerly Sichuan Forestry Administration)":"四川省林业和草原局",
"Sichuan Health Commission (formerly Sichuan Health and Family Planning Commission)":"四川省卫生健康委员会",
"State Administration of Foreign Experts Affairs (under the Ministry of Science and Technology)":"国家外国专家局",
"State Council Hong Kong and Macau Affairs Office":"国务院港澳事务办公室",
"State Council Leading Group Office of Poverty Alleviation and Development General Affairs Department":"国务院扶贫开发领导小组办公室综合司",
"State Council Overseas Chinese Affairs Office":"国务院侨务办公室",
"State Council Overseas Chinese Affairs Office, Domestic Department":"国务院侨务办公室国内司",
"State Ethnic Affairs Commission":"国家民族事务委员会",
"State Post Bureau":"国家邮政局",
"Tianjin Commission of Commerce":"天津市商务委员会",
"Tianjin Commission of Education":"天津市教育委员会",
"Tianjin Department of Civil Affairs":"天津市民政局",
"Tianjin Federation of Trade Unions":"天津市总工会",
"Yunnan Department of Civil Affairs":"云南省民政厅",
"Yunnan Department of Commerce":"云南省商务厅",
"Yunnan Department of Education":"云南省教育厅",
"Yunnan Forestry and Grassland Administration (formerly Yunnan Forestry Administration)":"云南省林业和草原局",
"Yunnan Health Commission (formerly Yunnan Health and Family Planning Commission)":"云南省卫生健康委员会",
"Yunnan Office of Overseas Chinese Affairs":"云南省人民政府侨务办公室",
"Yunnan Office of Poverty Alleviation and Development":"云南省人民政府扶贫开发办公室",
"Yunnan People’s Association for Friendship with Foreign Countries":"云南省人民对外友好协会",
"Zhejiang Department of Civil Affairs":"浙江省民政厅",
"Zhejiang Department of Commerce":"浙江省商务厅",
"Zhejiang Department of Education":"浙江省教育厅",
"Zhejiang Department of Science and Technology":"浙江省科技厅"
}




#################################################################################
# CLEANING UP CHINESE PSU NAMES, MATCHING THEM TO THE ENGLISH ONES, GETTING #S OF OFFICES SPONSORED #
#################################################################################

# making sure all the PSU names in Chinese are the same (getting rid of the variation in the data) so you can group by both English and Chinese PSU at the same time without any weird artefacts.  Do this using mapping with the massive dictionary above)
# https://michaeljsanders.com/2017/04/17/python-vlookup.html
df_repoff['Professional Supervisory Unit (Chinese)'] = df_repoff["Professional Supervisory Unit (English)"].map(PSU_replace)
# need to do a groupby to get the uniques, but you also have to call some sort of function after the groupby, otherwise you just get a useless object.  so we're also getting the # of offices sponsored.  Resetting the index flattens out the multilevel index that is created by a groupby on 2 columns
PSUs = df_repoff.groupby(["Professional Supervisory Unit (English)", 'Professional Supervisory Unit (Chinese)'])[["Organization Name (English)"]].count().reset_index()
PSUs.rename(columns={"Organization Name (English)": "Number of Foreign NGOs Sponsored"}, inplace = True)
#print (PSUs)




#################################################################################
##### CONCATENATING PERMITTED AREAS OF OPERATION  #######
#################################################################################

# for the next part, we'll eventually be replacing numbers in the AOO and Sector columns with the actual text we want to concatenate later. But first we have to make all the non-zero values in those columns the same in order to do an easy replacement.  Since we want to retain the values for "Number of Foreign NGOs Sponsored" above, I'm making a separate df here, which we'll then map back together at the end
# only bringing in the needed columns to do this  https://stackoverflow.com/a/32751412/7841877
AOOconcat1 = df_repoff.groupby(["Professional Supervisory Unit (English)"])[['ALL OF CHINA', 'Anhui', 'Beijing', 'Chongqing', 'Fujian', 'Gansu', 'Guangdong', 'Guangxi', 'Guizhou', 'Hainan', 'Hebei', 'Heilongjiang', 'Henan', 'Hubei', 'Hunan', 'Inner Mongolia', 'Jiangsu', 'Jiangxi', 'Jilin', 'Liaoning', 'Ningxia', 'Qinghai', 'Shaanxi', 'Shandong', 'Shanghai', 'Shanxi', 'Sichuan', 'Tianjin', 'Tibet', 'Xinjiang', 'Xinjiang Bingtuan', 'Yunnan', 'Zhejiang', 'Unknown']].count()
AOOconcat1.rename(columns={"ALL OF CHINA": "All of China"}, inplace = True)
# https://stackoverflow.com/questions/24021909/pandas-replace-non-zero-values
AOOconcat1[AOOconcat1 != 0] = 1
# https://www.geeksforgeeks.org/python-pandas-series-str-replace-to-replace-text-in-a-series/
AOOconcat1["All of China"] = AOOconcat1["All of China"].replace(1, "All of China")
AOOconcat1["Anhui"] = AOOconcat1["Anhui"].replace(1, "Anhui")
AOOconcat1["Beijing"] = AOOconcat1["Beijing"].replace(1, "Beijing")
AOOconcat1["Chongqing"] = AOOconcat1["Chongqing"].replace(1, "Chongqing")
AOOconcat1["Fujian"] = AOOconcat1["Fujian"].replace(1, "Fujian")
AOOconcat1["Gansu"] = AOOconcat1["Gansu"].replace(1, "Gansu")
AOOconcat1["Guangdong"] = AOOconcat1["Guangdong"].replace(1, "Guangdong")
AOOconcat1["Guangxi"] = AOOconcat1["Guangxi"].replace(1, "Guangxi")
AOOconcat1["Guizhou"] = AOOconcat1["Guizhou"].replace(1, "Guizhou")
AOOconcat1["Hainan"] = AOOconcat1["Hainan"].replace(1, "Hainan")
AOOconcat1["Hebei"] = AOOconcat1["Hebei"].replace(1, "Hebei")
AOOconcat1["Heilongjiang"] = AOOconcat1["Heilongjiang"].replace(1, "Heilongjiang")
AOOconcat1["Henan"] = AOOconcat1["Henan"].replace(1, "Henan")
AOOconcat1["Hubei"] = AOOconcat1["Hubei"].replace(1, "Hubei")
AOOconcat1["Hunan"] = AOOconcat1["Hunan"].replace(1, "Hunan")
AOOconcat1["Inner Mongolia"] = AOOconcat1["Inner Mongolia"].replace(1, "Inner Mongolia")
AOOconcat1["Jiangsu"] = AOOconcat1["Jiangsu"].replace(1, "Jiangsu")
AOOconcat1["Jiangxi"] = AOOconcat1["Jiangxi"].replace(1, "Jiangxi")
AOOconcat1["Jilin"] = AOOconcat1["Jilin"].replace(1, "Jilin")
AOOconcat1["Liaoning"] = AOOconcat1["Liaoning"].replace(1, "Liaoning")
AOOconcat1["Ningxia"] = AOOconcat1["Ningxia"].replace(1, "Ningxia")
AOOconcat1["Qinghai"] = AOOconcat1["Qinghai"].replace(1, "Qinghai")
AOOconcat1["Shaanxi"] = AOOconcat1["Shaanxi"].replace(1, "Shaanxi")
AOOconcat1["Shandong"] = AOOconcat1["Shandong"].replace(1, "Shandong")
AOOconcat1["Shanghai"] = AOOconcat1["Shanghai"].replace(1, "Shanghai")
AOOconcat1["Shanxi"] = AOOconcat1["Shanxi"].replace(1, "Shanxi")
AOOconcat1["Sichuan"] = AOOconcat1["Sichuan"].replace(1, "Sichuan")
AOOconcat1["Tianjin"] = AOOconcat1["Tianjin"].replace(1, "Tianjin")
AOOconcat1["Tibet"] = AOOconcat1["Tibet"].replace(1, "Tibet")
AOOconcat1["Xinjiang"] = AOOconcat1["Xinjiang"].replace(1, "Xinjiang")
AOOconcat1["Xinjiang Bingtuan"] = AOOconcat1["Xinjiang Bingtuan"].replace(1, "Xinjiang Bingtuan")
AOOconcat1["Unknown"] = AOOconcat1["Unknown"].replace(1, "Unknown")
AOOconcat1["Yunnan"] = AOOconcat1["Yunnan"].replace(1, "Yunnan")
AOOconcat1["Zhejiang"] = AOOconcat1["Zhejiang"].replace(1, "Zhejiang")

cols = ['All of China', 'Anhui', 'Beijing', 'Chongqing', 'Fujian', 'Gansu', 'Guangdong', 'Guangxi', 'Guizhou', 'Hainan', 'Hebei', 'Heilongjiang', 'Henan', 'Hubei', 'Hunan', 'Inner Mongolia', 'Jiangsu', 'Jiangxi', 'Jilin', 'Liaoning', 'Ningxia', 'Qinghai', 'Shaanxi', 'Shandong', 'Shanghai', 'Shanxi', 'Sichuan', 'Tianjin', 'Tibet', 'Xinjiang', 'Xinjiang Bingtuan', 'Yunnan', 'Zhejiang', 'Unknown']

AOOconcat1['Sponsored Foreign NGOs’ Permitted Area(s) of Operation'] = AOOconcat1[cols].apply(lambda row: ', '.join(row.values.astype(str)), axis=1)
AOOconcat2 = AOOconcat1.drop(columns=['All of China', 'Anhui', 'Beijing', 'Chongqing', 'Fujian', 'Gansu', 'Guangdong', 'Guangxi', 'Guizhou', 'Hainan', 'Hebei', 'Heilongjiang', 'Henan', 'Hubei', 'Hunan', 'Inner Mongolia', 'Jiangsu', 'Jiangxi', 'Jilin', 'Liaoning', 'Ningxia', 'Qinghai', 'Shaanxi', 'Shandong', 'Shanghai', 'Shanxi', 'Sichuan', 'Tianjin', 'Tibet', 'Xinjiang', 'Xinjiang Bingtuan', 'Yunnan', 'Zhejiang', 'Unknown'])
#print (AOOconcat2)

# for some reason I can't clean up this column in pandas -- i keep getting a "bus error 10" -- so we'll do it later in python




#################################################################################
##### CONCATENATING SECTORS #######
#################################################################################

# just copying the pattern in the section above
sectorconcat = df_repoff.groupby(["Professional Supervisory Unit (English)"])[['Aging', 'Agriculture', 'Animal Protection', 'Arts and Culture', 'Civil Soc\'y Cap\'y building', 'Disabilities', 'Disaster Relief', 'Econ. Development', 'Education', 'Energy', 'Environment', 'Ethnic Affairs', 'Gender Issues', 'Health', 'Human Rights', 'Infrastructure', 'Int\'l Relations/Exchange', 'Labor', 'Law and Governance', 'LGBTQ Issues', 'Media', 'Migrants', 'Poverty Alleviation', 'Religion', 'Rural Issues/Devt', 'Sport', 'Technology', 'Tourism', 'Trade', 'Urban Issues/Devt', 'Youth']].count()

sectorconcat[sectorconcat != 0] = 1

sectorconcat["Aging"]=sectorconcat["Aging"].replace(1, "Aging")
sectorconcat["Agriculture"]=sectorconcat["Agriculture"].replace(1, "Agriculture")
sectorconcat["Animal Protection"]=sectorconcat["Animal Protection"].replace(1, "Animal Protection")
sectorconcat["Arts and Culture"]=sectorconcat["Arts and Culture"].replace(1, "Arts and Culture")
sectorconcat["Civil Soc'y Cap'y building"]=sectorconcat["Civil Soc'y Cap'y building"].replace(1, "Civil Soc'y Cap'y building").replace("Civil Soc'y Cap'y building", "Civil Society Capacity-Building")
sectorconcat["Disabilities"]=sectorconcat["Disabilities"].replace(1, "Disabilities")
sectorconcat["Disaster Relief"]=sectorconcat["Disaster Relief"].replace(1, "Disaster Relief")
sectorconcat["Econ. Development"]=sectorconcat["Econ. Development"].replace(1, "Econ. Development").replace("Econ. Development", "Economic Development")
sectorconcat["Education"]=sectorconcat["Education"].replace(1, "Education")
sectorconcat["Energy"]=sectorconcat["Energy"].replace(1, "Energy")
sectorconcat["Environment"]=sectorconcat["Environment"].replace(1, "Environment")
sectorconcat["Ethnic Affairs"]=sectorconcat["Ethnic Affairs"].replace(1, "Ethnic Affairs")
sectorconcat["Gender Issues"]=sectorconcat["Gender Issues"].replace(1, "Gender Issues")
sectorconcat["Health"]=sectorconcat["Health"].replace(1, "Health")
sectorconcat["Human Rights"]=sectorconcat["Human Rights"].replace(1, "Human Rights")
sectorconcat["Infrastructure"]=sectorconcat["Infrastructure"].replace(1, "Infrastructure")
sectorconcat["Int'l Relations/Exchange"]=sectorconcat["Int'l Relations/Exchange"].replace(1, "Int'l Relations/Exchange").replace("Int'l Relations/Exchange", "International Relations/Exchange")
sectorconcat["Labor"]=sectorconcat["Labor"].replace(1, "Labor")
sectorconcat["Law and Governance"]=sectorconcat["Law and Governance"].replace(1, "Law and Governance")
sectorconcat["LGBTQ Issues"]=sectorconcat["LGBTQ Issues"].replace(1, "LGBTQ Issues")
sectorconcat["Media"]=sectorconcat["Media"].replace(1, "Media")
sectorconcat["Migrants"]=sectorconcat["Migrants"].replace(1, "Migrants")
sectorconcat["Poverty Alleviation"]=sectorconcat["Poverty Alleviation"].replace(1, "Poverty Alleviation")
sectorconcat["Religion"]=sectorconcat["Religion"].replace(1, "Religion")
sectorconcat["Rural Issues/Devt"]=sectorconcat["Rural Issues/Devt"].replace(1, "Rural Issues/Devt").replace("Rural Issues/Devt", "Rural Issues/Development")
sectorconcat["Sport"]=sectorconcat["Sport"].replace(1, "Sport")
sectorconcat["Technology"]=sectorconcat["Technology"].replace(1, "Technology")
sectorconcat["Tourism"]=sectorconcat["Tourism"].replace(1, "Tourism")
sectorconcat["Trade"]=sectorconcat["Trade"].replace(1, "Trade")
sectorconcat["Urban Issues/Devt"]=sectorconcat["Urban Issues/Devt"].replace(1, "Urban Issues/Devt").replace("Urban Issues/Devt", "Urban Issues/Development")
sectorconcat["Youth"]=sectorconcat["Youth"].replace(1, "Youth")

cols1 = ['Aging', 'Agriculture', 'Animal Protection', 'Arts and Culture', 'Civil Soc\'y Cap\'y building', 'Disabilities', 'Disaster Relief', 'Econ. Development', 'Education', 'Energy', 'Environment', 'Ethnic Affairs', 'Gender Issues', 'Health', 'Human Rights', 'Infrastructure', 'Int\'l Relations/Exchange', 'Labor', 'Law and Governance', 'LGBTQ Issues', 'Media', 'Migrants', 'Poverty Alleviation', 'Religion', 'Rural Issues/Devt', 'Sport', 'Technology', 'Tourism', 'Trade', 'Urban Issues/Devt', 'Youth']

sectorconcat['Sponsored Foreign NGOs’ Field(s) of Work'] = sectorconcat[cols1].apply(lambda row: ', '.join(row.values.astype(str)), axis=1)
sectorconcat = sectorconcat.drop(columns=['Aging', 'Agriculture', 'Animal Protection', 'Arts and Culture', 'Civil Soc\'y Cap\'y building', 'Disabilities', 'Disaster Relief', 'Econ. Development', 'Education', 'Energy', 'Environment', 'Ethnic Affairs', 'Gender Issues', 'Health', 'Human Rights', 'Infrastructure', 'Int\'l Relations/Exchange', 'Labor', 'Law and Governance', 'LGBTQ Issues', 'Media', 'Migrants', 'Poverty Alleviation', 'Religion', 'Rural Issues/Devt', 'Sport', 'Technology', 'Tourism', 'Trade', 'Urban Issues/Devt', 'Youth'])
#print (sectorconcat)





#################################################################################
##### CONCATENATING REGISTRATION LOCATIONS #######
#################################################################################

# concatenating values for the sponsored registration locations for each unique PSU. this is done differently from above, which is converting from tick marks to text. below is simply concatenating text that already exists, just smashing text from different rows together. https://stackoverflow.com/questions/41571318/python-pandas-concatenating-multiple-row-values-for-each-index-value
reg_loc_combine = df_repoff.groupby(["Professional Supervisory Unit (English)"])[['Registration Location']].agg(lambda grp: ', '.join(grp.unique()))
# sorting within the resulting concatenated cells to make it alphabetical https://stackoverflow.com/a/55779189/7841877
reg_loc_combine['Registration Location'] = reg_loc_combine['Registration Location'].map(lambda x: ', '.join(sorted(x.split(', '))))
reg_loc_combine.rename(columns={"Registration Location": "Sponsored Foreign NGOs’ Registration Location(s)"}, inplace = True)
#print(reg_loc_combine)





#################################################################################
##### JOINING THE RESULTING 4 DFS #######
#################################################################################

final_df = pd.merge(PSUs, sectorconcat, how='left', left_on='Professional Supervisory Unit (English)', right_on='Professional Supervisory Unit (English)')

final_df = pd.merge(final_df, reg_loc_combine, how='left', left_on='Professional Supervisory Unit (English)', right_on='Professional Supervisory Unit (English)')

final_df = pd.merge(final_df, AOOconcat2, how='left', left_on='Professional Supervisory Unit (English)', right_on='Professional Supervisory Unit (English)')

#print(final_df)





#################################################################################
##### CLEANING UP ALL THE CONCAT MESS IN PYTHON AND MAKING IT HTML-READY #######
#################################################################################

export_csv = final_df.to_csv ('collateral/final_df.csv', header=True, index=False)
list = []
with open('collateral/final_df.csv', 'r') as file_in:
	reader = csv.reader(file_in)
	for row in reader:
		row[3] = row[3].replace(", 0", "").replace("0, ", " ").replace("0", "").strip()
		row[5] = row[5].replace(", 0", "").replace("0, ", " ").replace("0", "").strip()
		list.append(row)
		#print(row)
		#print("")

# https://stackoverflow.com/a/54963455/7841877
html_table = tabulate(list, tablefmt='html', headers="firstrow")
html_table1 = html_table.replace("<table>", "").replace("style=\"text-align: right;\"", "").strip()

fin = open("collateral/PSUtable_input.html", "rt")
fout = open("output/PSUtable.html", "wt")
for line in fin:
	fout.write(line.replace('REPLACE_ME', html_table1))
fin.close()
fout.close()


print("")
print ("You should have a shiny new html file for upload to Github now. Don't forget you have to manually update the heatmap (sorry about that).")
print("")
#RESET IFRAME HEIGHT TO ACCOUNT FOR NEW PSUS
