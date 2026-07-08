**Checkout latency incident — Exec Summary**

This document describes the checkout latency incident that occurred on Tuesday. As you know, we have been monitoring checkout performance closely, and it's worth noting that in order to understand what happened we need to walk through the timeline in detail.

The incident began when an engineer deployed a cache configuration change. Basically, the change bypassed the pricing cache. As previously mentioned, this happened under load. To reiterate, the cache was the problem. We then investigated for some time before identifying the cause, at which point we reverted the change and monitored recovery, and everything eventually returned to normal after a while.
