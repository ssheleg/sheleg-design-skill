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

/**
 * Three buttons with three geometries, because the pack measures three. The
 * primary is a pill in ink that moves `opacity` and nothing else; the secondary
 * is a hairline block; the ghost is the pack's hero button and inverts inside
 * `.fn-hero` without any prop of its own.
 */
export function Button({
  variant = 'primary',
  size = 'md',
  disabled = false,
  onClick,
  children,
  className,
}: ButtonProps) {
  return (
    <button
      type="button"
      className={['fn-btn', `fn-btn--${variant}`, `fn-btn--${size}`, className]
        .filter(Boolean)
        .join(' ')}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
