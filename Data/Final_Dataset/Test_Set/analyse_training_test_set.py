
def add_zone(df):

	df['Zone'] = ''

	# Create a dictionary for mapping
	value_map = {
1:	12,
2:	16,
3:	2,
4:	3,
5:	15,
6:	14,
7:	15,
8:	14,
9:	15,
10:	15,
11:	15,
12:	12,
13:	13,
14:	12,
15:	16,
16:	2,
17:	18,
18:	18,
19:	2,
20:	16,
21:	16,
22:	16,
23:	12,
24:	18,
25:	18,
26:	15,
27:	12,
28:	6,
29:	15,
30:	12,
31:	15,
32:	12,
33:	12,
34:	6,
35:	14,
36:	18,
37:	6,
38:	3,
39:	12,
40:	15,
41:	18,
42:	12,
43:	7,
44:	6,
45:	3,
46:	7,
47:	14,
48:	7,
49:	3,
50:	18,
51:	8,
52:	6,
53:	12,
54:	16,
55:	16,
56:	15,
57:	13,
58:	9,
59:	14,
60:	17,
61:	12,
62:	6,
63:	5,
64:	6,
65:	8,
66:	3,
67:	3,
68:	18,
69:	8,
70:	12,
71:	14,
72:	16,
73:	9,
74:	9,
75:	6,
76:	3,
77:	8,
78:	9,
79:	8,
80:	12,
81:	13,
82:	9,
83:	5,
84:	14,
85:	8,
86:	12,
87:	18,
88:	10,
89:	6,
90:	7,
91:	7,
92:	15,
93:	15,
94:	3,
95:	2,
96:	8,
97:	3,
98:	9,
99:	3,
100:	6,
101:	9,
102:	3,
103:	5,
104:	2,
105:	15,
106:	8,
107:	3,
108:	14,
109:	5,
110:	17,
111:	2,
112:	12,
113:	12,
114:	12,
115:	6,
116:	2,
117:	17,
118:	18,
119:	14,
120:	3,
121:	14,
122:	14,
123:	8,
124:	15,
125:	15,
126:	10,
127:	18,
128:	18,
129:	2,
130:	6,
131:	14,
132:	8,
133:	9,
134:	17,
135:	18,
136:	18,
137:	6,
138:	15,
139:	14,
140:	14,
141:	18,
142:	12,
143:	3,
144: 5,
145:	12,
146:	15,
147:	9,
148:	12,
149:	1,
150:	6,
151:	18,
152: 9,
153: 9,
154: 18,
155:	14,
156:	3,
157:	5,
158:	5,
159:	9,
160:	6,
161:	14,
162:	18,
163:	6,
164:	8,
165:	6,
166:	12,
167:	14,
168:	12,
169:	12,
170:	8,
171:	6,
172:	16,
173:	1,
174:	3,
175:	16,
176:	18,
177:	2,
178:	8,
179:	6,
180:	18,
181:	18,
182:	15,
183:	14,
184:	3,
185:	18,
186:	18,
187:	5,
188:	12,
189:	14,
190:	16,
191:	8,
192:	14,
193:	2,
194:	12,
195:	14,
196:	14,
197:	17,
198:	9,
199:	14,
200:	18,
201:	18,
202:	3,
203:	16,
204:	14,
205:	10,
206:	12,
207:	18,
208:	18,
209:	2,
210:	6,
211:	8,
212:	14,
213:	2,
214:	6,
215:	9,
216:	9,
217:	9,
218:	18,
219:	9,
220:	17,
221:	17,
222:	14,
223:	9,
224:	14,
225:	13,
226:	14,
227:	13,
228:	13,
229:	3,
230:	3,
231:	3,
232:	3,
233:	17,
234:	17,
235:	12,
236:	7,
237:	6,
238:	6,
239:	6,
240:	6,
241:	3,
242:	14,
243:	14,
244:	12,
245:	6,
246:	11,
247:	14,
248:	12,
249:	14,
250:	12,
251:	9,
252:	6,
253:	1,
254:	1,
255:	9,
256:	17,
257:	17,
258:	12,
259:	1,
260:	10,
261:	10,
262:	12,
263:	1,
264:	13
	}

	# Assign values based on dictionary mapping
	df['Zone'] = df['StnId'].map(value_map)

	return df



###################################################################
# Plot Outlier Percentage in training and test set


# # Specify the path to your Excel file
# excel_file_path = 'final_dataset_train_discussion.csv'

# # Read the Excel file into a DataFrame
# data = pd.read_csv(excel_file_path)

# data = add_zone(data)

# # Assuming your dataset is stored in a DataFrame named 'data'
# outlier_threshold = 1.5  # Define your outlier threshold here

# # Step 1: Calculate outliers
# q1 = data['ETo_sum_day'].quantile(0.25)
# q3 = data['ETo_sum_day'].quantile(0.75)
# iqr = q3 - q1
# lower_bound = q1 - outlier_threshold * iqr
# upper_bound = q3 + outlier_threshold * iqr
# outliers = data[(data['ETo_sum_day'] < lower_bound) | (data['ETo_sum_day'] > upper_bound)]

# # Step 2: Group data by Zone
# grouped_data = outliers.groupby('Zone')

# # Step 3: Count outliers per zone
# outlier_counts = grouped_data.size()

# # Step 4: Calculate percentage of outliers
# total_counts = data['Zone'].value_counts()
# outlier_percentages = (outlier_counts / total_counts) * 100

