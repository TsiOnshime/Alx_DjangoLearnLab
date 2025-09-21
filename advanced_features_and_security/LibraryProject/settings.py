# --- HTTPS and Secure Redirects ---
SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS

SECURE_HSTS_SECONDS = 31536000  # Enforce HTTPS for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow site to be included in browser preload lists

SESSION_COOKIE_SECURE = True  # Session cookies only sent over HTTPS
CSRF_COOKIE_SECURE = True     # CSRF cookies only sent over HTTPS

X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME type sniffing
SECURE_BROWSER_XSS_FILTER = True    # Enable browser XSS filter

# --- End HTTPS and Secure Redirects ---