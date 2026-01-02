# Security Policy

## 🛡️ Reporting a Vulnerability

The RAGbot team takes security seriously. We appreciate your efforts to responsibly disclose your findings and will make every effort to acknowledge your contributions.

### How to Report a Security Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report security vulnerabilities by using one of the following methods:

1. **GitHub Security Advisories** (Preferred)
   - Go to the [Security tab](https://github.com/H0NEYP0T-466/RAGbot/security) of this repository
   - Click "Report a vulnerability"
   - Fill out the advisory form with details

2. **Direct Contact**
   - Open a [private security advisory](https://github.com/H0NEYP0T-466/RAGbot/security/advisories/new)
   - If you prefer, you can also create a private issue with the label `security`

### What to Include in Your Report

Please include the following information in your report:

- **Type of vulnerability** (e.g., XSS, SQL injection, authentication bypass, etc.)
- **Full paths of source file(s)** related to the manifestation of the issue
- **Location of the affected source code** (tag/branch/commit or direct URL)
- **Step-by-step instructions** to reproduce the issue
- **Proof-of-concept or exploit code** (if possible)
- **Impact of the issue**, including how an attacker might exploit it
- **Any potential mitigations** you've identified

### What to Expect

After you submit a vulnerability report, you can expect:

1. **Acknowledgment**: We will acknowledge receipt of your report within **48 hours**
2. **Assessment**: We will assess the vulnerability and determine its impact and severity
3. **Updates**: We will keep you informed of our progress throughout the process
4. **Resolution**: We will work to fix the vulnerability as quickly as possible
5. **Credit**: We will credit you in the security advisory (unless you prefer to remain anonymous)

### Disclosure Policy

- Security issues will be addressed with high priority
- We aim to resolve critical vulnerabilities within **7 days**
- We will coordinate the disclosure timeline with you
- We will publicly disclose the vulnerability after a fix is released
- Security patches will be released for the current major version

---

## 🔒 Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | ✅ Yes             |
| < Latest| ❌ No              |

We recommend always using the latest version of RAGbot for the best security.

---

## 🔐 Security Best Practices

When deploying RAGbot, please follow these security best practices:

### API Keys and Secrets

- **Never commit API keys** or secrets to the repository
- Use **environment variables** for sensitive configuration
- Rotate API keys regularly
- Use different keys for development and production

### Backend Security

- **Keep dependencies updated**: Regularly update Python packages
  ```bash
  pip list --outdated
  pip install -U package_name
  ```
- **Use HTTPS** in production environments
- **Implement rate limiting** to prevent abuse
- **Validate and sanitize** all user inputs
- **Use CORS** properly to restrict API access

### Frontend Security

- **Keep npm packages updated**: Regularly check for vulnerabilities
  ```bash
  npm audit
  npm audit fix
  ```
- **Sanitize user input** before rendering
- **Use Content Security Policy (CSP)** headers
- **Avoid storing sensitive data** in local storage

### Deployment Security

- **Use secure connections** (HTTPS/TLS)
- **Enable authentication** for production deployments
- **Implement logging and monitoring** for security events
- **Regular security audits** of dependencies
- **Backup data regularly**

---

## 🔍 Security Features

RAGbot implements the following security measures:

- **Input validation** on all API endpoints
- **CORS configuration** to restrict cross-origin requests
- **Environment-based configuration** for sensitive data
- **No hardcoded credentials** in the codebase
- **Dependency scanning** via GitHub Dependabot

---

## 🚨 Known Security Considerations

### LLM Integration

- RAGbot uses external LLM APIs (LongCat) - ensure you trust the provider
- User queries are sent to external services - inform users accordingly
- Implement appropriate **data privacy measures** for sensitive documents

### Document Processing

- PDF and Markdown documents are processed locally
- Validate document sources before indexing
- Be cautious with user-uploaded documents in production

### Vector Database

- FAISS index stores embeddings locally
- Ensure proper file permissions on the `faiss_index/` directory
- Consider encryption for sensitive indexed data

---

## 📚 Additional Resources

- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [React Security Best Practices](https://react.dev/learn/react-developer-tools)
- [GitHub Security Advisories](https://docs.github.com/en/code-security/security-advisories)

---

## 🙏 Thank You

We appreciate the security research community's efforts in keeping RAGbot and its users safe. Responsible disclosure of vulnerabilities helps us ensure the security and privacy of all users.

---

**Last Updated**: January 2026

For general questions about security, feel free to open a [Discussion](https://github.com/H0NEYP0T-466/RAGbot/discussions).
