from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl
from uuid import UUID
from datetime import datetime, time, timedelta

app = FastAPI(description="Fast API Tutorial : Part 11~12\ ExtraDatatype : UUID\Cookie and Header Parameters", version="0.1.0")

@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID, 
    start_date: datetime | None = Body(None),
    end_date: datetime | None = Body(None),
    repeat_at: time | None = Body(None),
    process_after: timedelta | None = Body(None)
    ):
    return {
        "item_id": item_id, 
        "start_date": start_date, 
        "end_date": end_date, 
        "repeat_at": repeat_at, 
        "process_after": process_after
    }

@app.get("/items")
async def read_items(
    cooki_id : Optional[str] = Cookie(None),
    accept_encoding: Optional[str] = Header(None),
    sec_ch_ua: Optional[str] = Header(None),
    user_agent: Optional[str] = Header(None),
    x_token: list[str] | None = Header(None)
    ):
    return {
        "cooki_id": cooki_id,
        "accept_encoding": accept_encoding,
        "sec_ch_ua": sec_ch_ua,
        "user_agent": user_agent,
        "x_token": x_token
    } 