import type { ReactNode } from 'react';

export interface PlateProps {
  /** The borrowed name — a publication, an authority, an issuer. One per plate. */
  name: ReactNode;
  /** Where the name points. A plate with no href is still a plate, not a button. */
  href?: string;
  /** `issued` is the plate you were given; `pending` is one you have not earned yet. */
  state?: 'issued' | 'pending';
  className?: string;
}

export function Plate({ name, href, state = 'issued', className }: PlateProps) {
  const cls = ['np-plate', `np-plate--${state}`, className].filter(Boolean).join(' ');
  if (href === undefined) {
    return <span className={cls}>{name}</span>;
  }
  return (
    <a className={cls} href={href} rel="noopener noreferrer">
      {name}
    </a>
  );
}
