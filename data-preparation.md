# Data preparation

**Week 3 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Adegboye Okikioluwa

What I reprojected, what I clipped, what I checked, and what I fixed.

---

## 1. Coordinate system decisions

**Working CRS:** <EPSG:32631>

**Why this one:** <This data was selected for measuring distance or
area, and the EPSG:32631 CRS chosen is in metres.>

| Dataset | CRS as downloaded | CRS after | Operation |
|---|---|---|---|
| <NGA_LGA_Boundaries_2_2609687066015738692.zip> | EPSG:4326 | EPSG:32631 | Reprojected |
| <Settlements_in_Nigeria_5337296628765511226.zip> | EPSG:4326 | EPSG:32631 | Reprojected |

> I reprojected both data imported to get the correct CRS of UTM31.

## 2. Clipping to the study area

- **Ibadan North and Lagelu LGA Boundary:** <source - OpenStreetMap and file - `Data/Processed/Roads_in_Lagelu_Ibadan_North_LGA.gpkg`>
- **Features before clipping:** <29684>
- **Features after clipping:** <12414>

<Features outside the study area boundary were removed.>

## 3. The five quality checks

| Check | Result | Action taken |
|---|---|---|
| Is the CRS what I think it is? | <yes> | <I reprojected to the correct CRS> |
| Are there nulls in the fields I need? | <yes> | <flagged the data> |
| Are there duplicate features? | <no> | <none> |
| Is the geometry valid? | <yes> | <None> |
| Does coverage span the whole study area? | <yes> | <verified with boundary data> |

## 4. Problems found, and what I did

**<Problem.>** <Some of the road data were not properly labelled with a name or given surface type or other attributes, data was only flagged.>

## 5. The analysis-ready output

- **File:** `Data/Processed/Lagelu_Ibadan_North_LGA_utm31.gpkg`
- **Format:** GeoPackage
- **CRS:** <EPSG:32631>
- **Features:** <2>
- **Produced by:** <manually in QGIS>

- **File:** `Data/Processed/Roads_in_Lagelu_Ibadan_North_LGA.gpkg`
- **Format:** GeoPackage
- **CRS:** <EPSG:32631>
- **Features:** <12414>
- **Produced by:** <manually in QGIS>

- **File:** `Data/Processed/utm31_Settlement_Names_IB_North_Lagelu_LGA.gpkg`
- **Format:** GeoPackage
- **CRS:** <EPSG:32631>
- **Features:** <527>
- **Produced by:** <manually in QGIS>

---

**Status:** Week 3 complete. First spatial analysis in Week 4.
