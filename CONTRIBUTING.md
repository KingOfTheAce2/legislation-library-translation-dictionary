# Contributing to Dutch Civil Procedure Legal Dictionary

Thank you for your interest in contributing! This project aims to provide high-quality, open-access legal translation resources. All contributions are welcome.

## 🎯 Ways to Contribute

### 1. Report Issues
Found an error or inconsistency?
- Check if the issue already exists
- Open a new issue with detailed information
- Include the specific term and suggested correction

### 2. Suggest New Terms
Missing important civil procedure terms?
- Check if the term already exists in the dictionary
- Provide context where the term is used
- Suggest an English translation
- Include sources or references if possible

### 3. Improve Translations
Better translation for existing terms?
- Explain why the current translation should be improved
- Provide context and usage examples
- Reference authoritative sources
- Consider regional variations

### 4. Enhance the Website
Technical improvements welcome!
- UI/UX enhancements
- New features (export, print, etc.)
- Performance optimizations
- Accessibility improvements
- Mobile experience

## 📋 Contribution Guidelines

### Quality Standards

All contributions must meet these standards:

1. **Accuracy**
   - Translations must be legally accurate
   - Prefer established legal terminology
   - Maintain consistency with existing terms

2. **Context**
   - Provide context for ambiguous terms
   - Include parenthetical clarifications when needed
   - Example: "aanbrengen (een geschil bij de rechter)"

3. **Attribution**
   - Credit original sources
   - Maintain author information
   - Respect existing licenses

4. **SME Review**
   - Significant changes should be reviewed by legal experts
   - Mark new terms as pending review if not yet verified
   - Seek feedback from practitioners

### Data Format

When adding or modifying terms, follow this JSON structure:

```json
{
  "source": "Dutch term here",
  "lang-source": "nl-nl",
  "target": "English translation here",
  "lang-target": "en-gb",
  "author": "Your Name / Team",
  "license": "CC BY 4.0",
  "sme-reviewed": "yes" or "pending"
}
```

**Required fields:**
- `source`: Dutch term (lowercase, with context in parentheses if needed)
- `lang-source`: Always "nl-nl"
- `target`: English translation
- `lang-target`: "en-gb" or "en-us"
- `author`: Your name or attribution
- `license`: Must be compatible with CC BY 4.0
- `sme-reviewed`: "yes" if expert-reviewed, "pending" if not

### JSON Guidelines

- Maintain alphabetical order by source term
- Use consistent formatting (2-space indentation)
- Validate JSON before submitting
- Keep the file structure clean

## 🔄 Contribution Process

### For Small Changes (1-5 terms)

1. **Fork the repository**
2. **Edit the JSON file** (`Glossary-of-Dutch-Procedural-Terminology.json`)
3. **Test your changes** - open `index.html` locally
4. **Submit a Pull Request** with:
   - Clear description of changes
   - Justification for modifications
   - Sources or references

### For Large Changes (6+ terms)

1. **Open an issue first** to discuss the scope
2. **Get feedback** from maintainers
3. **Follow the process above** once approved

### For Technical Changes

1. **Test thoroughly** across browsers
2. **Maintain backward compatibility**
3. **Document new features** in README
4. **Keep dependencies minimal**

## ✅ Pull Request Checklist

Before submitting a PR, ensure:

- [ ] JSON is valid (use a validator like jsonlint.com)
- [ ] Terms are alphabetically ordered
- [ ] All required fields are present
- [ ] Attribution is correct
- [ ] License is compatible (CC BY 4.0)
- [ ] Changes are tested locally
- [ ] Description explains the changes
- [ ] Sources are cited where applicable

## 👥 Review Process

1. **Submission**: Submit your PR with detailed description
2. **Initial Review**: Maintainers check format and guidelines
3. **SME Review**: Legal experts review translations (if applicable)
4. **Feedback**: Address any comments or requested changes
5. **Approval**: PR is merged once approved

## 🤝 Community Guidelines

### Be Respectful
- Respect different perspectives on translations
- Legal terminology can have regional variations
- Be constructive in feedback

### Collaborate
- Seek consensus on controversial translations
- Share knowledge and resources
- Help others with their contributions

### Quality Over Quantity
- Focus on accuracy, not speed
- One well-researched term is better than ten questionable ones
- Take time to verify translations

## 📚 Resources

### Dutch Legal Resources
- [Wetten.overheid.nl](https://wetten.overheid.nl/) - Official legal texts
- [Rechtspraak.nl](https://www.rechtspraak.nl/) - Dutch judiciary
- [Dutch Civil Code (translated)](https://www.dutchcivillaw.com/)

### Translation Resources
- [JIAMCATT Legal Glossary](https://www.jiamcatt.org/)
- [EU Terminology Database](https://iate.europa.eu/)
- [UN Term Portal](https://unterm.un.org/)

### Style Guides
- Preference for British English (en-gb)
- Follow established legal translation conventions
- Maintain consistency within the dictionary

## 🎓 For Legal Students

Want to contribute as a learning experience?

1. **Start small**: Suggest improvements to 1-2 terms
2. **Cite your sources**: Reference textbooks, cases, or statutes
3. **Ask questions**: Open discussions if unsure
4. **Get mentorship**: Connect with experienced legal translators

## 💡 Feature Requests

Have ideas for new features?

1. Check existing issues for similar requests
2. Open a new issue labeled "enhancement"
3. Describe the feature and its benefits
4. Be open to discussion and refinement

## 🐛 Bug Reports

Found a bug on the website?

1. Check if it's already reported
2. Include:
   - Browser and version
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable

## 📄 License

By contributing, you agree that your contributions will be licensed under CC BY 4.0, the same license as the project.

### What This Means
- Your contributions will be freely available
- Attribution will be given
- Others can build upon your work
- Commercial use is permitted with attribution

## ❓ Questions?

- **General questions**: Open a discussion on GitHub
- **Technical issues**: Open an issue
- **Private inquiries**: Contact maintainers via email

## 🙏 Thank You!

Every contribution, no matter how small, helps make legal knowledge more accessible. Thank you for being part of this project!

---

**Remember**: Accuracy and quality are paramount in legal translation. When in doubt, ask for review rather than guessing.
