import { Card, Heading, Rule } from '@sheleg-design/workbench';

export const Hairline = () => <Rule />;

export const Strong = () => <Rule tone="strong" />;

export const BetweenSections = () => (
  <div>
    <Heading level={2}>Recent runs</Heading>
    <p style={{ margin: '8px 0' }}>Five most recent executions of the ingest pipeline.</p>
    <Rule tone="strong" />
    <Heading level={2}>Schedule</Heading>
    <p style={{ margin: '8px 0' }}>Every 15 minutes, 02:00–23:45 UTC.</p>
  </div>
);

export const InsideACard = () => (
  <Card title="Deploy 4f2a91c" meta="us-east-1">
    <p style={{ margin: 0 }}>Rolled out to 3 of 8 regions.</p>
    <Rule />
    <p style={{ margin: 0 }}>Started 14:02 UTC by nadia@ from main.</p>
  </Card>
);
