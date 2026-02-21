"""
FastAPI default applications.
"""

from typing import Any, Dict, List, Optional, Sequence, Tuple, Type, Union

from fastapi import routing
from fastapi.datastructures import Default, DefaultPlaceholder
from fastapi.encoders import DictIntStrAny, SetIntStr
from fastapi.responses import JSONResponse, Response
from fastapi.types import ASGIApp
from fastapi.utils import generate_unique_id


class FastAPI:
    """
    FastAPI application class.
    """

    def __init__(
        self,
        *,
        debug: bool = False,
        routes: Optional[List[routing.BaseRoute]] = None,
        title: str = "FastAPI",
        description: str = "",
        version: str = "0.1.0",
        openapi_url: Optional[str] = "/openapi.json",
        openapi_tags: Optional[List[Dict[str, Any]]] = None,
        servers: Optional[List[Dict[str, Union[str, Any]]]] = None,
        default_response_class: Type[Response] = Default(JSONResponse),
        docs_url: Optional[str] = "/docs",
        redoc_url: Optional[str] = "/redoc",
        swagger_ui_oauth2_redirect_url: Optional[str] = None,
        swagger_ui_init_oauth: Optional[Dict[str, Any]] = None,
        middleware: Optional[Sequence[Any]] = None,
        exception_handlers: Optional[Dict[Union[int, Type[Exception]], Any]] = None,
        on_startup: Optional[Sequence[Callable[[], Any]]] = None,
        on_shutdown: Optional[Sequence[Callable[[], Any]]] = None,
        terms_of_service: Optional[str] = None,
        contact: Optional[Dict[str, Union[str, Any]]] = None,
        license_info: Optional[Dict[str, Union[str, Any]]] = None,
        openapi_prefix: str = "",
        root_path: str = "",
        root_path_in_servers: bool = True,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        callbacks: Optional[List[Dict[str, Any]]] = None,
        webhooks: Optional[routing.APIRouter] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        swagger_ui_parameters: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Callable[[routing.APIRoute], str] = Default(
            generate_unique_id
        ),
        **extra: Any,
    ) -> None:
        # Implementation would go here
        pass
