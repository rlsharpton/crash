rivers = {
    'nile': {'country': 'Egypt',
          'length': 'Longest',
          'continet': 'Africa',
          'color': 'blue',
          },
    'amazon': {'country': 'Brazil',
          'length': 'Second',
          'continet': 'S. America',
          'color': 'green',},
    'mississippi': {'country': 'USA',
          'length': 'Third',
          'continet': 'N America',
          'color': 'brown',},
    'yellow': {'country': 'China',
          'length': 'Fourth',
          'continet': 'Asia',
          'color': 'yellow',}
}

print(rivers)

for river, river_details in rivers.items():
    print("\nRiver:" + river)
    print("Length:" + river_details['length'])
    print("Continent:" + river_details['continet'])