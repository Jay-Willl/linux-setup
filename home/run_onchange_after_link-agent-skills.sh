#!/bin/sh
set -e

CANONICAL="$HOME/.config/agents/skills"
mkdir -p "$CANONICAL"

link_skills() {
    [ -d "$1" ] || return 0
    ln -sfn "$CANONICAL" "$1/skills"
}

link_skills "$HOME/.config/opencode"
link_skills "$HOME/.claude"
link_skills "$HOME/.kimi-code"
