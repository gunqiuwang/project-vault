# WSL → GitHub Push Pattern

WSL cannot directly push to GitHub when v2ray/Clash is running on Windows without "Allow LAN" enabled. The proxy is at `127.0.0.1:10808` on Windows but WSL's `127.0.0.1` is a different host.

## Working Method: Windows PowerShell + Git Proxy

```bash
# Copy repo to Windows-accessible path
cp -r ~/project-repo "/mnt/c/Users/$USER/Desktop/pv-push"

# Push via Windows git with proxy
powershell.exe -Command "
cd 'C:\Users\YOU\Desktop\pv-push'
git remote add origin https://github.com/USER/REPO.git 2>&1
git config --global http.proxy http://127.0.0.1:10808
git config --global https.proxy http://127.0.0.1:10808
git push origin master --force
git config --global --unset http.proxy
git config --global --unset https.proxy
"

# Clean up
rm -rf "/mnt/c/Users/$USER/Desktop/pv-push"
```

## Why This Works

- Windows git at `127.0.0.1:10808` reaches v2ray directly (same host)
- WSL `127.0.0.1` is WSL itself, not Windows — can't reach the proxy
- Copying to `/mnt/c/` makes it a Windows-local path
- Proxy config is set then immediately unset (global, not permanent)

## Alternative: Enable "Allow LAN" in v2ray

If v2ray has "Allow LAN" enabled, WSL can reach the proxy at the Windows host IP:

```bash
WIN_IP=$(ip route show default | awk '{print $3}')
git -c http.proxy=http://$WIN_IP:10808 push origin master
```

## Pitfalls

1. **Forget to unset global proxy** — affects all git repos. Always unset after push.
2. **Remote already exists** — `git remote add` fails on second run. Use `git remote set-url` or check first.
3. **`/tmp/` not accessible from Windows** — always use `/mnt/c/Users/...` for Windows-accessible paths.
4. **`gh` CLI from WSL** — install in WSL (`~/.local/bin/gh`) or use Windows `powershell.exe -Command "gh ..."`.
