# Cookiecutter Hyped Extension

A **Cookiecutter template** for creating `hyped` extensions. Extensions are optional add-ons that expand the core functionality of `hyped` by providing specialized nodes and operations for various use cases. This template provides a ready-to-use package structure that integrates with `hyped`.

## Features

- **Organized Structure**: Creates a modular, maintainable package structure.
- **Documentation Ready**: Includes basix setup for sphinx-style project documentation.
- **Testing Framework**: Prepares a folder for unit tests.
- **CI/CD Support**: Adds GitHub Actions workflows for automation (coming soon).

## Creating an extension repository

Here’s how to create an extension:

```bash
# install cookiecutter
pip install cookiecutter
# create repository from template
cookiecutter gh:open-hyped/hyped.extensions.cookiecutter
```

A directory of the following structure will be generated in the current directory:

```python
hyped.extensions.<NAME>
├── README.md                      # Description of your extension
├── pyproject.toml                 # Build system and dependency management
├── src/hyped/extensions/<NAME>    # Your extension package
│   ├── nodes                      # Directory for hyped nodes
│   └── ops                        # Directory for high-level operations
├── docs/                          # Basic Sphinx documentation setup
│   ├── build.sh                   # Builds the documentation locally
│   └── source/                    # Sphinx source directory
├── tests/hyped/extensions/<NAME>  # Unit tests for the extension
└── .github/workflows/             # GitHub Actions workflows
```

**Note**: The `src/hyped/extensions` directory is part of the `hyped.extensions` namespace. Do not add any files or folders directly in `src/hyped/extensions` (i.e., outside `<NAME>`). Doing so would break the namespace and could lead to import errors.

For example, the following structure is **invalid** and would cause issues:

```python
src/hyped/extensions/
├── my_extension/    # Valid
├── utils.py         # Invalid: Breaks the namespace
└── helpers/         # Invalid: Breaks the namespace
```

Instead, ensure all your extension's code is contained entirely within the `src/hyped/extensions/<NAME>` folder.


# Setting up a GitHub Repository

Follow these steps to configure the GitHub repository:

### 1. Create a GitHub Repository

Initialize the repository without a `README.md` or `.gitignore`, as these are already included in the template.

After creating a GitHub repository, link it to your local project directory as the remote repository:

```bash
git remote add origin <your-repo-url>
```

### 2. Configuring Secrets

GitHub Actions workflows included in the template require specific secrets to enable full functionality. These secrets can be configured on GitHub under **Settings > Secrets and Variables > Actions**.

Depending on the workflows you plan to use, add the following secrets:

- `COVERALLS_REPO_TOKEN`:

    Used in the `tests.yml` workflow to push coverage reports to Coveralls. To obtain this token, follow the instructions in the [Coveralls documentation](https://docs.coveralls.io/#integrate-coveralls-with-your-codebase).

- `TEST_PYPI_API_TOKEN`:

    Required by the `publish.yml` workflow to upload the package to TestPyPI for testing. Generate this token from your TestPyPI account settings under **Account Settings > API tokens**.

- `PYPI_API_TOKEN`:

    Required by the `publish.yml` workflow to upload the package to PyPI. Generate this token from your PyPI account settings under **Account Settings > API tokens**.

**Note**: If you don’t intend to use Coveralls, TestPyPI, or PyPI, you can skip setting up the respective secrets and modify or disable the workflows that depend on them.

### 3. Setting up GitHub Pages

The `docs.yml` workflow automatically builds and publishes documentation to GitHub Pages. To enable this functionality, follow these steps:

- Go to your repository on GitHub.
- Navigate to **Settings > Pages**.
- Under **Source**, select **Deploy from a branch**.
- In the Branch dropdown, choose `gh-pages` and click **Save**.


## Python Namespace Behavior

The hyped.extensions namespace relies on a shared structure between the core hyped package and any installed extensions. Python’s namespace packages have specific rules for handling modules across multiple installations, which can lead to unexpected issues if these rules are not followed.

- **Development Mode** (`pip install -e`): When the core `hyped` package is installed in development mode, the namespace `hyped.extensions` behaves differently than when installed in regular mode.

- **Mixed Installation Modes**: If the core `hyped` package is installed in development mode and an extension is installed in regular (non-development) mode, the namespace behavior can break. Specifically, the extension may fail to register under the `hyped.extensions` namespace.


| Core hyped Installation | Extension Installation | Behavior |
|-------------------------|------------------------|:--------:|
| Development Mode (-e)   | Development Mode (-e)  |    Ok    |
| Development Mode (-e)   | Regular Mode           |   Error  |
| Regular Mode            | Development Mode (-e)  |    Ok    |
| Regular Mode            | Regular Mode           |    Ok    |

This issue arises because Python uses a combination of `sys.path` and `*.dist-info` metadata to resolve namespaces. In development mode, the `src` directory is added to the `sys.path` directly, which can conflict with extensions installed in non-development mode (e.g., as `.dist-info` or `.egg-info`). This conflict prevents Python from correctly recognizing the namespace for extensions.

**Note**: This behavior is not specific to `hyped` but is a general limitation of Python’s namespace package system when mixing development and non-development installation modes.
