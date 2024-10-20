from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel

from llmstack.common.blocks.base.schema import StrEnum


class MessageType(StrEnum):
    BEGIN = "BEGIN"
    BOOKKEEPING = "BOOKKEEPING"
    CONTENT = "CONTENT"
    CONTENT_STREAM_CHUNK = "CONTENT_STREAM_CHUNK"
    CONTENT_STREAM_BEGIN = "CONTENT_STREAM_BEGIN"
    CONTENT_STREAM_END = "CONTENT_STREAM_END"
    ERRORS = "ERRORS"
    TOOL_CALL = "TOOL_CALL"
    TOOL_CALL_RESPONSE = "TOOL_CALL_RESPONSE"


class MessageData(BaseModel):
    pass


class Error(BaseModel):
    code: int = -1
    message: str


class ErrorsData(MessageData):
    errors: List[Error]


class ContentData(MessageData):
    content: Any


class ContentStreamChunkData(MessageData):
    chunk: Any


class ContentStreamErrorsData(MessageData):
    errors: List[Error]


class ToolCallData(MessageData):
    tool_call_id: str
    input: Dict
    name: str
    arguments: Dict


class ToolCallResponseData(MessageData):
    tool_call_id: str
    output: str = ""
    chunks: Dict = {}


class Message(BaseModel):
    id: str
    type: MessageType
    sender: str
    receiver: Optional[str] = None
    reply_to: Optional[str] = None  # Id of the message this is a reply to
    data: Optional[
        Union[
            ContentData,
            ContentStreamChunkData,
            ContentStreamErrorsData,
            ErrorsData,
            ToolCallData,
            ToolCallResponseData,
            Dict,
        ]
    ] = None
