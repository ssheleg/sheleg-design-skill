import { Card, ProgressBar } from '@sheleg-design/workbench';

export const Backfill = () => (
  <ProgressBar label="Backfill shard 3" value={412} max={1200} />
);

export const Finished = () => (
  <ProgressBar label="Nightly rebuild" value={100} tone="ok" />
);

export const StoppedPartWay = () => (
  <ProgressBar label="Export to warehouse" value={38} tone="danger" />
);

export const ShardStack = () => (
  <Card title="Backfill · orders.v3" meta="run 8842">
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      <ProgressBar label="Shard 1" value={1200} max={1200} tone="ok" />
      <ProgressBar label="Shard 2" value={1200} max={1200} tone="ok" />
      <ProgressBar label="Shard 3" value={412} max={1200} />
      <ProgressBar label="Shard 4" value={0} max={1200} tone="warn" />
    </div>
  </Card>
);
