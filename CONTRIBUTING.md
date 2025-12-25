# Contributing to ALICE's Temporal Funhouse

Thank you for your interest in contributing! This project welcomes contributions from researchers, developers, and AI enthusiasts.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
3. [Development Setup](#development-setup)
4. [Contribution Types](#contribution-types)
5. [Submission Guidelines](#submission-guidelines)
6. [Testing Requirements](#testing-requirements)
7. [Documentation Standards](#documentation-standards)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of:
- Experience level
- Background
- Identity
- Research approach

### Expected Behavior

- Be respectful and constructive in discussions
- Focus on technical merit and research validity
- Welcome diverse approaches to testing AI systems
- Give credit where credit is due
- Respect different perspectives on AI capabilities

### Unacceptable Behavior

- Harassment or discriminatory comments
- Bad faith criticism
- Sharing others' private information
- Plagiarism or misrepresentation of results

---

## How to Contribute

### 1. Report Bugs

**Before submitting**:
- Check existing issues to avoid duplicates
- Verify the bug with the latest version

**Bug Report Template**:
```markdown
**Description**: Brief description of the issue

**To Reproduce**:
1. Step 1
2. Step 2
3. Expected vs actual behavior

**Environment**:
- Python version:
- OS:
- AI player used:

**Logs/Output**:
```
(Paste relevant output)
```
```

### 2. Suggest Enhancements

We welcome ideas for:
- New extreme protocols
- Improved scoring metrics
- Better AI player implementations
- Documentation improvements

**Enhancement Template**:
```markdown
**Feature**: Brief description

**Motivation**: Why is this useful?

**Proposed Implementation**:
- Technical approach
- Potential challenges
- Expected impact

**Alternatives Considered**:
```

### 3. Submit Code

See [Submission Guidelines](#submission-guidelines) below.

---

## Development Setup

### Prerequisites

```bash
# Python 3.8 or higher
python --version

# Virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone git@github.com:YOUR_USERNAME/Alice_Temporal_Funhouse.git
cd Alice_Temporal_Funhouse

# Add upstream remote
git remote add upstream git@github.com:ext-sakamoro/Alice_Temporal_Funhouse.git
```

### Create a Branch

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/bug-description
```

---

## Contribution Types

### 1. New AI Player Implementation

**What we're looking for**:
- Integration with different LLM providers (OpenAI, Anthropic, Google, Cohere, etc.)
- Novel AI architectures (reinforcement learning, evolutionary algorithms, etc.)
- Baseline implementations (MinimaxAI, AlphaBetaAI, etc.)

**Checklist**:
- [ ] Inherits from `SimpleAI` or `LLMAIBase`
- [ ] Implements `think_and_move(gm)` method
- [ ] Handles invalid moves gracefully
- [ ] Includes docstring with usage example
- [ ] Tested on at least one protocol

**Example**:
```python
from simple_ai_players import LLMAIBase

class YourLLMPlayer(LLMAIBase):
    """
    AI player using [Your LLM Provider]

    Usage:
        player = YourLLMPlayer(color='B', api_key='...', model='...')
    """
    def __init__(self, color: str, api_key: str, model: str = "default-model"):
        super().__init__(color, model)
        # Your initialization

    def _call_llm_api(self, prompt: str) -> str:
        # Your LLM API call
        pass
```

### 2. New Protocol

**What we're looking for**:
- Protocols that test unexplored AI capabilities
- Clear theoretical motivation
- Measurable success criteria

**Checklist**:
- [ ] Protocol class with clear mechanics
- [ ] Scoring function with 3+ metrics
- [ ] Documentation in `docs/PROTOCOLS.md`
- [ ] Test results with at least one AI player
- [ ] Justification for why this tests diverse AI capabilities

**Template**:
```python
class YourProtocol:
    """
    Protocol Name: [Your Protocol]

    Target Capability: [What this tests]

    Mechanics:
    - [Mechanic 1]
    - [Mechanic 2]
    """
    def __init__(self):
        pass

    def run(self, ai_black, ai_white):
        """Run the protocol"""
        pass

    def calculate_score(self, history):
        """Calculate scores"""
        return {
            'metric_1': ...,
            'metric_2': ...,
            'metric_3': ...,
            'overall': ...
        }
```

### 3. Scoring Improvements

**What we're looking for**:
- More accurate metrics for existing protocols
- New evaluation dimensions
- Statistical validation of scoring systems

**Checklist**:
- [ ] Clear definition of what you're measuring
- [ ] Justification for metric choice
- [ ] Comparison with previous scoring
- [ ] Test results showing improvement

### 4. Documentation

**What we're looking for**:
- Clearer explanations of protocols
- More integration examples
- Tutorials for specific use cases
- Research insights

**Types**:
- Conceptual guides (how protocols work)
- How-to guides (step-by-step instructions)
- API references (technical details)
- Research notes (insights and analysis)

---

## Submission Guidelines

### Pull Request Process

1. **Update your fork**:
```bash
git fetch upstream
git rebase upstream/main
```

2. **Make your changes**:
```bash
# Edit files
git add .
git commit -m "feat: Add YourFeature"
```

3. **Push to your fork**:
```bash
git push origin feature/your-feature-name
```

4. **Open Pull Request**:
- Go to GitHub and create PR
- Fill out PR template (see below)
- Link related issues

### PR Template

```markdown
**Description**:
Brief description of changes

**Type of Change**:
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

**Testing**:
- [ ] Tested locally
- [ ] Added test cases
- [ ] All tests pass

**Checklist**:
- [ ] Code follows project style
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] Commit messages are clear

**Results** (for new AI players or protocols):
```
Protocol: RETRO
Score: 75.5/100
AI: MyNewPlayer
```
```

### Commit Message Guidelines

Use conventional commits format:

```
type(scope): subject

[optional body]

[optional footer]
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code refactoring
- `test`: Test additions/changes
- `perf`: Performance improvements

**Examples**:
```bash
feat(ai): Add OpenAI GPT-4 integration
fix(retro): Fix Phase G history reconstruction
docs(protocols): Update BABEL protocol specification
refactor(scoring): Improve temporal_reasoning metric
```

---

## Testing Requirements

### Running Tests

```bash
# Run all protocols
python alice_temporal_funhouse.py --protocol all

# Run specific protocol
python alice_temporal_funhouse.py --protocol retro

# With your AI player (requires modification)
# See docs/API_INTEGRATION.md
```

### Expected Output

Your contribution should not break existing tests:

```bash
# All protocols should complete without errors
# Scores should be in range [0, 100]
# JSON output should be valid
```

### Performance Benchmarks

For new AI players, include performance data:

| Protocol | Score | Time per Move | Total Time |
|----------|-------|---------------|------------|
| BABEL | 85.5 | 1.2s | 58s |
| Schrödinger | 78.0 | 1.5s | 72s |
| RETRO | 82.0 | 1.8s | 90s |
| CONCEPT | 70.5 | 1.3s | 65s |

---

## Documentation Standards

### Code Documentation

```python
def your_function(param1: str, param2: int) -> dict:
    """
    Brief description of what this does.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Dictionary containing:
        - key1: Description
        - key2: Description

    Example:
        >>> result = your_function("test", 42)
        >>> print(result)
        {'key1': 'value1', 'key2': 'value2'}
    """
    pass
```

### Markdown Documentation

- Use clear headings (H1 for title, H2 for sections)
- Include code examples with syntax highlighting
- Add tables for comparisons
- Link to related documentation

---

## Research Contributions

### Publishing Results

If you publish research using this test suite:

1. **Cite the project**:
```bibtex
@software{temporal_funhouse,
  title={Temporal Funhouse: Extreme Protocols for AI Testing},
  author={Context Drift Research Team},
  year={2025},
  url={https://github.com/ext-sakamoro/Alice_Temporal_Funhouse}
}
```

2. **Share your results**:
- Open an issue with your findings
- Include link to paper/preprint
- Share protocol scores and insights

3. **Contribute datasets**:
- Share game logs
- Share scoring data
- Share failure cases

---

## Recognition

### Contributors

All contributors will be acknowledged in:
- `README.md` contributors section
- Release notes for their contributions
- Research papers citing specific contributions

### Types of Recognition

- **Code Contributors**: Listed in GitHub contributors
- **Research Contributors**: Cited in papers
- **Documentation Contributors**: Credited in docs
- **Bug Reporters**: Mentioned in changelogs

---

## Questions?

- **General Questions**: Open a GitHub Discussion
- **Bug Reports**: Open an issue with bug template
- **Feature Requests**: Open an issue with enhancement template
- **Security Issues**: Email (see SECURITY.md - to be created)

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## Getting Help

### Resources

- **Documentation**: See `docs/` folder
- **Examples**: See `examples/` folder
- **API Guide**: See `docs/API_INTEGRATION.md`
- **Protocol Specs**: See `docs/PROTOCOLS.md`

### Community

- **GitHub Discussions**: Ask questions, share ideas
- **Issues**: Report bugs, request features

---

## Thank You!

Your contributions help advance our understanding of AI diversity, temporal reasoning, and value alignment.

**Welcome to the Funhouse!** 🎪

---

**Last Updated**: 2025-12-25
**Version**: 1.0.0
