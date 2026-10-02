libraries = [
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "sklearn",
    "scipy",
    "openpyxl",
    "statsmodels",
    "jupyter",
    "plotly"
]

for lib in libraries:
    try:
        module = __import__(lib)
        version = getattr(module, "__version__", "version unknown")
        print(f"✅ {lib:<12} {version}")
    except ImportError:
        print(f"❌ {lib:<12} NOT INSTALLED")