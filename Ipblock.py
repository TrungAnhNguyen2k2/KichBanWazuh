import subprocess

ipdes = "172.25.16.40/32"
print(ipdes)

inbound_args = [
    "netsh", "advfirewall", "firewall", "add", "rule", "name=MyRuleInbound",
    "dir=in", "action=block", "enable=yes", f"remoteip={ipdes}"
]
subprocess.run(inbound_args, shell=True)

outbound_args = [
    "netsh", "advfirewall", "firewall", "add", "rule", "name=MyRuleOutbound",
    "dir=out", "action=block", "enable=yes", f"remoteip={ipdes}"
]
subprocess.run(outbound_args, shell=True)
