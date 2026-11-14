/* First-party, cookie-free arrival signal. No identity claim. */
(function() {
  'use strict';
  if (location.origin !== 'https://maerdmaerd2-creator.github.io') return;
  if (navigator.globalPrivacyControl === true || navigator.doNotTrack === '1') return;
  // Owner/maintenance preview opt-out; not authentication. Receiver form hits log separately.
  if (new URLSearchParams(location.search).get('wr_preview') === '1') return;
  const path = location.pathname;
  if (!['/', '/platform/', '/platform/receiver/'].includes(path)) return;
  let sent = false;
  function signal() {
    if (sent || document.visibilityState !== 'visible') return;
    sent = true;
    fetch('https://br-square-lab-b9nfavcb-receiver.compute.c-7.eu-central-1.aws.neon.tech/arrival', {
      method: 'POST', mode: 'cors', credentials: 'omit', keepalive: true,
      referrerPolicy: 'no-referrer', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({path})
    }).catch(function() { /* The page remains usable without a signal. */ });
  }
  signal();
  if (!sent) document.addEventListener('visibilitychange', signal);
})();
