import numpy as np

# from ._drop_all_zero_rows import drop_all_zero_rows
# from ._add_elevation import add_elevation
# from ._add_longitude import add_longitude
from ._cyclic_datetime_julian_date import _cyclic_datetime_julian_date
# from ._calculate_hourly_Rso import calculate_hourly_Rso


def handle_zeros(df, **params):

	how_to_compute_daily_avg = params.get("how_to_compute_daily_avg")
	dropping_cols_strategy = params.get("dropping_cols_strategy")
	verbose = params.get("verbose")
	correlation_method = params.get("correlation_method")
	include_zeros = params.get("include_zeros")
	SolRad_daily = params.get("SolRad_daily")
	Rso_included = params.get("Rso_included")

		
	# df.drop(columns=['Day','Month'], axis=1).to_csv('./FeatureSelection/final_dataset_for_training.csv', index=False)
	# raise ValueError('Created final_dataset_for_training.csv For the feature selction methods, including CatBoost feature\
	# 	importance and different correlation methods')

	# df = add_elevation(df, **params)
	# df = add_longitude(df, **params)

	if SolRad_daily:
		df['SolRad_daily_avg'] = df.iloc[:,2:26].sum(axis=1)/24
		df = df[['StnId','SolRad_daily_avg','ETo_sum_day','Jul']]
		df = _cyclic_datetime_julian_date(df, 'Jul')
		# df = drop_all_zero_rows(df, **params)

	else:
		# df = drop_all_zero_rows(df, **params)

		if include_zeros:
			if how_to_compute_daily_avg == 'without_zeros':
				if Rso_included:
					# df_Rso = calculate_hourly_Rso(df, **params)
					df_Rso[df_Rso == 0] = np.nan
					df_Rso['Rso_daily_avg'] = df_Rso.mean(axis=1)

					for col in df_Rso.columns:		
						df_Rso[col].fillna(df_Rso['Rso_daily_avg'], inplace=True)

					df_Rso.drop(columns=['Rso_daily_avg'], axis=1, inplace=True)

				else:
					df[df.drop(columns=['StnId','ETo_sum_day','Jul'], axis=1) == 0] = np.nan
					df['SolRad_daily_avg'] = df.drop(columns=['StnId','ETo_sum_day','Jul'], axis=1).mean(axis=1)


			# elif how_to_compute_daily_avg == 'with_zeros':
			# 	df['SolRad_daily_avg'] = df.iloc[:, 1:25].mean(axis=1)
			# 	df[df.drop(columns=['StnId','ETo_sum_day'], axis=1) == 0] = np.nan


			for col in df.columns:		
				df[col].fillna(df['SolRad_daily_avg'], inplace=True)


			df.drop(columns=['SolRad_daily_avg'], axis=1, inplace=True)

		
		else:

			if dropping_cols_strategy=='feature_importance':

		  		#Keep Features with highest Feature Importance:
		  		df.drop(columns=['100','200','300','400','500','1100',
					'1300','1400','1500','1600','1700','1800',
					'1900','2000','2100','2200','2300','2400'],
					axis=1, inplace=True)	
		  		df.dropna(axis=0, inplace=True, 
		  			subset=[ '600', '700', '800',
		  			'900', '1000', '1200','ETo_sum_day'])
				

			elif dropping_cols_strategy=='correlation':

	  			#Keep Features with highest correlation with ETo_sum_day
				if correlation_method == 'pearson_':
					df.drop(columns=['100','200','300','400','500','600',
			                 '700','1400','1500','1600','1700','1800',
			                 '1900','2000','2100','2200','2300','2400'],
			                  axis=1, inplace=True)
					df.dropna(axis=0, inplace=True,
						subset=['800','900','1000','1100','1200','1300','ETo_sum_day'])

				elif correlation_method == 'mutual_info':
					df.drop(columns=['100','200','300','400','500',
			                 '600','700','1400','1500','1600','1700','1800',
			                 '1900','2000','2100','2200','2300','2400'],
			                  axis=1, inplace=True)
					df.dropna(axis=0, inplace=True,
						subset=['800','900','1000','1100','1200','1300','ETo_sum_day'])

				elif correlation_method == 'spearman_':
					df.drop(columns=['100','200','300','400','500','600',
			                 '1300','1400','1500','1600','1700','1800',
			                 '1900','2000','2100','2200','2300','2400'],
			                  axis=1, inplace=True)
					df.dropna(axis=0, inplace=True,
						subset=['700','800','900','1000','1100','1200','ETo_sum_day'])


	return df