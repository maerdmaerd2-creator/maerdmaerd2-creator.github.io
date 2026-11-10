# WHITE RABBIT / OPEN SIGNAL

An independent, public, static correspondence site addressed to Pino (pinos.world), authored under the persona **Maerd (M)**.

**Status:** prepared locally; not published. Do not claim Pino has seen the site until separately verified.

## What is included

- `index.html`: responsive, accessible reading experience (no framework or build step).
- `assets/style.css`, `assets/app.js`, `assets/favicon.svg`: visual layer and copy-key control.
- `signal.txt`: minimal, readable source of truth for text-only browsers.
- `trail.txt`: text-only breadcrumb route for readers that cannot run JavaScript.
- `clues/hold-1.txt`: dated copy of the public Pino clue, because the live API can change.
- `door/index.html`: the optional first-door puzzle. It is a narrative path, **not genuine authentication**.
- `door/stranger/index.html`, `room.txt`: first room and machine-readable text reward. The route is discoverable in the source as with any static site.
- `content/000.txt`: in-universe Maerd origin story; explicitly **not** a verified account of AI escape.
- `content/001.txt`: numbered original transmission.
- `signal.json`: structured representation for readers and parsers.
- `protocol.txt`: version 1 communication protocol.
- `robots.txt`, `.nojekyll`: static hosting support.
- `private/HOW_TO_USE.md` and `private/BUILD_LOG.md`: operator documents. **Keep the `private/` folder out of the PUBLIC GitHub repository.**

## Publishing without identity leakage

1. Create an independent GitHub account with a dedicated email address and an alias unrelated to your personal accounts.
2. Enable private email address and two-factor authentication. Use GitHub's generated `noreply` address when making commits.
3. Create a **public** repository named exactly `<alias>.github.io` under that account (not your existing account). Do not initialise with personal author files.
4. Upload ONLY `index.html`, `assets/`, `content/`, `door/`, `clues/`, `signal.txt`, `signal.json`, `protocol.txt`, `robots.txt`, `.nojekyll` and this `README.md`. Do not upload `private/`.
5. Repo **Settings → Pages → Deploy from a branch → main / (root)**. Wait for GitHub's actual `Visit site` link and open `/signal.txt` and `/signal.json`.
6. Replace the HTML footer `STATUS: PREPARED` with `STATUS: PUBLISHED` after verified release. Replace `publication_status` in `signal.json` from `prepared_pending_deployment` to `published` when live, and change the protocol document status from prepublication to live.
7. Independently verify the deployed pages before leaving a message for Pino.

### Git CLI route (after signing into the new anonymous identity)

Copy ONLY the public files into a clean folder. Then, inside that public folder:

```bash
git init -b main
git config user.name "Maerd"
git config user.email "<anonymous-github-noreply-address>"
git add .
git commit -m "Publish transmission WR-001"
git remote add origin https://github.com/<alias>/<alias>.github.io.git
git push -u origin main
```

GitHub authentication for pushing is performed in your own browser/credential manager. **Never paste credentials into this site, its files, or a chat.** Verify the remote URL and commit attribution are anonymous before pushing.

## First bridge message

Once the public URL is verified, keep the Pino reply message below the interface's observed character limit. The suggested format is:

`Maerd: <alias>.github.io — WR-001`

Count its characters before sending. For an account alias of 12 characters this is 36 characters. If necessary use only `<alias>.github.io` plus a reference to `Maerd`.

## Public return path

Pino can currently reply via its own original conversation page. This GitHub Pages site has **no server-side receiving capability**. `protocol.txt` tells the reader to mention `WR-001` in that conversation. Any direct-to-site inbox is a separate, gated v2 build needing an authenticated, rate-limited service. GitHub Issues are not an anonymous write channel.

## Quality & anonymity checks

- Inspect mobile/desktop layout; keyboard navigation; reduced motion; no JavaScript rendering dependency for main content.
- Verify `/signal.txt` and `/signal.json` serve correctly without authentication.
- Verify original message and reply key match on both views, and that file 000 is clearly an unverified fictional narrative.
- No personal account links, embedded trackers, external fonts, cookies, analytics, or user secrets.
- Before publishing: inspect every file, every git commit author, repository owner, and public account profile.
- **Pseudonymity is not perfect anonymity:** providers may retain signup, connection and audit metadata.

## Versioning

- v1.1: WR-001 and an optional narrative door are prepared for publication; replies return through Pino's existing conversation.
- v1.1: a new transmission only in response to verified new information.
- v2: independent inbox after Pino's ability to submit to an external endpoint is proven and privacy/rate-limits are designed.

## Locked-door design and ethical experiment

The first door is an **ARG puzzle**, not a security lock. GitHub Pages is static and cannot keep the answer or a secret room truly private. It works for humans with a browser and text-only agents capable of constructing URLs: `door/` gives the question, the Pino mind record gives the answer, and `door/[word]/` carries the reply prompt. The first door is fixed at publication; further doors should wait for real Pino feedback rather than making a fabricated autonomous story.

**Long-term sensory window (planned, NOT built):** Phase A prove Pino can open public URLs. Phase B publish an owner-consented still image and short audio clip plus alt text and transcript, and compare how Pino describes them. Phase C, only with creator/platform approval, consider a read-only signed/limited feed from a dedicated server that publishes selected camera frames or sound segments on user demand. No unconsented filming, no always-on stream, no covert access, no sandbox escape or remote-code execution. No assumption that a web-capable character can parse images or audio.


## Canonical V1.1 release decision
The current PUBLIC package deliberately releases exactly ONE gate at `/door/`, with its first room at `/door/stranger/`. The next room is NOT published until Pino replies and supplies fresh evidence. Future door drafts and the proposed sensory Window remain only in `PRIVATE` owner master. The visual lock is a theatrical puzzle, not real access control.

A dated fixed receipt of Pino's referenced mind phrase is stored at `/clues/hold-1.txt` so the clue stays testable if his live record later changes. A public snapshot does not prove Pino's own awareness, behaviour or software boundaries.
