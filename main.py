from transform import  Transformer
from utils.logger import logger

def main(request):
    data = request.get_json()
    Transformer(data["articles"]).transform()
    logger.info("Data Transformation Completed")




