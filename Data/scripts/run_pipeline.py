from src.pipeline_pkg.pipeline import run_pipeline

if __name__ == "__main__":
    success = run_pipeline()

    if success:
        print("Run completed")
    else:
        print("Skipped (already ran today)")
