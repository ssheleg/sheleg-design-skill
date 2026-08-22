import type { ReactNode } from 'react';

export interface ButtonProps {
  /** `primary` is the accent fill — at most one per view. */
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  onClick?: () => void;
  children: ReactNode;
  className?: string;
}

/** In this pack `primary` is a WASH and a 1.5px rim, not a fill — the reference
 *  never fills its accent, because white on `--accent` is 1.97:1. */
export function Button({
  variant = 'secondary',
  size = 'md',
  disabled = false,
  onClick,
  children,
  className,
}: ButtonProps) {
  return (
    <button
      type="button"
      className={['pb-btn', `pb-btn--${variant}`, `pb-btn--${size}`, className].filter(Boolean).join(' ')}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
