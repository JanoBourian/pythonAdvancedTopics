import json

class GeneralResponse:
    def __init__(self, data = None, status_code = 200, ierror = 0, cerror = "Process was executed correctly", is_base64encode = False, headers = {"Content-Type": "application/json"}):
        self.data = data
        self.status_code = status_code
        self.ierror = ierror 
        self.cerror = cerror
        self.is_base64encode = is_base64encode
        self.headers = headers 

class SuccessResponse(GeneralResponse):
    
    def __init__(self, data = None, status_code = 200, ierror = 0, cerror = "Process was executed correctly", is_base64encode = False, headers = {"Content-Type": "application/json"}):
        super().__init__(data, status_code, ierror, cerror, is_base64encode, headers)
    
    def final_response(self):
        return {
            "body": {
                "response":{
                    "data": json.dumps(self.data),
                    "ierror": self.ierror,
                    "cerror": self.cerror,
                }
            },
            "statusCode": self.status_code,
            "isBase64Encoded": json.dumps(self.is_base64encode),
            "headers": self.headers
        }

class ErrorResponse(GeneralResponse):
    def __init__(
        self,
        data=None,
        status_code=500,
        ierror=1,
        cerror="Process was not executed correctly",
        is_base64encode=False,
        headers={"Content-Type": "application/json"},
    ):
        super().__init__(data, status_code, ierror, cerror, is_base64encode, headers)

    def final_response(self):
        return {
            "body": {
                "response": {
                    "data": json.dumps(self.data),
                    "ierror": self.ierror,
                    "cerror": self.cerror,
                }
            },
            "statusCode": self.status_code,
            "isBase64Encoded": json.dumps(self.is_base64encode),
            "headers": self.headers,
        }
        
r = ErrorResponse(status_code=500)
print(r.final_response())

r = SuccessResponse()
print(r.final_response())