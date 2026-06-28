# Remarcable Take-Home Assignment

A Django web application for searching and filtering products by description, category, and tags.

## Requirements

- Python 3.12+
- pip

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/reubensinha/remarcable_take_home
cd remarcable
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the development server

```bash
python manage.py runserver
```

The database comes pre-populated with sample data — no migrations or data entry required.

## Admin Access

A pre-populated database is included with 5 categories, 10 tags, and 20 products.

Log in at `http://127.0.0.1:8000/admin` with:

- **Username:** admin
- **Email:** admin@example.com
- **Password:** testpassword1

## Usage

Navigate to `http://127.0.0.1:8000/products/` to access the search and filter interface.

- **Search:** filters products by description (case-insensitive, partial match)
- **Category:** filters products to a single category
- **Tags:** filters products by one or more tags (checkboxes); multiple selections are combined with OR logic
- Filters can be combined freely; click **Clear** to reset all filters

## Assumptions & Notes

- SQLite is used for simplicity; the repository includes a pre-populated `db.sqlite3` with sample data so no setup steps are required beyond installing dependencies and running the server
- URL Slugs are auto-generated from model names on save; duplicate names that produce identical slugs are technically possible, but for this exercise, collisions are assumed to be so rare as to not to occur in practice.
- Multiple selected tags use OR logic (products matching any selected tag are returned).`.distinct()` is applied to prevent duplicate results
- `on_delete=RESTRICT` is used on the Product→Category foreign key, preventing deletion of a category that has products assigned to it
