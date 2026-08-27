import type { ReactNode } from 'react';

export interface NavBarProps {
  brand: ReactNode;
  /** The link row — replaced by the consumer's toggle below 48rem. */
  children?: ReactNode;
  /** The trailing control, e.g. a quiet lit button. */
  actions?: ReactNode;
  className?: string;
}

export function NavBar({ brand, children, actions, className }: NavBarProps) {
  return (
    <header className={['td-nav', className].filter(Boolean).join(' ')}>
      <span className="td-nav__brand">{brand}</span>
      {children !== undefined && <nav className="td-nav__links">{children}</nav>}
      {actions !== undefined && <span className="td-nav__actions">{actions}</span>}
    </header>
  );
}
