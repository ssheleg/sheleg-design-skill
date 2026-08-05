import { Stat } from '@sheleg-design/workbench';

export const LatencyStat = () => (
  <Stat value="128 ms" label="p95 latency" source="last 24h · all regions" />
);

export const StatRow = () => (
  <div style={{ display: 'grid', gap: 12, gridTemplateColumns: 'repeat(4, minmax(0, 1fr))' }}>
    <Stat value="128 ms" label="p95 latency" source="last 24h · all regions" />
    <Stat value="99.94%" label="Availability" source="30d rolling · SLO 99.9%" />
    <Stat value="3" label="Open incidents" source="pagerduty · live" />
    <Stat value="1 204 883" label="Rows ingested" source="run 8842 · so far" />
  </div>
);

export const StatWithoutSource = () => (
  <Stat value="8" label="Queued runs" />
);
