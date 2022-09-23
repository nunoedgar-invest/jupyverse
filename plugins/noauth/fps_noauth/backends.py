from typing import Any, Dict, List, Optional, Tuple

from fastapi import Depends, WebSocket

from .models import BaseUser


def current_user(*args, **kwargs):
    async def _():
        pass

    return _


def websocket_auth(permissions: Optional[Dict[str, List[str]]] = None):
    """
    A function returning a dependency for the WebSocket connection.

    :param permissions: the permissions the user should be granted access to. The user should have
    access to at least one of them for the WebSocket to be opened.
    :returns: a dependency for the WebSocket connection. The dependency returns a tuple consisting
    of the websocket and the checked user permissions if the websocket is accepted, None otherwise.
    """

    async def _(
        websocket: WebSocket,
    ) -> Optional[Tuple[WebSocket, Optional[Dict[str, List[str]]]]]:
        return websocket, permissions

    return _


async def update_user(user: BaseUser = Depends(current_user())):
    async def _(data: Dict[str, Any]) -> BaseUser:
        return user

    return _
