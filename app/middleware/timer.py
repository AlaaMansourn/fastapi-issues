import time
from fastapi import Request


async def timming_midelware(request: Request,call_next):
    start =time.perf_counter()
    response = await call_next(request)
    response.headers["X_Proccess_Time"] = f"{time.perf_counter()-start:.4f}s"
    return response