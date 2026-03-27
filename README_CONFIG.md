# OpenClaw Configuration Backup

This directory contains configuration backups and templates for your OpenClaw instance running on a VPS.

## Structure

```
.
├── openclaw.json.example        # Template config (safe to commit)
├── .env.example                  # VPS credentials template
├── workspace/                    # Agent workspace configs
│   ├── IDENTITY.md              # Agent identity/personality
│   ├── BOOTSTRAP.md             # Init scripts
│   ├── HEARTBEAT.md             # Health check config
│   ├── AGENTS.md                # Multi-agent setup
│   ├── TOOLS.md                 # Available tools
│   ├── SOUL.md                  # Agent soul/values
│   └── USER.md                  # User preferences
└── config/                      # Additional configs
    └── openclaw.json            # (ignored, contains credentials)
```

## Security

⚠️ **Important**: Never commit the actual `openclaw.json` or `.env` files to Git (they're in `.gitignore` for this reason).

Sensitive data includes:
- Slack bot tokens (`xoxb-...`)
- Slack app tokens (`xapp-...`)
- Gateway auth tokens
- API keys (Google, OpenAI)
- Device identities
- Pairing credentials

## Setup New Instance

1. **Copy templates**:
   ```bash
   cp .env.example .env
   cp openclaw.json.example openclaw.json
   ```

2. **Fill in credentials**:
   ```bash
   # Edit .env with your VPS credentials
   # Edit openclaw.json with your Slack tokens and gateway auth
   ```

3. **Sync to VPS**:
   ```bash
   # Copy to your remote instance
   scp openclaw.json root@YOUR_VPS:/root/.openclaw/
   scp workspace/*.md root@YOUR_VPS:/root/.openclaw/workspace/
   ```

4. **Restart gateway**:
   ```bash
   ssh root@YOUR_VPS "systemctl --user restart openclaw-gateway"
   ```

## Updating Config

After making changes to OpenClaw on the VPS:

```bash
# Pull latest config from VPS
scp root@YOUR_VPS:/root/.openclaw/openclaw.json ./openclaw.json.example  # (after sanitizing)

# Commit workspace changes
git add workspace/
git commit -m "Update agent workspace config"
```

## Restoring Config

To restore from this backup:

1. Check git history for your desired version
2. Manually merge changes or cherry-pick commits
3. Sync back to VPS as shown in "Setup New Instance" above

## Workspace Files Reference

| File | Purpose |
|------|---------|
| `IDENTITY.md` | Define agent name, personality, emoji |
| `BOOTSTRAP.md` | Initial setup and agent instructions |
| `HEARTBEAT.md` | Monitoring and health check settings |
| `AGENTS.md` | Multi-agent configuration and routing |
| `TOOLS.md` | Available tools and their permissions |
| `SOUL.md` | Agent values, principles, guardrails |
| `USER.md` | User-specific preferences and settings |

## Slack App Manifest

For reference, the Slack app manifest that powers this integration is in the OpenClaw docs.
See: `/usr/lib/node_modules/openclaw/docs/channels/slack.md` on your VPS.

## Commands

Common OpenClaw CLI commands:

```bash
# Check status
openclaw status
openclaw health
openclaw gateway probe

# Slack-specific
openclaw channels status --probe
openclaw pairing list --channel slack
openclaw pairing approve slack <code>

# View logs
openclaw logs --follow

# Config management
openclaw config get channels.slack
openclaw config validate
```

## Support

- OpenClaw Docs: https://docs.openclaw.ai
- Slack Integration: https://docs.openclaw.ai/channels/slack
- GitHub Issues: Report issues in the main repository
