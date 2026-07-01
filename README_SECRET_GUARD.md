# Secret Guard

This project includes a Git pre-commit hook that blocks commits containing likely secrets.

## What It Checks

The hook scans staged files before each commit for:

- `OPENAI_API_KEY`
- `sk-`
- `sk-proj-`
- `AWS_SECRET_ACCESS_KEY`
- `PRIVATE KEY`

It does not create or store any real API keys.

## Enable The Hook

Run this once from the project folder:

```sh
git config core.hooksPath .githooks
```

After that, Git will run `.githooks/pre-commit` before every commit.

## Safe Test

Use only placeholders. Do not paste a real key.

1. Create a test file:

```sh
echo "OPENAI_API_KEY=placeholder-only" > secret-test.txt
```

2. Stage it:

```sh
git add secret-test.txt
```

3. Try to commit:

```sh
git commit -m "test secret guard"
```

The commit should be blocked.

4. Clean up:

```sh
git reset -- secret-test.txt
rm secret-test.txt
```

## Environment Files

`.env` and `.env.*` are ignored by Git. `.env.example` is allowed so the project can keep safe placeholder examples.
