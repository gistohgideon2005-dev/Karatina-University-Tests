## Purpose
This file gives AI coding assistants immediate, actionable context for working in this repository (a Katalon Studio test project).

## Quick project overview
- Project type: Katalon Studio test project (migratedVersion: 5.9.0).
- Tests live as Groovy scripts under `Scripts/` and as Test Suites under `Test Suites/`.
- Page elements are stored in the Katalon Object Repository under `Object Repository/` and referenced with paths such as `library/users/student/Karu_Student_Portal_login/Page_KarU  Log in/input_Password_ctl00MainContenttxtpass`.

## What matters for code changes
- Changing a repository path or test object name will break `findTestObject(...)` calls across scripts; prefer renaming with cross-file updates.
- Encrypted credentials appear in scripts via `WebUI.setEncryptedText(..., '<ciphertext>')`. Do not replace these strings with plain text; use Katalon's encryption helper if updating.
- Tests reference UI objects by repository path (forward-slash separated). Use exact path strings from `Object Repository/` when creating or updating tests.

## Where to look (key files / folders)
- Project definition: `Karatina-University-Tests.prj` (shows `migratedVersion` and include folders).
- Scripts: `Scripts/library/...` (auto-generated Groovy test scripts).
- Test suites: `Test Suites/...` (example: `Test Suites/Karatina University/KarU_Student_Portal.groovy`).
- Object repository: `Object Repository/...` (UI selectors and test object metadata).
- Profiles: `Profiles/default.glbl` (global variables; currently empty).
- Reports: `Reports/...` (execution outputs and `execution.properties`).

## How to run tests (examples)
- Using Katalon Studio GUI: open the project folder in Katalon and run Test Suites from the Test Explorer.
- Using Katalon Console (example):

```
katalon -noSplash -runMode=console -projectPath="/path/to/Karatina-University-Tests" \
  -retry=0 -testSuitePath="Test Suites/Karatina University/KarU_Student_Portal" \
  -executionProfile="default" -browserType="Chrome"
```

Adjust `-projectPath` and `-testSuitePath` to the environment. This repo's Test Suite name includes a space (`Karatina University`), so quote paths when passing to the CLI.

## Project-specific patterns & conventions
- Folder naming: `library/users/<role>/<flow>/...` — maps test objects and scripts by user role and high-level flow.
- Script files are named `Script<timestamp>.groovy` under `Scripts/...` and are often simple sequences of `WebUI.*` calls.
- Test suites use annotations `@SetUp`, `@TearDown`, and `@SetupTestCase` for lifecycle hooks; many are stubbed with `skipped = true` (enable only when needed).

## Integration & external dependencies
- The project targets standard web UI tests via Selenium (see `console.properties` remoteWebDriverType).
- No explicit external build tooling (Maven/Gradle) is present — Katalon Studio handles build/execution.

## Safe-edit rules for AI edits
- Do not alter `setEncryptedText` ciphertexts or try to 'decrypt' them in code edits.
- When renaming or moving `Object Repository` entries, update all `findTestObject(...)` references across `Scripts/` and `Test Cases/`.
- Preserve `Test Suites/` test suite structure and `@*` annotations unless updating lifecycle behavior deliberately.

## Examples from this repo
- Login flow (script): `Scripts/library/Users/student/login/Student_Portal_login_test_case/Script1616084043913.groovy` — shows `openBrowser`, `navigateToUrl`, `click`, `setText`, and `setEncryptedText` usage.
- Test suite example: `Test Suites/Karatina University/KarU_Student_Portal.groovy` — contains suite-level lifecycle hooks.

## If you need more
If anything here is ambiguous, ask for the target task (e.g., "update selector X", "add a new test for Y") and indicate whether you can run Katalon locally or need purely static changes.

---
Edit notes: this project is a Katalon-generated structure; prefer Katalon Studio or its console runner for executing and validating changes.
