import os




class Settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")


settings = Settings()