#!/usr/bin/env bash
# run-tests.sh — runs every HUnit test file in the current directory.
#
# Usage:
#   ./run-tests.sh                 # runs everything matching Tests*.hs
#   ./run-tests.sh 'Test*.hs'      # custom glob (quote it!)
#
# Each test file is expected to have a `main` that calls
# runTestTTAndExit, which exits non-zero when a test fails.

set -uo pipefail

# Use -Wno-x-partial instead of -w to keep the useful warnings.
GHC_FLAGS=(-w -v0)

pattern="${1:-Tests*.hs}"

shopt -s nullglob
files=($pattern)
shopt -u nullglob

if ((${#files[@]} == 0)); then
    echo "No files matched: $pattern" >&2
    exit 1
fi

passed=0
failed=0
failed_files=()

for f in "${files[@]}"; do
    echo "──────────────────────────────────────────"
    echo "  $f"
    echo "──────────────────────────────────────────"

    if runghc "${GHC_FLAGS[@]/#/--ghc-arg=}" "$f"; then
        passed=$((passed + 1))
    else
        failed=$((failed + 1))
        failed_files+=("$f")
    fi
    echo
done

echo "=========================================="
echo "  Files passed: $passed   failed: $failed"
if ((failed > 0)); then
    printf '  Failing: %s\n' "${failed_files[*]}"
fi
echo "=========================================="

((failed == 0))