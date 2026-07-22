from pydantic import BaseModel


class Settings(BaseModel):
    project_name: str = "Axitwo API"
    api_v1_prefix: str = "/api/v1"


settings = Settings()
