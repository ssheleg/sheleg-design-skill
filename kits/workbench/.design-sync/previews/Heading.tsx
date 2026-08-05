import { Heading, Rule } from '@sheleg-design/workbench';

export const PageTitle = () => <Heading level={1}>Ingest pipeline</Heading>;

export const SectionTitle = () => <Heading level={2}>Recent runs</Heading>;

export const TypeRamp = () => (
  <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
    <Heading level={1}>Ingest pipeline</Heading>
    <Rule />
    <Heading level={2}>Recent runs</Heading>
    <Heading level={3}>Shard 3 · us-east-1</Heading>
  </div>
);
