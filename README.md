SublimeModest
=============

A Sublime Text 3 plugin for the modeling language Modest.
For Modest itself, see http://www.modestchecker.net .

Installation
------------
This plugin is not available in the package manager at the moment. 

- Navigate to your `Packages` folder (for example `C:\Users\<X>\AppData\Roaming\Sublime Text 3\Packages` for Windows). 
- Run `git clone https://github.com/MarkusBauer/SublimeModest.git Modest` there and you're done.

Tool paths
----------
If the **Modest tools** are not in your PATH, you have to tell the plugin where they are located. 

- Create a `Packages/User/Modest.sublime-settings` file (menu: Preferences &rArr; Package Settings &rArr; Modest &rArr; Settings - User). 
- Copy and paste the example configuration file `Modest.sublime-settings` there (menu: Preferences &rArr; Package Settings &rArr; Modest &rArr; Settings - Example). 
- Now insert the path to your modest tools directory. Save.

Remember that paths must be written using double backslash (`\\`) for Windows. 


If modest does not find your **Dot** installation, you have to edit the `mosta.exe.config` file, located in your Modest tools directory. The relevant section will look like this:

	<setting name="DotPath" serializeAs="String">
		<value>C:\Program Files (x86)\GraphViz\bin\dot.exe</value>
	</setting>

