import type { ReactNode } from 'react';

export interface NavSlabProps {
  /** The wordmark or product name at the leading edge. */
  brand: ReactNode;
  children: ReactNode;
  /** The one control the slab carries on its trailing edge. */
  action?: ReactNode;
  className?: string;
}

export function NavSlab({ brand, children, action, className }: NavSlabProps) {
  return (
    <header className={['dm-slab', className].filter(Boolean).join(' ')}>
      <div className="dm-slab__brand">{brand}</div>
      <nav className="dm-slab__nav">{children}</nav>
      {action !== undefined && <div className="dm-slab__action">{action}</div>}
    </header>
  );
}
