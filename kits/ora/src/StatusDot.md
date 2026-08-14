---
category: Data
---

A 6px `--radius-pill` dot at the status colour, and its word. **The word is a required
prop**, and that is the pack's palette rule made into an API: in the light theme
`--good` is 2.13:1 and `--warn` 2.01:1 on paper, below the 3:1 non-text floor, so the
colour is reinforcement and the word is the message.

`live` is the only status that pulses. It means work is happening right now and it never
appears beside a finished state. Under reduced motion it holds at 90% opacity.

```tsx
<StatusDot status="live" label="running" />
<StatusDot status="danger" label="blocked" />
```
