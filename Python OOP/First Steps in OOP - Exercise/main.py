class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if language != self.language:
            return f"{self.name} does not know {language}"
        self.skills += skills_earned
        return f"{self.name} watched {course_name}"

    def change_language(self, new_language, skills_needed):
