cities = {'zacatecas':{'population': 1000000,
					   'country': 'mexico',
					   'fact':'la nufa',
					  },
		  'buenos aires':{'population': 7000000,
		  				  'country':'argentina',
		  				  'fact':'martu morales'	
		  				 },
		  'los angeles':{'population':340000000,
		  				 'country': 'united states',
		  				 'fact':'punto com companies',
		  				},
		  }

for city,info in cities.items():
	print(f"\n{city.title()} information:")

	for key, value in info.items():
		print(f"\t{key} : {value}")
	