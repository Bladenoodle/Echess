"""Module for invoke tasks"""
from invoke import task
from src.database_files.db import init_db

@task
def start(ctx):
    """Run the program and initialize database if database doesn't exist"""
    init_db()
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    """Run testing"""
    ctx.run("pytest src/tests/ --maxfail=1 --disable-warnings -q", pty=True)

@task(name="coverage-report")
def coverage_report(ctx):
    """Run tests with coverage and generate HTML report"""
    ctx.run("coverage run -m pytest src/tests/", pty=True)
    ctx.run("coverage html", pty=True)
