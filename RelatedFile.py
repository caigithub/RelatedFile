import sublime, sublime_plugin
import util 

class RelatedFileCommand(sublime_plugin.WindowCommand):
    def run(self, suggests=[]):
        if not self.window.active_view():
            return

        path = self.window.active_view().file_name()
        if not path:
            return

        self.window.open_file( util.getNextFile(path, suggests ) )

        #sublime.status_message("No file to switch found in directories of opened files, showing the Goto menu.")
        #self.window.run_command("show_overlay", {"overlay": "goto", "text": base})

        return


class RelatedFileListCommand(sublime_plugin.WindowCommand):
    def run(self, suggests=[]):
        if not self.window.active_view():
            return

        path = self.window.active_view().file_name()
        if not path:
            return

        self.window.run_command("show_overlay", {"overlay": "goto", "text": util.getNextFileKeyword( path, suggests )})
        return

