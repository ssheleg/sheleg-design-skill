---
category: Signature
---

Sourced authority as layout: named experts, each with their institution on a
second line and an optional role on a third. A claim without an attributed name
and a testimonial without a person attached to it are both bans in this pack, so
this is where the credibility of a health page is actually built — the
institution line is what keeps the section from reading as marketing.

The rail scrolls horizontally and snaps; it is swipeable on touch, which is the
mechanism. The pack's circular desktop nav buttons are an affordance over that
same scroll and stay with the pack's interaction layer rather than crossing into
the kit.

```tsx
<AuthorityRow
  label="Our medical and scientific advisors"
  people={[
    { id: 'ea', name: 'Dr. Elena Arriaga', institution: 'Stanford Medicine', role: 'Preventive cardiology' },
    { id: 'jo', name: 'Dr. Julius Okonkwo', institution: 'Mayo Clinic', role: 'Endocrinology' },
    { id: 'ms', name: 'Dr. Mira Shah', institution: 'UCSF Health', role: 'Diagnostic radiology' },
  ]}
/>
```
