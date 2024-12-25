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


## Setting up a GitHub Repository

Follow these steps to configure the GitHub repository:

### 1. Create a GitHub Repository

Initialize the repository without a `README.md` or `.gitignore`, as these are already included in the template.

After creating a GitHub repository, link it to your local project directory as the remote repository:

```bash
git remote add origin <your-repo-url>
```

### 2. Configuring GitHub Actions

To enable full functionality of the GitHub Actions workflows included in this template, some configuration is required. Follow the steps below to set up the necessary components.

#### 2.1. Coveralls Integation

If you want to track test coverage and push coverage reports to [coveralls.io](https://coveralls.io), you’ll need to configure the `COVERALLS_REPO_TOKEN` secret on the GitHub Repository under **Settings > Secrets and Variables > Actions**. To obtain the token, follow the instructions [here](https://docs.coveralls.io/#integrate-coveralls-with-your-codebase).

#### 2.2. PyPI Configuration (Trusted Publisher)

To enable the publish.yml workflow to upload your package to PyPI, you need to register GitHub as a trusted publisher. Log in to your **PyPI account** and navigate to the **Publishing** section. Enter the requested details about your package and repository to register GitHub as a **trusted publisher**. Follow the instructions provided on PyPI to complete the registration. Once this is done, the GitHub Actions workflow will be able to securely upload your package to PyPI.

**Note: The Environment name needs to be "pypi".**

#### 2.3 TestPyPI Configuration

The process **TestPyPI** is identical, except you'll need to use your [TestPyPI account](https://test.pypi.org) instead.


### 3. Setting up GitHub Pages

The `docs.yml` workflow automatically builds and publishes documentation to GitHub Pages. To enable this functionality, follow these steps:

1. Go to your repository on GitHub.
2. Navigate to **Settings > Pages**.
3. Under **Source**, select **Deploy from a branch**.
4. In the Branch dropdown, choose `gh-pages` and click **Save**.


## Publishing a Release

This template includes an automated workflow to handle the process of publishing a release to both **PyPI** and **GitHub**. Whenever you push a commit to the `main` branch, the workflow is tested by publishing the distribution to **TestPyPI**. When you create a tag with a valid version format (e.g., v1.2.3), the release workflow will be triggered to publish the release to both **PyPI** and **GitHub**.

To create a version release, run the following git commands:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Once the tag is pushed to GitHub, the workflow will trigger automatically:

- **Publish to TestPyPI**: First, the workflow will test the publishing process by pushing the release to TestPyPI.
- **Publish to PyPI**: If everything goes smoothly on TestPyPI, the workflow will proceed to publish the release to PyPI.
- **GitHub Release**: Lastly, the workflow will sign the distribution and upload it as a GitHub Release.


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
