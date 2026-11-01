# Free cement kiln specific-heat-consumption shift tracker (2026)

**Publisher:** Infinity for Cement Organization, cementequipment.org. Original single-sheet CSV worksheet with 31 blank shift rows. No third-party manuals or copyrighted files included.

**Public page:** https://www.cementequipment.org/home/reducing-heat-consumption-in-preheater-and-calciner-the-right-technology-process-combination/

## What it does

This CSV opens in Microsoft Excel, LibreOffice Calc, or another formula-compatible spreadsheet program. Enter one comparable operating period per row. The three formula columns calculate fuel energy input (MJ), specific heat consumption (MJ per tonne clinker) and the equivalent (kcal per kg clinker).

**Required fields:** clinker output in tonnes, and for every fuel used during the same period, fuel mass in kg and its net calorific value (NCV/LHV) in MJ/kg. Leave unused fuels at zero or blank. Do not use HHV/GCV in NCV columns. Use the same clinker and fuel measurement period. The worksheet returns blank output for missing production or fuel; it displays CHECK NCV if a fuel mass is present without its heating value. The workbook does not independently validate process-meter calibration, quality, fuel moisture or alternative-fuel composition.

**Formula:** total thermal input [MJ] = Σ fuel mass [kg] × net calorific value [MJ/kg]. SHC [MJ/t clinker] = thermal input [MJ] ÷ clinker produced [t]. SHC [kcal/kg clinker] = SHC [MJ/t] ÷ 4.184. This is a screening-level *fuel-based* specific heat metric, not a closed process energy balance; no corrected heat losses, clinker chemistry, indirect electricity, waste heat recovery or emissions are inferred.

## Use safely

- No plant operating decisions should be based solely on this worksheet. Reconcile certified meter data and plant-specific OEM operating procedures.
- The sheet intentionally ships with blank measurement cells; it does not claim any typical efficiency, guaranteed fuel saving, or plant performance.
- CSV is text without formatting or macros; Excel may display a file-format warning, and spreadsheet software may use local separator conventions.
- If the formula appears as text, adjust the spreadsheet import locale and formula separator. Do not enable macros; none are required.

For the verified inventory of additional existing spreadsheet references: https://www.cementequipment.org/cement-plant-excel-calculation-toolkit/

© 2026 Infinity for Cement Organization. Permission granted to download, use and adapt **this original free template** for internal engineering analysis, with attribution. No warranty; validate locally.
