# AI Agent Instructions for codeql-demo-python

## Project Purpose
A **deliberately vulnerable** Python codebase designed to demonstrate GitHub Code Scanning with CodeQL. All security issues are intentional for teaching purposes.

## Architecture Overview
Three standalone, minimal Python scripts, each demonstrating a distinct injection vulnerability:
- **`insecure_eval.py`**: Unsafe `eval()` on untrusted user input (code injection)
- **`insecure_sql.py`**: SQL injection via f-string concatenation in queries
- **`insecure_subprocess.py`**: Command injection through `subprocess.run(..., shell=True)`

Each file includes:
1. A vulnerable function accepting untrusted input
2. A `__main__` block for standalone execution
3. Inline `# VULNERABILITY:` comments marking the specific flaw

## Code Patterns & Conventions

### Vulnerability Marking
Always include explicit `# VULNERABILITY:` comments when adding insecure patterns (for CodeQL demonstration). Example:
```python
# VULNERABILITY: eval on untrusted input
return eval(expr)
```

### Function Structure
- Input acceptance via CLI arguments (`sys.argv`) or direct prompts
- Minimal logic to focus on the vulnerability
- Print debug output before the vulnerable call for clarity

### File Organization
- No external dependencies beyond Python stdlib
- No class definitions (purely functional demos)
- Each file is independently executable

## CI/CD & Security Scanning

### CodeQL Workflow (`.github/workflows/codeql.yml`)
The project runs CodeQL analysis on:
- **Triggers**: Every push to `main`, all PRs, and weekly Monday schedule at 3 AM UTC
- **Scope**: Python language using `security-extended` and `security-and-quality` queries
- **Permissions**: Write to security events for reporting

**When modifying code:** New vulnerabilities will be detected automatically; no manual setup required.

## Development Workflow

### Testing Vulnerabilities Locally
```sh
# Eval injection - try entering: __import__('os').system('id')
python insecure_eval.py

# SQL injection - uses SQLite (database must exist first)
python insecure_sql.py <db_path> <username>

# Command injection - try entering: 127.0.0.1; whoami
python insecure_subprocess.py <host>
```

### Adding New Vulnerabilities
1. Create a new `.py` file in the root directory
2. Add a function accepting untrusted input
3. Include a `# VULNERABILITY: <description>` comment above the vulnerable code
4. Commit to a feature branch and open a PR—CodeQL will flag it automatically

## Important Constraints

- **Never fix vulnerabilities** unless explicitly requested (project is intentional for demo/education)
- **Avoid dependencies**: Keep examples stdlib-only to minimize external variables
- **Preserve simplicity**: Each script should demonstrate one flaw clearly
- **No tests/CI helpers**: Project focuses purely on vulnerability patterns

## Key Files
- `.github/workflows/codeql.yml` – Security scanning configuration
- `README.md` – Spanish-language project overview
- Individual `.py` files – Each demonstrates one injection type
