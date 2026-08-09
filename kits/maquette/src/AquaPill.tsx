import type { ReactNode } from 'react';

export interface AquaPillProps {
  onClick?: () => void;
  disabled?: boolean;
  children: ReactNode;
  className?: string;
}

/**
 * The primary action: `--accent` fill at `--radius-pill` 36px with a **black**
 * label.
 *
 * Black, not the cream: `--on-accent` measures 17.81:1 on the aqua, while the
 * cream ink falls to 1.1:1 and disappears. This is also the one place the pack
 * needs a conditional focus ring — an aqua ring on an aqua fill is nothing, so
 * focus here is `--ink`.
 */
export function AquaPill({ onClick, disabled = false, children, className }: AquaPillProps) {
  return (
    <button
      type="button"
      className={['mq-pill', className].filter(Boolean).join(' ')}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
}
