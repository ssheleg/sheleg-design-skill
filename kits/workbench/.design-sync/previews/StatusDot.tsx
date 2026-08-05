import { Card, StatusDot } from '@sheleg-design/workbench';

export const Running = () => (
  <StatusDot status="running" label="Backfilling shard 3 of 12" />
);

export const EveryState = () => (
  <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
    <StatusDot status="running" label="Backfilling shard 3 of 12" />
    <StatusDot status="ok" label="Finished in 11m 04s" />
    <StatusDot status="warn" label="Waiting on schema approval" />
    <StatusDot status="danger" label="Failed — connection refused" />
    <StatusDot status="idle" label="Paused since 3 Aug" />
  </div>
);

export const DotOnly = () => (
  <div style={{ display: 'flex', gap: 12, alignItems: 'center' }}>
    <StatusDot status="ok" />
    <StatusDot status="running" />
    <StatusDot status="danger" />
  </div>
);

export const InACardHeader = () => (
  <Card title="Ingest pipeline" meta="run 8842 · 14:02 UTC">
    <StatusDot status="warn" label="Waiting on schema approval — 6m" />
  </Card>
);
