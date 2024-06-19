# import json
# import hmac
# import requests
# from hashlib import sha256
# from calendar import timegm
# from datetime import datetime


# def _get_x_pay_token(shared_secret, resource_path, query_string, body):
#     timestamp = str(timegm(datetime.utcnow().timetuple()))
#     pre_hash_string = timestamp + resource_path + query_string + json.dumps(body)
#     hash_string = hmac.new(
#         shared_secret, msg=pre_hash_string.encode("utf-8"), digestmod=sha256
#     ).hexdigest()
#     return "xv2:" + timestamp + ":" + hash_string


# shared_secret = b"{{mySharedSecret}}"
# resource_path = "authorizations"
# query_string = "apiKey={{myaApi}}"
# body = {
#     # ... (Your JSON data here)
# }
# print(json.dumps(body, indent=2))

# x_pay_token = _get_x_pay_token(shared_secret, resource_path, query_string, body)

# headers = {
#     "X-PAY-TOKEN": x_pay_token,
#     "Accept": "application/json",
#     "Content-Type": "application/json",
# }
# url = "https://sandbox.api.visa.com/acs/v3/payments/authorizations?apiKey={{myaApi}}"
# r = requests.post(url, headers=headers, json=body)

# print(r.content)

# template = loader.get_template("checkout/sdk.html")

# context = {
#     "code": r.content,
# }

#     return HttpResponse(template.render(context, request))
