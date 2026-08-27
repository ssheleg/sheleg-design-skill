# Style-pack index

Load this file only when selecting or authoring a visual system. The pack file,
not this index, is authoritative for tokens, components, responsive behavior,
motion and bans.

## Defaults

- Product UI with no stronger signal: [workbench](./styles/workbench.md).
- Marketing page with no stronger signal: [showroom](./styles/showroom.md).
- Presentation or board deck: [briefing-room](./styles/briefing-room.md).
- Cinematic systems or infrastructure page: [instrument-console](./styles/instrument-console.md).

**Six of the thirty-seven are on the core contract.
The other thirty-one answer all four widened sections.** A pack marked **core contract** leaves component
states, hero, responsive rules and the signature element open. Generate its kit
before building components.

## Catalogue

| Pack | Register | Good fit |
|---|---|---|
| [`instrument-console`](./styles/instrument-console.md) | near-black aerospace console | technical systems and infrastructure · **core contract** |
| [`editorial-luxury`](./styles/editorial-luxury.md) | cream and espresso | editorial, research, premium B2B · **core contract** |
| [`workbench`](./styles/workbench.md) | quiet light/dark UI | dashboards, admin, internal tools · (standalone) · **core contract** |
| [`briefing-room`](./styles/briefing-room.md) | dark 16:9 deck | investor and board presentations · (standalone) · **core contract** |
| [`atrium`](./styles/atrium.md) | cream daylight | consumer health and high-trust DTC |
| [`babylove`](./styles/babylove.md) | white with orange | SEO SaaS, long time-to-value, disconnected states |
| [`patchbay`](./styles/patchbay.md) | black with mint-cyan | engines, buses, pipelines, OSS front doors |
| [`nameplate`](./styles/nameplate.md) | cool slab with coral | press, certification and third-party trust · (standalone) |
| [`rimlight`](./styles/rimlight.md) | white with blue light | studios, services and case studies · (standalone) |
| [`onionskin`](./styles/onionskin.md) | white working sheet | developer and AI infrastructure · (standalone) |
| [`deskmate`](./styles/deskmate.md) | warm beige with a dusk bleed | AI coworkers and chat-native agents · (standalone) |
| [`test-drive`](./styles/test-drive.md) | warm paper with one coral | self-serve SaaS proven by the live product · (standalone) |
| [`outrank`](./styles/outrank.md) | white with violet | one brand across marketing and product |
| [`orchard`](./styles/orchard.md) | warm oat slabs | friendly biotech and wellness · **core contract** |
| [`field-notes`](./styles/field-notes.md) | ruled green paper | auditable open-source developer tools · (standalone) |
| [`showroom`](./styles/showroom.md) | white gallery | product-led companies selling the app |
| [`blueprint`](./styles/blueprint.md) | white technical stock | vector, storage and query infrastructure |
| [`prism`](./styles/prism.md) | iridescent hard edge | command-first OSS infrastructure |
| [`maquette`](./styles/maquette.md) | near-black table | enterprise data infrastructure |
| [`cyclorama`](./styles/cyclorama.md) | looping pastel field | applied-AI consultancies |
| [`scoreboard`](./styles/scoreboard.md) | warm paper | growth, ads and accumulating metrics |
| [`datasheet`](./styles/datasheet.md) | off-white specification | fraud, identity and device intelligence |
| [`manpage`](./styles/manpage.md) | cream manual | APIs, SDKs, CLIs and MCP servers |
| [`pigeonhole`](./styles/pigeonhole.md) | filed white field | inbox, ticket and CRM triage |
| [`roster`](./styles/roster.md) | faint square grid | platforms sold through who uses them |
| [`ora`](./styles/ora.md) | warm coal | machine verdicts, audits and protocol traces · (standalone) |
| [`tenor`](./styles/tenor.md) | warm management paper | agent operations and autonomous back office · (standalone) |
| [`ledger`](./styles/ledger.md) | cream ruled console | analysts, BI and warehouse agents · (standalone) |
| [`paperclip`](./styles/paperclip.md) | monochrome coal | orchestrators, schedulers and job runners · (standalone) |
| [`awning`](./styles/awning.md) | white commerce forecourt | storefront, payroll and billing platforms · (standalone) · **core contract** |
| [`router`](./styles/router.md) | pale console with hairlines | dashboard, billing and inventory surfaces · (standalone) |
| [`daylight`](./styles/daylight.md) | bright portal with one shadow | client onboarding and service portals · (standalone) |
| [`notation`](./styles/notation.md) | restrained technical hairlines | OSS, docs and developer workspaces · (standalone) |
| [`almanac`](./styles/almanac.md) | oatmeal editorial paper | manifestos and category-defining pages · (standalone) |
| [`vitrine`](./styles/vitrine.md) | serif trust display | evaluated B2B, security and compliance · (standalone) |
| [`proscenium`](./styles/proscenium.md) | white demo sequence | product tours and launch pages · (standalone) |
| [`bulletin`](./styles/bulletin.md) | cheerful outlined bands | broad SMB and agency platforms · (standalone) |

## Selection protocol

When candidates overlap, mount both on the same populated page behind
`?variant=<pack>`; change only the token layer. Pick from real content and
density, record the decision, then remove the comparison harness. A placeholder
route cannot expose the difference.

The pack wins on values. The calibration dials in `SKILL.md` win on amount.
Neither may invent a token the chosen pack does not define.
