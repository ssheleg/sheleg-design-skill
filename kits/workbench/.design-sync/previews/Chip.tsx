import { Chip } from '@sheleg-design/workbench';

export const RegionChip = () => <Chip>us-east-1</Chip>;

export const VersionUnderReview = () => (
  <div style={{ display: 'flex', gap: 6, alignItems: 'center' }}>
    <Chip tone="accent">v2.14.0</Chip>
    <Chip>v2.13.4</Chip>
    <Chip>v2.13.3</Chip>
  </div>
);

export const FilterRail = () => (
  <div style={{ display: 'flex', gap: 6, alignItems: 'center', flexWrap: 'wrap' }}>
    <Chip selected>Failed only</Chip>
    <Chip>Last 24h</Chip>
    <Chip>us-east-1</Chip>
    <Chip>shard 3</Chip>
  </div>
);

export const MetadataRow = () => (
  <div style={{ display: 'flex', gap: 6, alignItems: 'center' }}>
    <Chip>run 8842</Chip>
    <Chip>1 204 883 rows</Chip>
    <Chip>11m 04s</Chip>
  </div>
);
