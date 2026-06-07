# WSL Cross-Boundary Development Patterns

> Patterns for working across WSL ↔ Windows boundary. Discovered during project-vault development.

## Obsidian Symlink from WSL

**❌ `ln -sf` does NOT work.** WSL symlinks are Linux-native. Windows apps (including Obsidian) cannot follow them. Error: `EACCES: permission denied, lstat`

**✅ Use Windows `mklink /J` (directory junction):**

```bash
# From WSL terminal
powershell.exe -Command "cmd /c mklink /J 'C:\Users\YOU\Documents\Obsidian Vault\Projects\项目名' 'C:\Users\YOU\project\docs\vault'"
```

**Why junction, not symlink:**
- `mklink /D` (symlink) — requires admin privileges
- `mklink /J` (junction) — no admin required, transparent to Windows

**Prerequisite:** Project MUST be on Windows volume (`/mnt/c/` or `/mnt/d/`). WSL-only paths (`/home/user/`) are invisible to Windows.

## Git Push from WSL to GitHub

When v2ray proxy is on Windows but not accepting LAN connections, WSL can't reach GitHub directly. Solution:

```bash
# Copy repo to Windows-accessible path
cp -r ~/project-vault /mnt/c/Users/guoku/Desktop/pv-push

# Push via PowerShell with git proxy
powershell.exe -Command "
cd 'C:\Users\guoku\Desktop\pv-push'
git config --global http.proxy http://127.0.0.1:10808
git config --global https.proxy http://127.0.0.1:10808
git push origin master --force
git config --global --unset http.proxy
git config --global --unset https.proxy
"

# Clean up
rm -rf /mnt/c/Users/guoku/Desktop/pv-push
```

**Alternative (auth token in URL):**
```powershell
$token = gh auth token
$url = "https://gunqiuwang:$token@github.com/gunqiuwang/project-vault.git"
git push $url master --force
```

## Path Detection Pattern

```bash
# Check if project is on Windows volume
if echo "$PROJECT_ROOT" | grep -qE "^/mnt/[cd]/"; then
  ON_WINDOWS_VOLUME=true
fi

# Check if running in WSL
if grep -qiE "(microsoft|wsl)" /proc/version 2>/dev/null; then
  IS_WSL=true
fi

# Convert WSL path to Windows path
WIN_PATH=$(wslpath -w "$WSL_PATH" 2>/dev/null || echo "$WSL_PATH" | sed 's|/mnt/c/|C:\\|;s|/mnt/d/|D:\\|;s|/|\\|g')
```

## cmd.exe UNC Path Warning

When WSL CWD is a UNC path (`\\wsl.localhost\...`), `cmd.exe` warns "UNC paths are not supported. Defaulting to Windows directory." This is cosmetic — the command still executes. Safe to ignore.

## Windows Host IP from WSL

```bash
WIN_IP=$(ip route show default | awk '{print $3}')
# Usually 172.27.x.x (WSL2 virtual network)
```

Note: This is the WSL virtual adapter IP, not the physical network IP. Proxy on `127.0.0.1` in Windows is NOT accessible from WSL via this IP unless "Allow LAN" is enabled in the proxy.
