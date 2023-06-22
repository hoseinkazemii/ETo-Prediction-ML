import math

from ._replace_night_Rso_by_zero import replace_night_Rso_by_zero


def calculate_hourly_Rso(df, **params):

	verbose = params.get("verbose")

	if verbose:
		print("Claculating hourly Rso...")

	Gsc = 0.082
	sigma = 2.04*pow(10,-10)
	
	for t in range(1, 25):

		Rso_lst = []

		for i in df.index:

			latitude = df.loc[i,'Latitude']
			longitude = df.loc[i,'Longitude']
			elevation = df.loc[i,'Elevation']
			J = df.loc[i,'Jul']


			phi = math.pi*latitude/180
			dr = 1+0.033*math.cos((2*math.pi*J)/365)
			delta = 0.409*math.sin(((2*math.pi*J)/365)-1.39)
			b = 2*math.pi*(J-81)/364
			Sc = 0.1645*math.sin(2*b)-0.1255*math.cos(b)-0.025*math.sin(b)
			omega_s = math.acos(-math.tan(phi)*math.tan(delta))
			omega = (math.pi/12)*(t+(120-longitude)/15-12+Sc)
			omega_1 = omega-0.5*math.pi/12
			omega_2 = omega+0.5*math.pi/12
			sin_tetha = (omega_2-omega_1)*math.sin(phi)*\
				math.sin(delta)+math.cos(phi)*math.cos(delta)*(math.sin(omega_2)-math.sin(omega_1))
			if (omega < -omega_s) or (omega > omega_s):
				Ra = 0
			else:
				Ra = (12/math.pi)*60*Gsc*dr*sin_tetha				
			Rso = 2500/9 * Ra * (0.75 + 2*pow(10, -5)*elevation)
			Rso_lst.append(Rso)

		df[f'Rso_{t}'] = Rso_lst

	# df = replace_night_Rso_by_zero(df, **params)
		
	df.drop(columns=['Latitude','Elevation','Longitude'], axis=1, inplace=True)

	column_names = ['Rso_{}'.format(i) for i in range(1, 25)]
	df_Rso = df.loc[:, column_names]

	return df_Rso