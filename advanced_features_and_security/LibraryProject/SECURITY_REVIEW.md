## Security Measures Implemented

- **HTTPS enforced:** All HTTP requests are redirected to HTTPS.
- **HSTS enabled:** Browsers are instructed to always use HTTPS for one year, including subdomains and preload.
- **Secure cookies:** Session and CSRF cookies are only sent over HTTPS.
- **Secure headers:** Clickjacking, MIME sniffing, and XSS protections are enabled.
- **SSL/TLS certificates:** Deployment instructions provided for secure server configuration.

### Areas for Improvement

- Regularly update SSL certificates.
- Monitor security advisories for Django and dependencies.
- Consider using additional security middleware (e.g., django-csp for Content Security Policy).