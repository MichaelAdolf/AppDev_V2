@app.post("/refresh")
def trigger_refresh():
    try:
        script_path = Path("scripts/run_daily_refresh.py")

        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            check=True,
        )

        return {
            "status": "success",
            "message": "Daily refresh completed",
            "output": result.stdout,
        }

    except subprocess.CalledProcessError as exc:
        return {
            "status": "error",
            "message": str(exc),
            "output": exc.stdout,
            "error": exc.stderr,
        }
