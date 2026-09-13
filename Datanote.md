# PROJECT BREIF
How much has the built-up area of Lagelu and Ibadan North expanded since 2020?
Study area is Lagelu and Ibadan North LGAs, Ibadan, Oyo State.

A study on how much the built-up area of Lagelu and Ibadan North has expanded since 2020 is important because it provides evidence of the pace and pattern of urban growth in one of Nigeria's rapidly developing regions. Measuring built-up area changes since 2020 offers valuable insights into recent development trends, supports future growth projections, and contributes to achieving sustainable urban management goals in Lagelu and Ibadan North. Such information is essential for balancing economic development with environmental conservation and ensuring that urban expansion occurs in an efficient and resilient manner.

## The data needed:
Nigeria State Boundary Level Data
Nigeria LGA Level Data
Nigeria Ward Level Data
Nigeria Settlement Data
Nigeria Road Data: OSM plugin in QGIS


I.	Nigeria Ward Level Data: [GRID3 NGA – Operational Wards v3.0 (July 2026) – 128mb](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v3-0/about) (States included: Abia, Adamawa, Bauchi, Bayelsa, Borno, Delta, Enugu, FCT Abuja, Gombe, Jigawa, Kaduna, Kano, Katsina, Kebbi, Kogi, Kwara, Nasarawa, Niger, Ogun, Osun, Oyo, Sokoto, Yobe, and Zamfara)
•	Geometry – 5872
•	Key columns – globalid, uniq_id, statename, lganame, lgacode, statecode, wardname
•	Geometry types – Layer
•	Comments – None

II.	Nigeria LGA Level Data: [GRID3 NGA – Operational LGA Boundaries (December 2020) – 2.6mb](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about)
•	Geometry – 774
•	Key columns – globalid, uniq_id, statename, lganame, lgacode, statecode
•	Geometry types – Layer
•	Comments – None

III.	Nigeria State Boundary Data: [GRID3 NGA – Operational State Boundaries (December 2020) – 645kb](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-state-boundaries-/about)
•	Geometry – 37
•	Key columns – globalid, uniq_id, statename
•	Geometry types – Layer
•	Comments – None


IV.	Nigeria Settlement Data: [GRID3 NGA – Settlement Extents v4.1 (August 2026)](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about) - 
[GRID3 NGA – Settlement Names (September 2020) – 29.1mb](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-names/about)
•	Geometry – 2,546,560
•	Key columns – block_id, country, block_area_sqm, block_perimeter, building_count, extent_type and others
•	Geometry types – Layer
•	Comments –  None

V.	Nigeria Road Data: OSM plugin in QGIS

Ward Level: Admin 3\n
LGA level: Admin 2\n
State level: Admin 1\n

## What would I build:
An Interactive map of Lagelu and Ibadan North LGA, Ibadan, Oyo state that shows the settlement extent and urbanization trend from 2020 till present. The map would be updated monthly or as new data becomes available and can be used by any interested users.
