import type { ReactNode } from 'react';

export interface PlanCardProps {
  name: string;
  price: ReactNode;
  cadence?: string;
  features: string[];
  /** At most ONE plan per row is featured, and it is featured by fill, not by hue. */
  featured?: boolean;
  action: ReactNode;
  className?: string;
}

export function PlanCard({
  name,
  price,
  cadence,
  features,
  featured = false,
  action,
  className,
}: PlanCardProps) {
  return (
    <div
      className={['aw-plan', featured ? 'aw-plan--featured' : '', className]
        .filter(Boolean)
        .join(' ')}
    >
      <span className="aw-plan__name">{name}</span>
      <span className="aw-plan__price">{price}</span>
      {cadence ? <span className="aw-plan__cadence">{cadence}</span> : null}
      <ul className="aw-plan__features">
        {features.map((f) => (
          <li key={f}>{f}</li>
        ))}
      </ul>
      <div className="aw-plan__action">{action}</div>
    </div>
  );
}
