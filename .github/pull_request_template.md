# Pull Request

## 📝 Release Notes

<!-- 
This section will be automatically extracted for release notes generation.
Follow conventional commit format in your commit messages for best results.
-->

### Summary
<!-- Brief one-line summary that will appear in release notes -->
<!-- Example: "Add user authentication module with OAuth2 support" -->

### Description
<!-- Detailed description of changes - this will be included in release notes -->
<!-- 
Example:
- Added new user authentication module
- Implemented OAuth2 login flow
- Added password reset functionality
- Updated user profile management
-->

### Breaking Changes
<!-- List any breaking changes - these will be highlighted in release notes -->
- [ ] No breaking changes
- [ ] Breaking changes (use `BREAKING CHANGE:` in commit message):
  ```
  [Describe breaking changes and migration steps]
  
  Example:
  - API endpoint /v1/users changed to /v2/users
  - Database schema migration required
  - Environment variable AUTH_TOKEN renamed to API_TOKEN
  ```

### Impact
<!-- Who/what is affected by this change? -->
- **Affected Modules**: <!-- List modules/apps affected -->
- **User Impact**: <!-- How does this affect end users? -->
- **Performance Impact**: <!-- Any performance improvements/degradations? -->

### Related PRs/Issues
<!-- Link related PRs or issues for context -->
- Related to #<!-- issue number -->
- Closes #<!-- issue number -->
- Part of #<!-- epic or feature issue --> 

---

## 📋 Production Merge Readiness Checklist

### Level 1: Peer Review - Coding Standards and Business Logic

- [ ] **1.1** Code reviewed by at least one peer (preferably senior)
  - Reviewer: <!-- AUTO-FILLED: @reviewer -->
  - Review Date: <!-- AUTO-FILLED: YYYY-MM-DD -->

- [ ] **1.2** All reviewer comments resolved and approved
  - [ ] All comments addressed
  - [ ] Reviewer approval received

- [ ] **1.3** Coding standards and naming conventions followed
  - [ ] Pre-commit hooks passed
  - [ ] CI checks passed
  - [ ] No linting errors

- [ ] **1.4** Sensitive logic or configurations documented
  - [ ] Security-sensitive code documented
  - [ ] Configuration changes documented
  - [ ] Environment variables documented (if any)

- [ ] **1.5** Screenshots or review notes attached in PR
  - [ ] UI changes: Screenshots attached
  - [ ] Complex logic: Review notes attached
  - [ ] N/A (no UI/logic changes)

---

### Level 2: QA Certification - Functional, Edge, and Regression Testing

- [ ] **2.1** Code deployed to staging/UAT environment
  - Staging URL: ________________
  - Deployment Date: ________________

- [ ] **2.2** Test cases executed and test logs/reports attached
  - [ ] Unit tests passed
  - [ ] Integration tests passed
  - [ ] E2E tests passed (if applicable)
  - Test Report: [Link/Attachment]

- [ ] **2.3** No high/critical bugs pending
  - [ ] All critical bugs resolved
  - [ ] All high-priority bugs resolved
  - Bug Tracker Reference: ________________

- [ ] **2.4** Known issues listed with severity & fix plan
  - [ ] No known issues
  - [ ] Known issues documented below:
    ```
    Issue 1: [Description]
    Severity: [Critical/High/Medium/Low]
    Fix Plan: [Description or Ticket #]
    ```

- [ ] **2.5** Regression testing completed for impacted areas
  - [ ] Regression test suite executed
  - [ ] Impacted areas verified
  - Regression Test Report: [Link/Attachment]

---

### Level 3: Release Authorization - Deployment Planning

> **Note**: Level 3 items are required only for production deployments. For merges to `develop` or `staging`, these can be deferred.

- [ ] **3.1** Deployment plan prepared and reviewed
  - [ ] Deployment plan attached/generated
  - [ ] Plan reviewed by Team Lead
  - Deployment Plan: [Link/Attachment]

- [ ] **3.2** Rollback steps documented and verified
  - [ ] Rollback script prepared
  - [ ] Rollback steps verified by DevOps
  - Rollback Plan: [Link/Attachment]

- [ ] **3.3** Downtime estimate and mitigation plan provided
  - Estimated Downtime: ________________
  - Mitigation Plan: ________________

- [ ] **3.4** Stakeholders informed and communication plan ready
  - [ ] Stakeholders notified
  - [ ] Communication plan prepared
  - Release Request ID: ________________

- [ ] **3.5** Go/No-Go decision recorded in tracker
  - [ ] Decision recorded
  - Tracker Reference: ________________

---

## 📝 PR Details

### Type of Change
- [ ] 🐛 Bug fix
- [ ] ✨ New feature
- [ ] 🔧 Refactoring
- [ ] 📚 Documentation update
- [ ] ⚡ Performance improvement
- [ ] 🔒 Security fix
- [ ] 🧪 Test addition/update

### Related Issues/Tickets
<!-- Link to related issues, tickets, or BRD -->
- Closes #________________
- Related to #________________
- Bitrix/Ticket: ________________

### Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] E2E tests added/updated
- [ ] Manual testing completed

### Documentation
- [ ] Code comments added/updated
- [ ] README updated
- [ ] API documentation updated
- [ ] User guide updated (if applicable)
- [ ] Documentation link: ________________

### Screenshots (if applicable)
<!-- Add screenshots for UI changes -->

### Deployment Notes
<!-- Any special deployment instructions or considerations -->

### Rollback Plan
<!-- Brief description of rollback steps if needed -->

---

## ✅ Pre-Merge Checklist

- [ ] All CI checks passed
- [ ] Code reviewed and approved
- [ ] Tests passing
- [ ] Documentation updated
- [ ] No merge conflicts
- [ ] Branch is up to date with target branch

---

## 🚀 Release Request (Production Only)

> **For production deployments**: Use the Release Request Sender Tool to generate a release request.

- [ ] Release Request created via Release Request Sender Tool
- [ ] Request ID: ________________
- [ ] All Level 3 items completed

---

**Powered by [Dhwani RIS](https://dhwaniris.in)**

