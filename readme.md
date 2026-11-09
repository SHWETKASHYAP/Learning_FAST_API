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
