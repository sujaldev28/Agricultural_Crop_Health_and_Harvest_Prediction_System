name: Bug report
description: Create a report to help us improve
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Thank you for reporting a bug. Please fill in the details below.
  - type: textarea
    id: description
    attributes:
      label: Bug Description
      description: A clear and concise description of what the bug is.
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: Steps to Reproduce
      description: Describe how we can reproduce the behavior.
      placeholder: |
        1. Go to '...'
        2. Call method '...'
        3. See error
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Expected Behavior
      description: A clear description of what you expected to happen.
    validations:
      required: true
