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

### Option 3: Copy to Windows Desktop + Push (Most Reliable)

```bash
cp -r ~/project "/mnt/c/Users/YOU/Desktop/pv-push"
powershell.exe -Command "
cd 'C:\Users\YOU\Desktop\pv-push'
git config --global http.proxy http://127.0.0.1:10808
git config --global https.proxy http://127.0.0.1:10808
\$token = gh auth token
git push https://user:\$token@github.com/user/repo.git master --force
git config --global --unset http.proxy
git config --global --unset https.proxy
"
rm -rf "/mnt/c/Users/YOU/Desktop/pv-push"
```

### Option 4: When git push says "Repository not found" but repo exists

This happens when the credential helper fails with the proxy. Fix: embed token in URL.

```powershell
powershell.exe -Command "
git config --global http.proxy http://127.0.0.1:10808
git config --global https.proxy http://127.0.0.1:10808
gh auth setup-git 2>&1
\$token = gh auth token
cd 'C:\Users\YOU\Desktop\repo'
git push https://user:\$token@github.com/user/repo.git master --force
git config --global --unset http.proxy
git config --global --unset https.proxy
"
```

If that also fails, the repo may have been deleted. Verify with:
```powershell
gh repo list --limit 5 --json name
```
Then recreate if needed:
```powershell
gh repo create repo-name --public --source=. --push
```

## Key Insight

WSL `ln -sf` symlinks AND network proxy both require special handling for WSL→Windows interop. Always test cross-boundary operations. The `gh auth setup-git` command configures git to use gh's credential helper, which often fixes "Repository not found" errors.
