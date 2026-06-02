# WSL → GitHub Push via Windows Proxy

When WSL can't reach GitHub directly (no proxy configured in WSL), use Windows git with proxy.

## Pattern

```powershell
# 1. Copy repo to Windows-accessible path
# (WSL paths like /home/user/repo are NOT accessible to Windows git)

# 2. Configure git proxy in PowerShell
powershell.exe -Command "
git config --global http.proxy http://127.0.0.1:10808
git config --global https.proxy http://127.0.0.1:10808
"

# 3. Push from PowerShell
powershell.exe -Command "
cd 'C:\Users\YOU\Desktop\temp-repo'
git remote add origin https://github.com/USER/REPO.git
git push origin master
"

# 4. CLEAN UP global proxy (important!)
powershell.exe -Command "
git config --global --unset http.proxy
git config --global --unset https.proxy
"
```

## Why This Works

- v2ray/Clash runs on Windows, listening on 127.0.0.1:10808
- Windows git uses Windows proxy settings or explicit config
- WSL `127.0.0.1` ≠ Windows `127.0.0.1` (different network namespaces)

## Alternative: WSL Direct (if v2ray has "Allow LAN" enabled)

```bash
# Get Windows host IP
WIN_IP=$(ip route show default | awk '{print $3}')

# Push with proxy
cd ~/repo
git -c http.proxy=http://$WIN_IP:10808 push origin master
```

This requires v2ray/Clash to have "Allow LAN" (允许局域网连接) enabled.

## Pitfalls

1. **Always unset global proxy after push** — leaving `http.proxy` globally set breaks local/internal git operations.

2. **Copy to Windows path first** — Windows git can't handle `//wsl.localhost/...` paths reliably (dubious ownership errors). Copy to Desktop or use `wslpath -w`.

3. **Connection timeout** — If push hangs for 17+ seconds, proxy isn't running or port is wrong. Check `powershell.exe -Command "Get-Process v2ray*"`.

4. **gh CLI from WSL** — Install gh in WSL (`~/.local/bin/gh`) but authenticate via Windows `gh auth login`. The token is shared via Windows credential manager.
