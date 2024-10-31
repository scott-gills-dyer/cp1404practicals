
from programming_language import ProgrammingLanguage


def main():
    """Program to print python class and print dynamic languages."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]
    print(f"The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()