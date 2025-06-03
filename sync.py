import os
from repo_dir_sync import LibRepo, OtherRepo

r = LibRepo()
r.add(OtherRepo("serena", "serena", os.path.join("..", "serena", "src", "interprompt")))
r.runMain()
