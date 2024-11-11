class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors_str = "\n".join(f"- {author}" for author in self.authors) if self.authors else "-"
        
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description or '-'}\n"
            f"License: {self.license or '-'}\n\n"
            f"Authors:\n{authors_str}\n\n"
            f"Dependencies:\n{self._stringify_dependencies(self.dependencies)}\n\n"
            f"Development dependencies:\n{self._stringify_dependencies(self.dev_dependencies)}"
        )
