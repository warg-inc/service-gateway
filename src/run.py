


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.setup.app_factory:create_web_app",
        factory=True,
        host="127.0.0.1",
        port=8000,
        reload=True,
        reload_dirs=["src"],
    )