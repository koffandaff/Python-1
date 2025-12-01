https://bzf4dfdp-3001.inc1.devtunnels.ms/
---

# 📘 Nettacker Command Cheat Sheet

### 🎛 Engine Options
| Flag | Description | Example |
|------|-------------|---------|
| `-v` | Verbosity level (0–5) | `nettacker -i 127.0.0.1 -m port_scan -v 3` |
| `--verbose-event` | Show state of each thread | `nettacker -i 127.0.0.1 -m port_scan --verbose-event` |
| `-V` | Show version | `nettacker -V` |
| `-o` | Save results (txt, csv, html, json) | `nettacker -i example.com -m admin_scan -o results.html` |
| `--graph` | Build graph (HTML output only) | `nettacker -i example.com -m admin_scan -o report.html --graph d3_tree_v2_graph` |
| `-L` | Language selection | `nettacker -i example.com -m port_scan -L fr` |

---

### 🎯 Target Options
| Flag | Description | Example |
|------|-------------|---------|
| `-i` | Inline targets (comma separated) | `nettacker -i 127.0.0.1,example.com` |
| `-l` | Load targets from file | `nettacker -l targets.txt` |

---

### 🔍 Method Options
| Flag | Description | Example |
|------|-------------|---------|
| `-m` | Run specific module | `nettacker -i example.com -m admin_scan` |
| `--show-all-modules` | List all modules | `nettacker --show-all-modules` |
| `--profile` | Run a predefined profile | `nettacker -i example.com --profile brute_force` |
| `--show-all-profiles` | List all profiles | `nettacker --show-all-profiles` |
| `-x` | Exclude modules | `nettacker -i example.com -m port_scan -x admin_scan` |
| `-X` | Exclude ports | `nettacker -i example.com -m port_scan -X 80,443` |
| `-g` | Ports to scan | `nettacker -i example.com -m port_scan -g 22,80,443` |

---

### 👤 Authentication / Brute Force
| Flag | Description | Example |
|------|-------------|---------|
| `-u` | Inline usernames | `nettacker -i example.com -m ssh_brute -u admin` |
| `-U` | Usernames from file | `nettacker -i example.com -m ssh_brute -U users.txt` |
| `-p` | Inline passwords | `nettacker -i example.com -m ssh_brute -p 1234` |
| `-P` | Passwords from file | `nettacker -i example.com -m ssh_brute -P pass.txt` |

---

### 🌐 Networking
| Flag | Description | Example |
|------|-------------|---------|
| `-R` | Use SOCKS proxy | `nettacker -i example.com -m port_scan -R socks5://127.0.0.1:9050` |
| `--ping-before-scan` | Ping host before scanning | `nettacker -i 192.168.1.1 --ping-before-scan` |
| `--retries` | Retry count | `nettacker -i example.com -m port_scan --retries 5` |

---

### ⚙️ Performance
| Flag | Description | Example |
|------|-------------|---------|
| `-t` | Threads per host | `nettacker -i example.com -m port_scan -t 10` |
| `-M` | Parallel module scans | `nettacker -i example.com -m port_scan -M 3` |
| `--set-hardware-usage` | Control resource usage (low, normal, high, max) | `nettacker -i example.com -m port_scan --set-hardware-usage high` |

---

### 📡 API Mode
| Flag | Description | Example |
|------|-------------|---------|
| `--start-api` | Start API service | `nettacker --start-api --api-host 0.0.0.0 --api-port 5000` |
| `--api-access-key` | Set API key | `nettacker --start-api --api-access-key mysecret` |
| `--api-client-whitelisted-ips` | Restrict API clients | `nettacker --start-api --api-client-whitelisted-ips 127.0.0.1,192.168.0.0/24` |

---

# 📂 Understanding Nettacker Report Files

When you run Nettacker with `-o results.html` (or `.json`, `.csv`, `.txt`), here’s what’s inside:

### 1. **results.html**
- A **graphical report** viewable in any browser.
- Contains tables of targets, modules, ports, and logs.
- If you used `--graph`, it will include interactive visualizations (like d3 trees).

