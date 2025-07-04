# SMHI SQLMesh App

This repository contains a SQLMesh-based application that fetches weather warnings from the SMHI API and processes the data for further analysis or alerting. The application is containerized using Docker and can be integrated into automated workflows (e.g. k3s, cron jobs).

## Features

- Fetches and processes impact-based weather warnings from SMHI's open data API
- Supports Postgres as a backend database
- Designed for containerized environments (Docker, Docker Compose, k3s)
- Includes models for raw data ingestion, transformations, and alerting

## Getting started

### Prerequisites

- Docker
- Docker Compose
- Optionally: Python 3.12 and `sqlmesh` installed locally

### Build and run with Docker Compose

- docker compose up --build

### Running locally without Docker


## Configuration

Update connection settings in `config.yaml` to match your database and environment setup.

## Contributing

Feel free to submit pull requests or open issues for enhancements, bug fixes, or improvements.

## License

Specify your license here (e.g. MIT, Apache 2.0).
