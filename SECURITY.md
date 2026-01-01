# Security Policy

## 🛡️ Security

We take the security of RAGbot seriously. This document outlines our security policy and how to report vulnerabilities responsibly.

---

## 📢 Reporting a Vulnerability

If you discover a security vulnerability in RAGbot, please help us by reporting it responsibly.

### How to Report

**DO NOT** open a public GitHub issue for security vulnerabilities.

Instead, please report security issues through one of the following methods:

1. **GitHub Security Advisories** (Preferred)
   - Go to the [Security tab](https://github.com/H0NEYP0T-466/RAGbot/security)
   - Click "Report a vulnerability"
   - Fill out the vulnerability report form

2. **Email**
   - Send details to the repository maintainers via GitHub
   - Include "SECURITY" in the subject line

### What to Include

When reporting a security issue, please provide:

- **Description** of the vulnerability
- **Steps to reproduce** the issue
- **Potential impact** of the vulnerability
- **Affected versions** (if known)
- **Suggested fix** (if you have one)
- **Your contact information** for follow-up questions

### Example Report

```
Subject: SECURITY - SQL Injection Vulnerability in API Endpoint

Description:
The /chat endpoint is vulnerable to SQL injection attacks when processing user input.

Steps to Reproduce:
1. Send a POST request to /chat with payload: {"message": "'; DROP TABLE--"}
2. Observe database query execution

Impact:
An attacker could potentially access or modify database contents.

Affected Versions:
All versions prior to 1.0.0

Suggested Fix:
Use parameterized queries instead of string concatenation.
```

---

## 🔒 Vulnerability Handling Process

### Our Commitment

When you report a vulnerability, we commit to:

1. **Acknowledge receipt** within 48 hours
2. **Provide an initial assessment** within 5 business days
3. **Keep you informed** of progress toward a fix
4. **Notify you** when the vulnerability is fixed
5. **Publicly credit you** (if desired) once the fix is released

### Timeline

- **Critical vulnerabilities**: Addressed within 7 days
- **High severity**: Addressed within 30 days
- **Medium/Low severity**: Addressed within 90 days

### Disclosure Policy

We follow **coordinated disclosure**:

1. Vulnerability reported to maintainers
2. Fix developed and tested
3. Security advisory published
4. Patch released
5. Public disclosure (typically 90 days after initial report)

---

## 🔐 Security Best Practices

### For Users

When deploying RAGbot, follow these security best practices:

#### API Keys & Secrets

- ✅ **Never commit** API keys or secrets to version control
- ✅ **Use environment variables** for sensitive configuration
- ✅ **Rotate keys regularly** (at least every 90 days)
- ✅ **Use different keys** for development and production
- ✅ **Restrict API key permissions** to minimum required

#### Network Security

- ✅ **Use HTTPS** in production environments
- ✅ **Implement rate limiting** to prevent abuse
- ✅ **Use a firewall** to restrict access to backend ports
- ✅ **Keep backend API** on a private network when possible
- ✅ **Enable CORS** only for trusted domains

#### Authentication & Authorization

- ✅ **Implement authentication** for production deployments
- ✅ **Use secure session management**
- ✅ **Validate and sanitize** all user inputs
- ✅ **Implement access controls** for sensitive operations

#### Dependencies

- ✅ **Keep dependencies updated** regularly
- ✅ **Monitor security advisories** for dependencies
- ✅ **Use `npm audit`** and `pip-audit` to check for vulnerabilities
- ✅ **Review dependency changes** before updating

#### Monitoring & Logging

- ✅ **Enable logging** for security events
- ✅ **Monitor for suspicious activity**
- ✅ **Set up alerts** for critical errors
- ✅ **Regularly review logs**

#### Data Security

- ✅ **Encrypt sensitive data** at rest and in transit
- ✅ **Implement data retention policies**
- ✅ **Backup data regularly**
- ✅ **Secure document storage** in the `backend/data/` directory

### For Contributors

When contributing code:

- ✅ **Follow secure coding practices**
- ✅ **Validate all inputs** (especially user-provided data)
- ✅ **Sanitize outputs** to prevent XSS
- ✅ **Use parameterized queries** to prevent SQL injection
- ✅ **Avoid hardcoding secrets**
- ✅ **Review dependencies** for known vulnerabilities
- ✅ **Write security-aware code**
- ✅ **Document security considerations**

---

## 🚨 Known Security Considerations

### Current Limitations

This is an open-source project primarily for educational and research purposes. Please be aware:

1. **No Built-in Authentication**
   - The default setup does not include authentication
   - Implement authentication before exposing to the internet

2. **API Key Management**
   - API keys are stored in environment variables
   - Ensure `.env` files are never committed

3. **Document Upload**
   - Documents are stored on the filesystem
   - Implement access controls for document directories

4. **CORS Configuration**
   - Default CORS settings may be permissive for development
   - Restrict CORS in production

5. **Rate Limiting**
   - No default rate limiting is implemented
   - Add rate limiting for production deployments

### Recommended Enhancements for Production

Before deploying to production, consider:

- [ ] Implement user authentication and authorization
- [ ] Add rate limiting to API endpoints
- [ ] Configure CORS for specific trusted domains
- [ ] Set up HTTPS with valid certificates
- [ ] Implement input validation and sanitization
- [ ] Add security headers (CSP, HSTS, etc.)
- [ ] Set up monitoring and alerting
- [ ] Implement database backups
- [ ] Use a reverse proxy (nginx, Caddy)
- [ ] Enable audit logging

---

## 📋 Security Checklist

Use this checklist when deploying RAGbot:

### Environment Setup

- [ ] Environment variables configured
- [ ] API keys secured and not in code
- [ ] `.env` files excluded from version control
- [ ] Different keys for dev/staging/prod

### Network Security

- [ ] HTTPS enabled
- [ ] Firewall configured
- [ ] CORS restricted to trusted domains
- [ ] Rate limiting enabled

### Application Security

- [ ] Authentication implemented
- [ ] Input validation enabled
- [ ] Output sanitization in place
- [ ] Security headers configured

### Monitoring

- [ ] Logging enabled
- [ ] Alerts configured
- [ ] Regular security reviews scheduled

### Updates & Maintenance

- [ ] Dependencies up-to-date
- [ ] Security patches applied
- [ ] Backup system in place
- [ ] Incident response plan documented

---

## 🔍 Security Audits

We encourage security researchers to:

- Review our code for vulnerabilities
- Perform responsible security testing
- Report findings through proper channels

### Scope

**In Scope:**
- Authentication and authorization issues
- SQL injection, XSS, CSRF vulnerabilities
- API security issues
- Dependency vulnerabilities
- Information disclosure
- Access control issues

**Out of Scope:**
- Social engineering attacks
- Physical security
- DDoS attacks
- Issues in third-party dependencies (report to respective projects)

---

## 📚 Resources

### Security Tools

- [npm audit](https://docs.npmjs.com/cli/v8/commands/npm-audit) - Check for npm vulnerabilities
- [Snyk](https://snyk.io/) - Dependency vulnerability scanning
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Web application security risks
- [pip-audit](https://github.com/pypa/pip-audit) - Check Python dependencies

### Security Best Practices

- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [React Security Best Practices](https://reactjs.org/docs/dom-elements.html#dangerouslysetinnerhtml)

---

## 🤝 Acknowledgments

We would like to thank the following security researchers for responsibly disclosing vulnerabilities:

*(List will be updated as vulnerabilities are reported and fixed)*

---

## 📞 Contact

For security-related questions or concerns:

- Use GitHub Security Advisories for vulnerability reports
- For general security questions, open a discussion or contact maintainers

---

**Last Updated**: January 2026

Thank you for helping keep RAGbot secure! 🔒
