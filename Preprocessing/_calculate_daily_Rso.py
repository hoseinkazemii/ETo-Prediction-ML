import math

from ._replace_unusual_Rs import replace_unusual_Rs


def calculate_daily_Rso(df, **params):

	SolRad_daily = params.get("SolRad_daily")
	verbose = params.get("verbose")

		
	if verbose:
		print("Calculating daily Rso...")

	if SolRad_daily:

		Rso_lst = []

		Gsc = 0.082

		for i in df.index:
			
			latitude = df.loc[i,'Latitude']
			elevation = df.loc[i,'Elevation']
			phi = (latitude*math.pi)/180
			J = df.loc[i,'Jul']

			dr = 1+0.033*math.cos((2*math.pi*J)/365)
			delta = 0.409*math.sin(((2*math.pi*J)/365)-1.39)			
			omega = math.acos(-math.tan(phi)*math.tan(delta))
			Ra = (omega*math.sin(phi)*math.sin(delta)+math.cos(phi)*math.cos(delta)*math.sin(omega))*24*60*Gsc*dr/math.pi

			Rso = 625/54 * Ra * (0.75 + 2*pow(10, -5)*elevation)
			Rso_lst.append(Rso)

		df['Rso'] = Rso_lst

		df.drop(columns=['Latitude','Elevation'], axis=1, inplace=True)

	# df = replace_unusual_Rs(df, **params)