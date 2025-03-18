import xarray as xr

# 打开NetCDF文件
file_path = '2025-01\TJ_ENSO_2025_01.nc'
ds = xr.open_dataset(file_path)

# 打印数据集的信息
print(ds['nino34_mean'].values)

# 访问变量
#print(ds.variables)

# 关闭数据集（xarray会自动管理资源，但显式关闭是个好习惯）
ds.close()