async def swagger_middleware(app, handler):
    # Retrieve stored swagger validator
    async def middleware_handler(request, *args, **kwargs):
        # Find specs by path in request
        # Get all parameters in path, query, headers, body
        # Validate parameters
        response = await handler(request, *args, **kwargs)
        # Validate response
        return response

    return middleware_handler
