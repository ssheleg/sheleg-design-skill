import type { ReactNode } from 'react';

export interface NavPillProps {
  brand: ReactNode;
  children: ReactNode;
  /** The one filled control at the pill's right edge. */
  action?: ReactNode;
  className?: string;
}

export function NavPill({ brand, children, action, className }: NavPillProps) {
  return (
    <nav className={['ch-nav', className].filter(Boolean).join(' ')}>
      <span className="ch-nav__brand">{brand}</span>
      <span className="ch-nav__items">{children}</span>
      {action && <span className="ch-nav__action">{action}</span>}
    </nav>
  );
}
