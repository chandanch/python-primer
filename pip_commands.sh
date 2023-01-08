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

