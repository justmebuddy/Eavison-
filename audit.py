# audit.py
import re

# Enhanced Regex Patterns
SQL_ERRORS = [
    r"SQL syntax.*MySQL", r"Warning.*mysql_", r"Unclosed quotation mark",
    r"PostgreSQL.*ERROR", r"SQLite/JDBCDriver", r"ORA-\d{5}",
    r"Microsoft OLE DB Provider for SQL Server"
]

XSS_PATTERNS = [
    r"<script.*?>.*?</script>", r"onerror\s*=", r"onload\s*=",
    r"javascript:", r"<img.*?src=", r"alert\(", r"eval\("
]

# User Information & Data Leak Patterns
DATA_LEAK_PATTERNS = [
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", # Emails
    r"root@localhost", r"password\s*=", r"api[_-]?key",
    r"token\s*=", r"database\s*error", r"stack trace"
]

# Version Detection Patterns
SERVICE_REGEX = {
    "Apache": r"Apache/\d\.\d\.\d+",
    "PHP": r"PHP/\d\.\d\.\d+",
    "IIS": r"IIS/\d\.\d+"
}

def analyze_response(url, html, headers):
    findings = []

    # Check for SQLi
    for pattern in SQL_ERRORS:
        if re.search(pattern, html, re.IGNORECASE):
            findings.append("SQL Injection indicator")
            break

    # Check for XSS
    for pattern in XSS_PATTERNS:
        if re.search(pattern, html, re.IGNORECASE):
            findings.append("Possible XSS pattern")
            break

    # Check for Sensitive Data Leak
    for pattern in DATA_LEAK_PATTERNS:
        if re.search(pattern, html, re.IGNORECASE):
            findings.append("Sensitive data exposure")
            break

    # Check for Outdated Service Software
    for service, pattern in SERVICE_REGEX.items():
        if re.search(pattern, str(headers), re.IGNORECASE):
            findings.append(f"Potential outdated service: {service}")

    return list(set(findings))
