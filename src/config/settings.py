import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, AliasChoices, model_validator



class Settings(BaseSettings):
    groq_api_key: str =Field(validation_alias=AliasChoices("GROQ_API_KEY", "groq_api_key"),
                                default="")
    tavily_api_key: str =Field(validation_alias=AliasChoices("TAVILY_API_KEY", "tavily_api_key"),
                                default="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")
    db_user : str = Field(default="postgres", validation_alias=AliasChoices("DB_USER", "db_user"))
    db_password : str = Field(default="postgres", validation_alias=AliasChoices("DB_PASSWORD", "db_password"))
    db_host : str = Field(default="localhost", validation_alias=AliasChoices("DB_HOST", "db_host"))
    db_port : int = Field(default=5432, validation_alias=AliasChoices("DB_PORT", "db_port"))
    db_name : str = Field(default="graphql", validation_alias=AliasChoices("DB_NAME", "db_name"))

    database_url:str = Field(
        default="postgresql://postgres:postgres@localhost:5432/ ",
        validation_alias=AliasChoices("DATABASE_URL", "database_url")
    )
    @model_validator(mode="after")
    def construct_db_url(self):
        if not self.database_url:
            self.database_url = (
                f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
            )
        return self


    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


    



settings = Settings()