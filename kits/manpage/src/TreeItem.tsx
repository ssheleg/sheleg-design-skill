import type { ReactNode } from 'react';

export interface TreeItemProps {
  children: ReactNode;
  /** `last` draws └, `branch` draws ├ for an item with siblings below it. */
  kind?: 'last' | 'branch';
  className?: string;
}

export function TreeItem({ children, kind = 'last', className }: TreeItemProps) {
  return (
    <div className={['mp-tree', className].filter(Boolean).join(' ')}>
      <span className="mp-tree__glyph" aria-hidden="true">
        {kind === 'last' ? '└' : '├'}
      </span>
      <span className="mp-tree__body">{children}</span>
    </div>
  );
}