### 2. **results.json**
- Machine‑readable format.
- Useful for automation, scripting, or importing into other tools.
- Example entry:
  ```json
  {
    "target": "172.25.80.1",
    "module": "port_scan",
    "port": 8080,
    "service": "http-alt",
    "ssl_flag": false
  }
  ```

### 3. **results.csv**
- Spreadsheet‑friendly format.
- Each row = one finding (date, target, module, port, logs).
- Easy to open in Excel or LibreOffice.

### 4. **results.txt**
- Plain text log.
- Good for quick viewing in terminal with `cat` or `less`.

---

# 🧠 How to “read” the logs
- **date** → when the finding was logged.  
- **target** → IP/domain scanned.  
- **module_name** → which module produced the result.  
- **port** → port number detected.  
- **logs** → dictionary of details (service type, regex matches, SSL flag, etc).  

Example:
```
Port 8080 → running_service: http-alt, ssl_flag: False
```
➡ Means: port 8080 is open, looks like HTTP, no SSL.



---

# 📘 Nettacker Modules Cheat Sheet

OWASP Nettacker modules fall into three categories:  
- **Scan** → detect services, versions, technologies  
- **Vuln** → check for known vulnerabilities  
- **Brute** → attempt brute force logins  

---

## 🔎 Scan Modules
| Module | Purpose |
|--------|---------|
| `adobe_aem_lastpatcheddate_scan` | Detect Adobe AEM and return last patched date |
| `admin_scan` | Look for admin folders (`/admin`, `/phpmyadmin`, `/wp-admin`, etc.) |
| `citrix_lastpatcheddate_scan` | Detect Citrix Netscaler Gateway and last patched date |
| `cms_detection_scan` | Identify CMS (WordPress, Drupal, Joomla) |
| `confluence_version_scan` | Detect Confluence version |
| `crushftp_lastpatcheddate_scan` | Detect CrushFTP and last patched date |
| `cups_version_scan` | Detect CUPS version (port 631) |
| `dir_scan` | Scan for well‑known directories |
| `drupal_modules_scan` | Detect popular Drupal modules |
| `drupal_theme_scan` | Detect popular Drupal themes |
| `drupal_version_scan` | Identify Drupal version |
| `icmp_scan` | Ping target, log response time |
| `http_redirect_scan` | Detect HTTP 3xx redirects and destination |
| `http_status_scan` | Return HTTP status code |
| `ivanti_csa_lastpatcheddate_scan` | Detect Ivanti CSA appliance last patched date |
| `ivanti_vtm_version_scan` | Detect Ivanti vTM version |
| `joomla_template_scan` | Detect Joomla templates |
| `joomla_user_enum_scan` | Enumerate Joomla users |
| `joomla_version_scan` | Identify Joomla version |
| `moveit_version_scan` | Detect Progress MOVEit version |
| `pma_scan` | Detect phpMyAdmin |
| `port_scan` | Scan open ports and identify services |
| `sender_policy_scan` | Check SPF policy settings |
| `shodan_scan` | Query Shodan API for target info |
| `subdomain_scan` | Enumerate subdomains |
| `viewdns_reverse_ip_lookup_scan` | Identify hosted domains via ViewDNS |
| `wappalyzer_scan` | Detect technologies/libraries with Wappalyzer |
| `wordpress_version_scan` | Identify WordPress version |
| `wp_plugin_scan` | Detect popular WordPress plugins |
| `wp_theme_scan` | Detect WordPress themes |
| `wp_timthumbs_scan` | Detect WordPress TimThumb.php |
| `wp_user_enum_scan` | Enumerate WordPress users |

---

## ⚡ Ports Scanned
- By default: **1000 most popular ports**  
- To scan all:  
  ```bash
  nettacker -i target.com -m port_scan -g 1-65535
  ```

---

