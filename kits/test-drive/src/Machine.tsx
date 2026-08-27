import type { ReactNode } from 'react';

export interface MachineProps {
  /** An optional chrome-bar title, e.g. the command being demonstrated. */
  title?: string;
  children: ReactNode;
  className?: string;
}

export function Machine({ title, children, className }: MachineProps) {
  return (
    <div className={['td-machine', className].filter(Boolean).join(' ')}>
      {title !== undefined && <div className="td-machine__title">{title}</div>}
      <div className="td-machine__body">{children}</div>
    </div>
  );
}

export interface CaretProps {
  className?: string;
}

/** The blinking terminal caret — legal inside Machine only. */
export function Caret({ className }: CaretProps) {
  return <span className={['td-caret', className].filter(Boolean).join(' ')} aria-hidden="true" />;
}
