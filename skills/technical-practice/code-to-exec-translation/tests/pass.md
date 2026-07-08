**Image upload change — for VP Product**

**So what:** Photo-heavy pages now load about 3× faster on mobile, which should cut the drop-off we see on the listing flow.

**What changed:** We moved image processing off the page-load path, so pages no longer wait for images to be resized before showing.

**Why it matters:** Mobile listing pages were our slowest, and slow pages lose customers. Early numbers show median load dropping from 2.4s to 0.8s. Revenue impact is not yet measured — Unknown until we have a week of data.

**Status & risk:** Shipped to 20% of traffic behind a flag. Watching error rates and image-quality complaints before full rollout next week.

**Needed from you:** Nothing — FYI. Will confirm the conversion impact once we have a week of data.
