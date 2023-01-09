# List all currently installed packages in the machine
pip list

# Install a specific package
pip install <package_name>

# Install a specific version of the package - Use semantic version - 1.2.4
pip install <package_name>==<Semantic_Version>

# Uninstall a package
pip uninstall <package_name>

# Install the latest compatible version, here * indicates to install the latest patch version
# For example, if we have 3 version 2.3.0, 2.3.1, 2.3.2, then 2.3.2 will be installed, since it
# is the latest patch version
pip install <package_name>==2.3.*

# Alternative syntax:
pip install <package_name>~=2.3.*

# Similarly we can install the latest compatible minor version version 
pip install <package_name>~=2.*

#################### pipenv Commands ###################

# Install all dependencies
pipenv install

# Install a package
pipenv install <package_name>

# Uninstall a package
pipenv uninstall <package_name>

# Install all dependencies of a project i.e. install packages listed on Pipfile
pipenv install

# Update a package
pipenv update <package_name>

# Update all packages in a project
pipenv update --outdated

# List all dependencies of a package
pipenv graph

# View documentation of modules built-in or custom modules:
pydoc <module_name>

# Start pydoc server to view docs of all modules
pydoc -p <port_number>

# Write docstring content to html
pydoc -w <module_name>
# ex: pydoc document_strings.image_converter