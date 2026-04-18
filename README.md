# wcag-accessibility-testing
---
   Accessibility testing project using Lighthouse and Playwright to detect issues and validate WCAG 2.1 compliance
---

# Overview
This project demonstrates how to perform accessibility testing using a combination of automated tools and functional validation.
Lighthouse is used to detect accessibility issues, while Playwright validates real user interactions such as keyboard navigation, focus visibility, and form usability.
The results are mapped to official WCAG 2.1 success criteria and conformance levels (A and AA).

---
# Objective

To identify accessibility issues and validate whether a web application complies with WCAG standards.

---

# Tech Stack
    Playwright (TypeScript)
    Lighthouse CLI
    Python (WCAG classification)
    Node.js
---

# How It Works
1. Run Lighthouse Audit
2. Classify WCAG Issues (Python)
3. Run Playwright Tests
---

# Playwright Checks
    Keyboard navigation (WCAG 2.1.1)
    Focus visibility (WCAG 2.4.7)
    Form inputs usability (WCAG 3.3.2)
# Results
✔ Functional Validation (Playwright)
All tests passed:
    Keyboard navigation works
    Focus is visible
    Form inputs are interactable
❌ Accessibility Issues (Lighthouse)
    Missing alt text → WCAG 1.1.1 (Level A)
    Missing labels → WCAG 3.3.2 (Level A)
    Low contrast → WCAG 1.4.3 (Level AA)
# Final Status
 ❌ Not WCAG A compliant
 ❌ Not WCAG AA compliant

 # Key Insight
 ---
    A fully functional application does not guarantee accessibility compliance.
 ---

 # 🏗️ Architecture
 
 # 🔄 Flow
    1. Run Lighthouse audit
    2. Generate report.json
    3. Map issues to WCAG criteria
    4. Identify failing elements
    5. Validate behavior using Playwright
    6. Produce final accessibility result
    
 # 💥 What This Project Demonstrates
    Understanding of WCAG 2.1 (A & AA)
    Ability to map issues to official success criteria
    Automated accessibility detection (Lighthouse)
    Functional validation using Playwright
    QA mindset: detection + validation
    End-to-end accessibility testing approach
    
# 📎 Demo Website
    https://projects.accesscomputing.uw.edu/au/before.html
    
