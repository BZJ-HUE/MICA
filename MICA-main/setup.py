from pathlib import Path

from setuptools import find_packages, setup

BASE_DIR = Path(__file__).resolve().parent
README_PATH = BASE_DIR.parent / "README.md"

__lib_name__ = "MICA"
__lib_version__ = "1.0.0"
__description__ = "MICA: A Cross-Modal Multi-View Contrastive Learning Framework for Spatial Multi-Omics Integration"
__url__ = "https://github.com/BZJ-HUE/MICA"
__keywords__ = [
    "Spatial Multi-modal Omics",
    "Graph Neural Networks",
    "Multi-view Contrastive Learning",
    "Spatial Domain Identification",
]

__requires__ = [
    "torch>=1.8.0",
    "numpy==1.22.3",
    "scanpy==1.9.1",
    "anndata==0.8.0",
    "rpy2==3.4.1",
    "pandas==1.4.2",
    "scipy==1.8.1",
    "scikit-learn==1.1.1",
    "scikit-misc==0.2.0",
    "tqdm==4.64.0",
    "matplotlib==3.4.2",
    "seaborn>=0.12.0",
]

if README_PATH.exists():
    __long_description__ = README_PATH.read_text(encoding="utf-8")
else:
    __long_description__ = __description__

setup(
    name=__lib_name__,
    version=__lib_version__,
    description=__description__,
    url=__url__,
    packages=find_packages(),
    install_requires=__requires__,
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    long_description=__long_description__,
    long_description_content_type="text/markdown",
    keywords=__keywords__,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
