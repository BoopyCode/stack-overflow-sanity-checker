#!/usr/bin/env python3
"""
Stack Overflow Sanity Checker
Because copy-pasting code you don't understand is like performing surgery
by watching a 30-second TikTok tutorial.
"""

import re
import sys
import random
from pathlib import Path

# The sacred texts of Stack Overflow
SUSPICIOUS_PATTERNS = [
    (r'\beval\b', "Found 'eval' - Congratulations, you've installed a backdoor!"),
    (r'\bexec\b', "Found 'exec' - Your code now runs arbitrary code. What could go wrong?"),
    (r'\bimport\s*\*', "Wildcard import detected - Namespace pollution incoming!"),
    (r'\bassert\s*True', "Asserting True - The programmer's equivalent of 'This statement is false'"),
    (r'\bwhile\s*True:', "Infinite loop found - Your CPU sends its regards"),
    (r'\bfrom\s+os\s+import\s+system', "Direct system calls - Because security is someone else's problem"),
    (r'\b\d{4}-\d{2}-\d{2}\b', "Hardcoded date - This code expires like milk"),
    (r'# TODO:', "TODO comment - Future you will hate present you"),
    (r'\bpass\b', "'pass' statement - The programming equivalent of shrugging"),
]

# Wisdom from the ancients
QUOTES = [
    "Understanding the code is optional, but suffering the consequences is mandatory.",
    "This code works on my machine™",
    "If it's stupid but it works, it's still stupid and you're lucky.",
    "You're not a real developer until you've debugged someone else's Stack Overflow code at 3 AM.",
]


def check_file(filepath):
    """Scans a file for suspicious Stack Overflow patterns."""
    try:
        content = Path(filepath).read_text()
    except Exception as e:
        print(f"Failed to read {filepath}: {e}")
        return
    
    issues = []
    for pattern, warning in SUSPICIOUS_PATTERNS:
        if re.search(pattern, content):
            issues.append(warning)
    
    if issues:
        print(f"\n🔍 Checking: {filepath}")
        print(f"Found {len(issues)} potential issue(s):")
        for issue in issues:
            print(f"  ⚠️  {issue}")
        print(f"\n💡 Wisdom: {random.choice(QUOTES)}")
    else:
        print(f"✅ {filepath} looks... suspiciously clean. Did you actually write this?")


def main():
    """Main function - because every script needs one, apparently."""
    if len(sys.argv) < 2:
        print("Usage: python stack_sanity.py <file1.py> [file2.py ...]")
        print("Example: python stack_sanity.py my_questionable_code.py")
        sys.exit(1)
    
    print("🧠 Stack Overflow Sanity Checker")
    print("=" * 40)
    
    for filepath in sys.argv[1:]:
        check_file(filepath)


if __name__ == "__main__":
    main()