# # Set the desired height and width of the figure
# fig_width = 3  # in inches
# fig_height = 3  # in inches

# # Step 5: Visualize the results
# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.size'] = 7

# fig, ax = plt.subplots(figsize=(fig_width, fig_height))

# outlier_percentages.plot(kind='bar', ax=ax)
# ax.set_xlabel('Zone')
# ax.set_ylabel('Percentage of Outliers')

# # Adjust x tick labels
# ax.tick_params(axis='x', rotation=0)

# plt.savefig('Outlier_Percentage_Train.jpg', format='jpg', dpi=600)
# plt.show()



##################################################################
# # Plot ETo distribution in training and test set
# import matplotlib.pyplot as plt
# import pandas as pd
# import matplotlib.font_manager as fm

# # Specify the path to your Excel file
# excel_file_path = 'final_dataset_train_discussion.csv'

# # Read the Excel file into a DataFrame
# df = pd.read_csv(excel_file_path)

# df = add_zone(df)

# # Sort the unique zone values in numerical order
# unique_zones = sorted(df['Zone'].unique())

# # Set the font to Times New Roman
# font_path = 'C:/Windows/Fonts/times.ttf'
# font_prop = fm.FontProperties(fname=font_path)

# # Set the default font family for the plot
# plt.rcParams['font.family'] = font_prop.get_name()

# # Create a subplot grid to plot each distribution separately
# fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(16, 16))
# axes = axes.flatten()

# # Iterate over the unique zone values and plot the ETo distribution for each zone
# for i, zone in enumerate(unique_zones):
#     if i < len(axes):  # Check if there are more subplots available
#         ax = axes[i]  # Get the corresponding subplot
#         zone_data = df[df['Zone'] == zone]['ETo_sum_day']  # Filter data for the current zone
#         ax.hist(zone_data, bins=20)  # Plot the histogram of ETo values
#         ax.set_title(f"Zone {zone}", fontsize=15)  # Set the title for the subplot

#         # Set the font properties for x-ticks and y-ticks
#         ax.tick_params(axis='x', labelsize=15)
#         ax.tick_params(axis='y', labelsize=15)

# plt.tight_layout()  # Adjust spacing between subplots
# plt.subplots_adjust(hspace=0.5)  # Adjust vertical spacing between subplots
# plt.savefig('ETo_Distribution_Each_Zone_Train.jpg', format='jpg', dpi=600)
# plt.show()  # Show the plot


###################################################################
# # Plot correlation between Daily SolRad and ETo in each zone in the training and test set
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import font_manager

# # Specify the path to your CSV file
# csv_file_path = 'final_dataset_train_discussion.csv'

# # Read the CSV file into a DataFrame
# df = pd.read_csv(csv_file_path)
# df = add_zone(df)

# # Calculate the sum of columns 3 to 27 for each zone
# df['SolRad_daily_avg'] = df.iloc[:, 2:26].sum(axis=1) / 24
# selected_columns = ['SolRad_daily_avg', 'Zone', 'ETo_sum_day']
# df = df[selected_columns]

# correlations = df.groupby('Zone')[['SolRad_daily_avg', 'ETo_sum_day']].corr(method='spearman').iloc[0::2, -1].values

# # Get unique Zone values and sort them in ascending order
# zones = sorted(df['Zone'].unique())

# # Set figure size
# plt.figure(figsize=(2.7, 2.7))

# # Set font properties for all text elements
# font_properties = font_manager.FontProperties(family='Times New Roman', size=5)

# # Plot correlation values as markers
# plt.plot(zones, correlations, marker='o', linestyle='-', color='b', linewidth=0.5, markersize=2)

# # Connect the points with lines
# for i in range(len(zones)-1):
#     plt.plot([zones[i], zones[i+1]], [correlations[i], correlations[i+1]], linestyle='-', color='b', linewidth=0.5)

# # Set x-tick labels as unique Zone values
# plt.xticks(zones, zones, fontproperties=font_properties)


# # Set labels and title with font properties
# plt.xlabel('Zone', fontproperties=font_properties, fontsize=8)
# plt.ylabel('Correlation', fontproperties=font_properties, fontsize=8)

# # Set y-axis ticks from 0.9 to 0.99
# plt.yticks([0.9, 0.92, 0.94, 0.96, 0.98], fontproperties=font_properties)

# # Set the border linewidth to 0.5
# plt.gca().spines['top'].set_linewidth(0.5)
# plt.gca().spines['bottom'].set_linewidth(0.5)
# plt.gca().spines['left'].set_linewidth(0.5)
# plt.gca().spines['right'].set_linewidth(0.5)

# # Set the tick linewidth to 0.5
# plt.gca().tick_params(width=0.5)

# # Save the plot as a high-resolution image
# plt.savefig('Correlations_between_Rs_and_ETo_Train.jpg', format='jpg', dpi=600)

# # Display the plot
# plt.show()

###############################
# Eliminating records with ETo values higher than 15 or ETo's 99th percentile

# import pandas as pd
# csv_file_path = 'final_dataset_train_discussion.csv'
# df = pd.read_csv(csv_file_path)
# quantile_99 = df['ETo_sum_day'].quantile(0.99)

# print(df.shape)

# df = df[df['ETo_sum_day'] <= quantile_99]
# print(df.shape)

#############################################
# Dropping null values

# import pandas as pd
# csv_file_path = 'final_dataset_test_discussion.csv'
# df = pd.read_csv(csv_file_path)

# print(df.shape)
# df.dropna(inplace=True,how='any')

# print(df.shape)

########################################


