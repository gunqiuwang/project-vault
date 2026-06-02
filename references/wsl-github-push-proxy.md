# WSL + GitHub Push Proxy Fix

## Problem

WSL cannot reach Windows proxy (v2ray/Clash at 127.0.0.1:10808) because `127.0.0.1` in WSL refers to WSL itself, not Windows host.

The Windows host IP (from `/etc/resolv.conf` or `ip route show default`) often doesn't have the proxy listening on LAN.

## Solutions

### Option 1: v2ray Allow LAN (Recommended)

Enable "Allow LAN" in v2ray settings. Then from WSL:
```bash
export https_proxy=http://$(ip route show default | awk '{print $3}'):10808
git push origin master
```

### Option 2: PowerShell git proxy (Quick Fix)

```powershell
powershell.exe -Command "
git config --global http.proxy http://127.0.0.1:10808
git config --global https.proxy http://127.0.0.1:10808
cd 'C:\Users\YOU\Desktop\repo-copy'
git push origin master
git config --global --unset http.proxy
git config --global --unset https.proxy
"
```

### Option 3: Copy to Windows Desktop + Push

```bash
cp -r ~/project "/mnt/c/Users/YOU/Desktop/pv-push"
powershell.exe -Command "
cd 'C:\Users\YOU\Desktop\pv-push'
git remote add origin https://github.com/user/repo.git
git push origin master
"
rm -rf "/mnt/c/Users/YOU/Desktop/pv-push"
```

## Key Insight

WSL `ln -sf` symlinks AND network proxy both require special handling for WSL→Windows interop. Always test cross-boundary operations.
