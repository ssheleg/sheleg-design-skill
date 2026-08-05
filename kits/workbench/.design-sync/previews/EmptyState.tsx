import { Card, EmptyState } from '@sheleg-design/workbench';

export const PausedScheduler = () => (
  <EmptyState
    message="No runs in the last 24 hours. The scheduler was paused on 3 Aug."
    actionLabel="Resume scheduler"
    onAction={() => console.log('resume')}
  />
);

export const FilteredToNothing = () => (
  <EmptyState
    message="No failed runs match this filter — every run in the last 7 days finished."
    actionLabel="Clear filter"
    onAction={() => console.log('clear')}
  />
);

export const NothingToDo = () => (
  <EmptyState message="This pipeline has no downstream consumers yet." />
);

export const InsideACard = () => (
  <Card title="Incidents" meta="last 30 days">
    <EmptyState
      message="No incidents opened since 6 Jul. The last one closed after 41 minutes."
      actionLabel="Open incident history"
      onAction={() => console.log('history')}
    />
  </Card>
);
