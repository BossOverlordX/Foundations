import base64
import os

# Create a FastAPI endpoint that accepts a POST request with a JSON body containing a single field called "text" and returns a checksum of the text
# The code should utilise only base64 and os libraries (if at all)
@app.post("/checksum")
async def checksum(text: Text):
    return base64.b64encode(os.urandom(32)).decode("utf-8")