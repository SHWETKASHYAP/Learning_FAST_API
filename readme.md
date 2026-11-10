#----- /data route :-

When you call FastAPI(title="Learning API", version="0.1.0"), it registers three extra routes on your app:

Route	What it returns
/openapi.json	The machine-readable description of your API (JSON)
/docs	Swagger UI page (interactive)
/redoc	ReDoc page (read-only, cleaner for reading)

Normally, API documentation is a separate document someone writes by hand. It goes out of date the moment the code changes. Frontend developers then call endpoints wrongly because the docs lied.

FastAPI’s idea: your code already contains all the information (paths, methods, types). So generate the docs from the code, and they can never drift.

Think of a restaurant that prints its menu automatically from the kitchen’s recipe list. If the chef adds a dish, the menu updates itself. Nobody writes the menu by hand.

Your endpoints are the recipes. /docs is the menu


#----------async def:-

“In FastAPI, async def endpoints run directly on the event loop, so they must only use non-blocking, awaitable operations. Plain def endpoints are run in a thread pool, so blocking calls are safe but each request uses a thread. async def hurts performance when you call blocking code inside it, like time.sleep, requests.get, or a sync database driver, because it blocks the event loop and stalls every other request. The fix is either to use async libraries, declare the endpoint with plain def, or offload the blocking part with asyncio.to_thread. For CPU-bound work, neither helps because of the GIL, so I’d use multiple processes or a task queue.”