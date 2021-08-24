import requests
import json

url = "http://120.236.164.111:9090/ydzf/api/controller/xzcf/zyclController/addOrUpdate"
headers = {"Content-Type": "application/json",
           "cookie": "ydzf_token=mrjvcb4EKAfdDLYNgItphUBb2HdbmuSCTEpnwSprie6pdraH44hlZcbmP3huYhKsp3zkLDqCKcPn_eEdhV4r8PPv5mRP5Mrhd6pZjvbnCuN4reduR-jTDNpOY3WUjQINjJpZQTyHJR88DAL1AKY9UztcZFWZF9JVmMOD3ufZkxSF4-CKUAzBfwCINzKZ56AXMY5uevKP0CSU9ncNrIx7SBczPaSFJDekXCWMrAvHcYrVdrzpymCmC-ah0HcmzdKPZuEJ4U5LUfABvpgDX4KVmApIU5Yp7n-LmSNy1740DDTXS2zCS8hWOmMTlJBJ1dP-2PXDxq-oFpTlj3gVc69eTqkJjGr5B8aQk9qSDafhl3VhEYJDcFtCsbacDO3wfyWi56-ykNEBC6SdcGUiLT9e5w==; path=/; httponly"}
data = {"baseInfor": {"BENCHMARK_TYPE": 3, "ILLEGAL_TYPE": 2, "FACTOR_TYPE": 2, "FACTOR": "12312", "LEVEL": "99"}}
result = requests.post(url=url, headers=headers, data=data)
print(result.text)