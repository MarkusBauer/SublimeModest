import sublime, sublime_plugin
import Default

class BuildmodestCommand(Default.exec.ExecCommand):
	def run(self, **kwargs):
		s = sublime.load_settings("Modest.sublime-settings")
		path = s.get("modest_path", "");
		# terminating / or \\
		if (path != "" and path[-1] != "/" and path[-1] != "\\"):
			if ("\\" in path):
				path += "\\"
			else:
				path += "/"
		# add the path to the command
		if (path != ""):
			cmd = kwargs["cmd"]
			cmd[0] = path + cmd[0]
			print("EXECUTABLE: " + cmd[0])
			kwargs["cmd"] = cmd
		super().run(**kwargs)
