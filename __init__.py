import subprocess, os

try:
	# On importe tout
	from ssh_lib.ssh_lib import ssh_client
except ModuleNotFoundError:
	# Si module non trouvé, on installe les dépendances
	subprocess.run(f"pip install --no-cache-dir -r {os.path.dirname(os.path.realpath(__file__))}/requirements.txt", shell=True)
	from ssh_lib.ssh_lib import ssh_client