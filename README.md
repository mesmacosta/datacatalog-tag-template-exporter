# Datacatalog Tag Template Exporter

[![CircleCI][1]][2] [![PyPi][7]][8] [![License][9]][9] [![Issues][10]][11]

A Python package to manage Google Cloud Data Catalog Tag Template export scripts.

**Disclaimer: This is not an officially supported Google product.**

<!--
  ⚠️ DO NOT UPDATE THE TABLE OF CONTENTS MANUALLY ️️⚠️
  run `npx markdown-toc -i README.md`.

  Please stick to 80-character line wraps as much as you can.
-->

## Table of Contents

<!-- toc -->

- [Executing in Cloud Shell](#executing-in-cloud-shell)
- [1. Environment setup](#1-environment-setup)
  * [1.1. Python + virtualenv](#11-python--virtualenv)
    + [1.1.1. Install Python 3.6+](#111-install-python-36)
    + [1.1.2. Get the source code](#112-get-the-source-code)
    + [1.1.3. Create and activate an isolated Python environment](#113-create-and-activate-an-isolated-python-environment)
    + [1.1.4. Install the package](#114-install-the-package)
  * [1.2. Docker](#12-docker)
  * [1.3. Auth credentials](#13-auth-credentials)
    + [1.3.1. Create a service account and grant it below roles](#131-create-a-service-account-and-grant-it-below-roles)
    + [1.3.2. Download a JSON key and save it as](#132-download-a-json-key-and-save-it-as)
    + [1.3.3. Set the environment variables](#133-set-the-environment-variables)
- [2. Export Templates to CSV file](#2-export-templates-to-csv-file)
  * [2.1. A CSV file representing the Templates will be created](#21-a-csv-file-representing-the-templates-will-be-created)
  * [2.2. Run the datacatalog-tag-template-exporter script](#22-run-the-datacatalog-tag-template-exporter-script)

<!-- tocstop -->

-----

## Executing in Cloud Shell
````bash
# Set your SERVICE ACCOUNT, for instructions go to 1.3. Auth credentials
# This name is just a suggestion, feel free to name it following your naming conventions
export GOOGLE_APPLICATION_CREDENTIALS=~/datacatalog-tag-template-exporter-sa.json

# Install datacatalog-tag-template-exporter
pip3 install datacatalog-tag-template-exporter --user

# Add to your PATH
export PATH=~/.local/bin:$PATH

# Look for available commands
datacatalog-tag-template-exporter --help
````

## 1. Environment setup

### 1.1. Python + virtualenv

Using [virtualenv][3] is optional, but strongly recommended unless you use [Docker](#12-docker).

#### 1.1.1. Install Python 3.6+

#### 1.1.2. Get the source code
```bash
git clone https://github.com/mesmacosta/datacatalog-tag-template-exporter
cd ./datacatalog-tag-template-exporter
```

_All paths starting with `./` in the next steps are relative to the `datacatalog-tag-template-exporter`
folder._

#### 1.1.3. Create and activate an isolated Python environment

```bash
pip install --upgrade virtualenv
python3 -m virtualenv --python python3 env
source ./env/bin/activate
```

#### 1.1.4. Install the package

```bash
pip install --upgrade .
```

### 1.2. Docker

Docker may be used as an alternative to run the script. In this case, please disregard the
[Virtualenv](#11-python--virtualenv) setup instructions.

### 1.3. Auth credentials

#### 1.3.1. Create a service account and grant it below roles

- Data Catalog Admin

#### 1.3.2. Download a JSON key and save it as
This name is just a suggestion, feel free to name it following your naming conventions
- `./credentials/datacatalog-tag-template-exporter-sa.json`

#### 1.3.3. Set the environment variables

_This step may be skipped if you're using [Docker](#12-docker)._

```bash
export GOOGLE_APPLICATION_CREDENTIALS=~/credentials/datacatalog-tag-template-exporter-sa.json
```

## 2. Export Templates to CSV file

### 2.1. A CSV file representing the Templates will be created

Templates are composed of as many lines as required to represent all of their fields. The columns are
described as follows:

| Column                 | Description                                    | 
| ---                    | ---                                            | 
| **template_name**      | Resource name of the Tag Template for the Tag. | 
| **display_name**       | Resource name of the Tag Template for the Tag. | 
| **field_id**           | Id of the Tag Template field.                  | 
| **field_display_name** | Display name of the Tag Template field.        | 
| **field_type**         | Type of the Tag Template field.                | 
| **enum_values**        | Values for the Enum field.                     | 

### 2.2. Run the datacatalog-tag-template-exporter script

- Python + virtualenv

```bash
datacatalog-tag-template-exporter tag-templates export --project-ids my-project --file-path CSV_FILE_PATH
```


[1]: https://circleci.com/gh/mesmacosta/datacatalog-tag-template-exporter.svg?style=svg
[2]: https://circleci.com/gh/mesmacosta/datacatalog-tag-template-exporter
[3]: https://virtualenv.pypa.io/en/latest/
[7]: https://img.shields.io/pypi/v/datacatalog-tag-template-exporter.svg
[8]: https://pypi.org/project/datacatalog-tag-template-exporter/
[9]: https://img.shields.io/github/license/mesmacosta/datacatalog-tag-template-exporter.svg?force_cache=true
[10]: https://img.shields.io/github/issues/mesmacosta/datacatalog-tag-template-exporter.svg
[11]: https://github.com/mesmacosta/datacatalog-tag-template-exporter/issues
