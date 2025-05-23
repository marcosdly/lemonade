from setuptools import setup

with open("src/lemonade/version.py", encoding="utf-8") as fp:
    version = fp.read().split('"')[1]


setup(
    name="lemonade-sdk",
    version=version,
    description="Lemonade SDK: Your LLM Aide for Validation and Deployment",
    author_email="lemonade@amd.com",
    package_dir={"": "src"},
    packages=[
        "lemonade",
        "lemonade.profilers",
        "lemonade.common",
        "lemonade.tools",
        "lemonade.tools.ort_genai",
        "lemonade.tools.quark",
        "lemonade.tools.report",
        "lemonade.tools.server",
        "lemonade_install",
        "lemonade_server",
    ],
    # NOTE versions are the latest releases under the major version (as in semver)
    install_requires=[
        "invoke>=2.2.0,<3",
        "onnx>=1.18.0,<2",
        "torch>=2.7.0,<3",
        "pyyaml>=5.4.1,<6",
        "typeguard>=2.13.3,<3",
        "packaging>=25.0,<26",
        "numpy>=2.2.6,<3",
        "pandas>=2.2.3,<3",
        "fasteners",
        "GitPython>=3.1.44,<4",
        "psutil>=6.1.1,<7",
        "wmi",
        "pytz",
        "zstandard",
        "matplotlib",
        "tabulate",
        # huggingface-hub==0.31.0 introduces a new transfer protocol that was causing us issues
        "huggingface-hub==0.30.2",
    ],
    extras_require={
        "llm": [
            "transformers",
            "accelerate",
            "py-cpuinfo",
            "sentencepiece",
            "datasets",
            # Install human-eval from a forked repo with Windows support until the
            # PR (https://github.com/openai/human-eval/pull/53) is merged
            "human-eval-windows==1.0.4",
            "fastapi",
            "uvicorn[standard]",
            "openai>=1.82.0",
            "lm-eval[api]",
        ],
        "llm-oga-igpu": [
            "onnxruntime-genai-directml==0.8.0",
            "onnxruntime-directml==1.22.0",
            "transformers==4.52.3",
            "lemonade-sdk[llm]",
        ],
    },
    classifiers=[],
    entry_points={
        "console_scripts": [
            "lemonade=lemonade:lemonadecli",
            "lemonade-install=lemonade_install:installcli",
            "lemonade-server=lemonade_server.cli:main",
            "lemonade-server-dev=lemonade_server.cli:main",
        ]
    },
    python_requires=">=3.11, <3.13",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    package_data={
        "lemonade_server": ["server_models.json"],
    },
)

# This file was originally licensed under Apache 2.0. It has been modified.
# Modifications Copyright (c) 2025 AMD
