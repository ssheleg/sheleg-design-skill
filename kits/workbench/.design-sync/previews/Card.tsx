import { Button, Card, Chip, Rule, StatusDot } from '@sheleg-design/workbench';

export const RunCard = () => (
  <Card title="Ingest pipeline" meta="run 8842 · 14:02 UTC">
    <StatusDot status="running" label="Backfilling shard 3 of 12" />
  </Card>
);

export const CardWithRule = () => (
  <Card title="Deploy 4f2a91c" meta="us-east-1">
    <p style={{ margin: 0 }}>Rolled out to 3 of 8 regions. No error-rate change.</p>
    <Rule />
    <p style={{ margin: 0 }}>Started 14:02 UTC by nadia@ from main.</p>
  </Card>
);

export const CardWithActions = () => (
  <Card title="Schema change · orders.v3" meta="proposed 2 days ago">
    <p style={{ margin: '0 0 12px' }}>
      Adds <code>fulfilment_channel</code> and drops the unused{' '}
      <code>legacy_ref</code> column. Two downstream jobs read this table.
    </p>
    <div style={{ display: 'flex', gap: 8 }}>
      <Button size="sm">Approve</Button>
      <Button size="sm" variant="secondary">Request changes</Button>
    </div>
  </Card>
);

export const CardGrid = () => (
  <div style={{ display: 'grid', gap: 12, gridTemplateColumns: 'repeat(2, minmax(0, 1fr))' }}>
    <Card title="Ingest pipeline" meta="run 8842">
      <StatusDot status="running" label="Backfilling shard 3 of 12" />
    </Card>
    <Card title="Nightly rebuild" meta="run 8841">
      <StatusDot status="ok" label="Finished in 11m 04s" />
    </Card>
    <Card title="Warehouse export" meta="run 8839">
      <StatusDot status="danger" label="Failed — connection refused" />
    </Card>
    <Card title="Retention sweep" meta="scheduled 02:00 UTC">
      <Chip>paused</Chip>
    </Card>
  </div>
);
