# Password Strength Checker

A command-line Python program that checks whether a password meets a set of basic security requirements.

## About This Project

I built this as part of preparing to apply to Georgia State University's MSIS program, with a planned concentration in Cybersecurity. It's part of a larger effort to build technical projects in areas I want to study further.

The goal was to take concepts from LinkedIn Learning's *Python Essential Training* — variables, loops, conditionals, and boolean logic — and apply them to a problem with real security relevance, while keeping the scope small enough that I could fully understand and explain every line.

## How It Works

The program asks the user to enter a password, then checks it against the following rules:

- **Minimum length of 8 characters** (the widely adopted baseline)
- **At least one uppercase letter**
- **At least one lowercase letter**
- **At least one number**
- **At least one special character** from a defined set
- **No whitespace characters**

For each failed rule, the program prints a message telling the user what's missing. After all checks complete, it gives a final verdict: *"Your password is strong"* if every rule passed, or *"Your password is weak"* otherwise.

## Design Choices

A few decisions worth calling out:

- **Minimum length of 8.** This is the universally adopted baseline. NIST recommends 12+ for higher-security contexts. The threshold can be raised by changing one value.
- **Single-pass loop.** The program walks through the password only once and checks all the character-based rules in parallel, instead of running a separate loop for each one. This is more efficient and avoids repeating the same logic.
- **Explicit special character set.** Python doesn't have a built-in `.isspecial()` method because what counts as "special" varies by application, so the accepted characters are defined directly in the code.
- **Independent rule checks.** Each rule is checked separately so the user sees all the reasons their password failed at once, instead of fixing one rule only to be told about another on the next try.

## How to Run

This program runs from the command line and requires Python 3.

```bash
python3 password_checker.py
```

You'll be prompted to enter a password. The program will then print any rule failures followed by a strength verdict.

## What I Learned

Two things stood out from building this:

The first was a small but real habit: **always save the file before running it.** I lost time more than once chasing a bug that wasn't actually a bug — the code in front of me on screen wasn't the code the terminal was running, because I hadn't saved my changes. Learning to check the state of things (is the file saved? is the terminal pointing at the right folder?) before assuming the code is wrong was a useful debugging instinct to build early.

The second was watching my own intuition build through repetition. The first time I wrote the flag-and-loop pattern (for uppercase letters), I was translating each line from English to Python piece by piece. By the fifth time I wrote a version of it, I was reaching for the pattern automatically — I even added a check for whitespace characters that wasn't in the original plan, because the structure had become familiar enough that adapting it to a new rule felt natural. That shift from *thinking about* code to *thinking in* code was unexpected and is the part I want to keep building on.

## Possible Improvements

A few things I'd add to a future version of this project:

- **A strength scale instead of a yes/no verdict.** Right now the program just says strong or weak. A more useful version would count how many rules pass and assign a level — weak, medium, strong, very strong — similar to the strength meters you see when signing up for an account.

- **A retry loop.** Right now if the password is weak, the program ends and you have to run it again to try a new one. A real tool would keep asking until the user provides a strong password.

- **A check against commonly used passwords.** A password like `Password1!` technically passes every rule in this program, but it's also one of the most-hacked passwords in existence. A future version would compare the input against a known list of weak or breached passwords.

- **Hidden input as the user types.** Right now the password is visible on screen as it's typed. Python's `getpass` module would hide it, which is closer to how real authentication systems handle password entry.
