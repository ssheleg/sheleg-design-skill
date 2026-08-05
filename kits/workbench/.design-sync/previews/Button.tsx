import { Button } from '@sheleg-design/workbench';

export const DeployPrimary = () => (
  <Button onClick={() => console.log('deploy')}>Deploy to production</Button>
);

export const ActionRow = () => (
  <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
    <Button onClick={() => console.log('deploy')}>Deploy to production</Button>
    <Button variant="secondary" onClick={() => console.log('diff')}>
      Review diff
    </Button>
    <Button variant="ghost" onClick={() => console.log('logs')}>
      Open logs
    </Button>
  </div>
);

export const Sizes = () => (
  <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
    <Button size="sm" variant="secondary">Retry shard</Button>
    <Button size="md" variant="secondary">Retry run</Button>
    <Button size="lg" variant="secondary">Retry pipeline</Button>
  </div>
);

export const DisabledUntilApproval = () => (
  <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
    <Button disabled>Merge schema change</Button>
    <Button variant="ghost" size="sm">Request approval</Button>
  </div>
);
