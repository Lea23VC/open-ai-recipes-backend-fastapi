from mangum import Mangum
from main import app

# Mangum allow us to use fastapi with lambdas using Api Gateway service
handler = Mangum(app)
