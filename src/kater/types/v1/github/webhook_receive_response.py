# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["WebhookReceiveResponse"]


class WebhookReceiveResponse(BaseModel):
    """Response for successful webhook receipt."""

    delivery_id: str

    event_type: str

    received: bool

    message: Optional[str] = None

    processed: Optional[bool] = None
