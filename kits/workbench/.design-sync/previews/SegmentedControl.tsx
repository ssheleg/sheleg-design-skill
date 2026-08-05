import { useState } from 'react';
import { Card, SegmentedControl, Stat } from '@sheleg-design/workbench';

export const TimeRange = () => {
  const [range, setRange] = useState('24h');
  return (
    <SegmentedControl
      label="Time range"
      options={[
        { value: '1h', label: '1h' },
        { value: '24h', label: '24h' },
        { value: '7d', label: '7d' },
        { value: '30d', label: '30d' },
      ]}
      value={range}
      onChange={setRange}
    />
  );
};

export const Environment = () => {
  const [env, setEnv] = useState('production');
  return (
    <SegmentedControl
      label="Environment"
      options={[
        { value: 'production', label: 'Production' },
        { value: 'staging', label: 'Staging' },
      ]}
      value={env}
      onChange={setEnv}
    />
  );
};

export const AboveAStat = () => {
  const [range, setRange] = useState('24h');
  const value = range === '1h' ? '104 ms' : range === '24h' ? '128 ms' : '141 ms';
  return (
    <Card title="p95 latency" meta="all regions">
      <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
        <SegmentedControl
          label="Time range"
          options={[
            { value: '1h', label: '1h' },
            { value: '24h', label: '24h' },
            { value: '7d', label: '7d' },
          ]}
          value={range}
          onChange={setRange}
        />
        <Stat value={value} label="p95 latency" source={`last ${range} · all regions`} />
      </div>
    </Card>
  );
};
