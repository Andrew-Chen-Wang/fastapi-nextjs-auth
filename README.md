# FastAPI + NextJS Auth

This is a template for a FastAPI + NextJS project with authentication.

### Usage (Local)

To get started, run:

```bash
cd frontend
npm install
cd ..
pip install -r requirements/local.txt
```

To run the backend:

```bash
python main.py run --reload --settings=local --log-level=debug
```

To run the frontend:

```shell
cd frontend
npm run dev
```

You can still run a script by adding a click command in [`main.py`](./main.py)

### Usage (Production)

We assume we'll deploy to a CDN with a server. We want to save
as much latency as possible + for SEO purposes, so we will find
which pieces of data we can pre-render.

### Credit and License

Template from https://github.com/Andrew-Chen-Wang/fastapi-django-orm.

Kudos to https://github.com/digitros/nextjs-fastapi for the NextJS template.

This repository is licensed under the Apache 2.0 license
which can be found in the [LICENSE](./LICENSE) file.