## 🛡️ Vuln Modules
| Module | Purpose |
|--------|---------|
| `apache_ofbiz_cve_2024_38856` | Check Apache OFBiz CVE‑2024‑38856 |
| `apache_struts_vuln` | Check Apache Struts CVE‑2017‑5638 |
| `bftpd_*` | Multiple CVEs (DoS, overflow, memory leak) |
| `CCS_injection_vuln` | SSL CCS Injection CVE‑2014‑0224 |
| `citrix_cve_2019_19781_vuln` | Citrix CVE‑2019‑19781 |
| `citrix_cve_2023_24488_vuln` | Citrix CVE‑2023‑24488 (XSS) |
| `clickjacking_vuln` | Missing `X-Frame-Options` |
| `content_security_policy_vuln` | Missing CSP header |
| `content_type_options_vuln` | Missing `X-Content-Type-Options` |
| `crushftp_cve_2025_31161_vuln` | CrushFTP CVE‑2025‑31161 |
| `f5_cve_2020_5902_vuln` | F5 RCE CVE‑2020‑5902 |
| `heartbleed_vuln` | SSL Heartbleed CVE‑2014‑0160 |
| `msexchange_cve_2021_26855` | MS Exchange SSRF CVE‑2021‑26855 |
| `http_cors_vuln` | Overly permissive CORS |
| `options_method_enabled_vuln` | OPTIONS method enabled |
| `paloalto_panos_cve_2025_0108_vuln` | PAN‑OS CVE‑2025‑0108 |
| `paloalto_globalprotect_cve_2025_0133_vuln` | GlobalProtect CVE‑2025‑0133 (XSS) |
| `proftpd_*` | Multiple CVEs (SQLi bypass, DoS, overflow, traversal) |
| `server_version_vuln` | Server banner leakage |
| `sonicwall_sslvpn_cve_2024_53704_vuln` | SonicWALL SSLVPN CVE‑2024‑53704 |
| `ssl_signed_certificate_vuln` | Weak/self‑signed certs |
| `ssl_expired_certificate_vuln` | Expired certs |
| `ssl_version_vuln` | Old SSL versions supported |
| `ssl_weak_cipher_vuln` | Weak cipher suites |
| `wordpress_dos_cve_2018_6389_vuln` | WordPress DoS CVE‑2018‑6389 |
| `wp_plugin_cve_2023_47668_vuln` | WordPress plugin CVE‑2023‑47668 |
| `wp_xmlrpc_bruteforce_vuln` | XMLRPC brute force vuln |
| `wp_xmlrpc_pingback_vuln` | XMLRPC pingback vuln |
| `x_powered_by_vuln` | `X-Powered-By` leakage |
| `xdebug_rce_vuln` | XDebug RCE v2.5.5 |
| `XSS_protection_vuln` | Missing `X-XSS-Protection` |
| `vbulletin_cve_2019_16759_vuln` | vBulletin RCE CVE‑2019‑16759 |

---

## 🔐 Brute Modules
Default usernames: `admin, root, test, ftp, anonymous, user, support, 1`  
Default passwords: common weak ones (`admin`, `123456`, `password`, etc.)

| Module | Purpose |
|--------|---------|
| `ftp_brute` | Brute force FTP |
| `http_basic_auth_brute` | Brute force HTTP Basic Auth |
| `http_form_brute` | Brute force via HTTP form fields |
| `http_ntlm_brute` | Brute force HTTP NTLM |
| `smtp_brute` | Brute force SMTP (ports 25, 465, 587) |
| `ssh_brute` | Brute force SSH (port 22) |
| `telnet_brute` | Brute force Telnet (port 23) |
| `wp_xmlrpc_brute` | Brute force WordPress via XMLRPC |

---

## 🚀 Example Usage
- **Port scan all ports**
  ```bash
  nettacker -i 192.168.1.10 -m port_scan -g 1-65535
  ```
- **Run vulnerability check**
  ```bash
  nettacker -i example.com -m heartbleed_vuln
  ```
- **Brute force SSH**
  ```bash
  nettacker -i 192.168.1.10 -m ssh_brute -U users.txt -P passwords.txt
  ```

---


---

