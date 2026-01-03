# API Test Automation Examples (Python + Pytest)

This repository contains **example API automated tests** written in Python.
The goal of this project is **not** to provide a production-ready framework,
but to demonstrate **clear, reusable patterns** for API testing that can be
quickly understood and applied to other projects.

The examples focus on:
- clean test structure
- readable test flow
- separation of responsibilities
- minimal abstraction without overengineering

---

## Tech Stack

- Python 3
- Pytest
- Requests
- Pydantic (schemas)
- Faker (test data generation)
- Allure (optional reporting)

---

## Project Structure (High Level)

- `data/`dataclasses
  - API endpoints
  - data generators
  - dataclasses for request payloads
- `modules/`
  - request body builders
  - registered_module
- `utils/`
  - assertions
  - schema validation
  - logger
- `tests/`
  - API test examples
  - pytest fixtures

---

## Registration Tests

### Purpose

Registration tests verify the **client registration flow** and validate that:
- a client can be successfully registered
- the API returns a valid access token
- the response matches the expected schema

### What the tests do

1. Generate random client data using `Faker`
2. Build a request body using a schema
3. Send a `POST` request to `/api-clients`
4. Validate:
   - HTTP status code (`201 CREATED`)
   - response schema (`TokenResponseSchema`)

### Covered scenarios

- Direct URL usage via `Endpoints`
- URL construction using fixtures (environment-based)

These examples show **different ways to structure the same test logic** and
demonstrate how environment configuration can affect test behavior.

---

## Create Order Test

### Purpose

The create order test verifies that an **authenticated user** can successfully
create an order.

### What the test does

1. Registers a new client and retrieves an auth token (fixture)
2. Generates order data (book ID, customer name)
3. Sends a `POST` request to `/orders` with authorization headers
4. Validates:
   - HTTP status code (`201 CREATED`)
   - response schema (`CreateOrderResponseSchema`)

This test demonstrates:
- dependency on authentication
- usage of pytest fixtures
- passing headers between requests
- real API flow (register → authorize → create order)

---

### Project Philosophy

This repository is intentionally kept simple and educational.

Tests should be easy to read

Architecture should be understandable at a glance

Examples should help quickly bootstrap new API automation projects

No unnecessary abstractions.
No hidden magic.
Focus on clarity and reusability.

## Environment Configuration

Some examples use environment variables.

Create a `.env` file in the project root if needed:

```env
BASE_URL=https://simple-books-api.click

If the environment variable is not set, the tests can fall back to
the base URL defined in Endpoints.

---

How to Run Tests

Activate virtual environment and install dependencies:

pip install -r requirements.txt


Run all tests:

pytest


Run with Allure (optional):

pytest --alluredir=allure-results
allure serve allure-results

---
