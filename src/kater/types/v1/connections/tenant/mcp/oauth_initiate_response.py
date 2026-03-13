# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ......_models import BaseModel

__all__ = ["OAuthInitiateResponse"]


class OAuthInitiateResponse(BaseModel):
    """Response model containing the OAuth authorization URL for the frontend."""

    authorize_url: str
