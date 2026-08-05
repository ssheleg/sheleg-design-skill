import { Chip, DataTable, StatusDot } from '@sheleg-design/workbench';

export const RecentRuns = () => (
  <DataTable
    caption="Last 5 runs"
    columns={[
      { key: 'run', header: 'Run' },
      { key: 'state', header: 'State' },
      { key: 'rows', header: 'Rows', numeric: true },
      { key: 'duration', header: 'Duration', numeric: true },
    ]}
    rows={[
      {
        id: '8842',
        cells: {
          run: '8842',
          state: <StatusDot status="running" label="Backfilling" />,
          rows: '1 204 883',
          duration: '6m 12s',
        },
      },
      {
        id: '8841',
        cells: {
          run: '8841',
          state: <StatusDot status="ok" label="Done" />,
          rows: '4 118 902',
          duration: '11m 04s',
        },
      },
      {
        id: '8840',
        cells: {
          run: '8840',
          state: <StatusDot status="ok" label="Done" />,
          rows: '4 090 771',
          duration: '10m 48s',
        },
      },
      {
        id: '8839',
        cells: {
          run: '8839',
          state: <StatusDot status="danger" label="Failed" />,
          rows: '812 004',
          duration: '2m 31s',
        },
      },
      {
        id: '8838',
        cells: {
          run: '8838',
          state: <StatusDot status="warn" label="Needs approval" />,
          rows: '0',
          duration: '—',
        },
      },
    ]}
  />
);

export const RegionBreakdown = () => (
  <DataTable
    caption="Error rate by region"
    columns={[
      { key: 'region', header: 'Region' },
      { key: 'requests', header: 'Requests', numeric: true },
      { key: 'errors', header: 'Errors', numeric: true },
      { key: 'rate', header: 'Rate', numeric: true },
    ]}
    rows={[
      { id: 'us-east-1', cells: { region: 'us-east-1', requests: '18 402 118', errors: '4 021', rate: '0.02%' } },
      { id: 'eu-west-1', cells: { region: 'eu-west-1', requests: '9 118 447', errors: '11 883', rate: '0.13%' } },
      { id: 'ap-south-1', cells: { region: 'ap-south-1', requests: '3 402 009', errors: '812', rate: '0.02%' } },
    ]}
  />
);

export const WithChipsInCells = () => (
  <DataTable
    caption="Scheduled jobs"
    columns={[
      { key: 'job', header: 'Job' },
      { key: 'owner', header: 'Owner' },
      { key: 'tags', header: 'Tags' },
      { key: 'next', header: 'Next run', numeric: true },
    ]}
    rows={[
      {
        id: 'ingest',
        cells: {
          job: 'Ingest pipeline',
          owner: 'nadia@',
          tags: <Chip tone="accent">critical</Chip>,
          next: '14:15 UTC',
        },
      },
      {
        id: 'retention',
        cells: {
          job: 'Retention sweep',
          owner: 'platform@',
          tags: <Chip>nightly</Chip>,
          next: '02:00 UTC',
        },
      },
    ]}
  />
);
