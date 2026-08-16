import type { ReactNode } from 'react';

export interface ButtonProps {
  /** `primary` is the accent fill — the pack allows one per view. */
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  onClick?: () => void;
  children: ReactNode;
  className?: string;
}

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
      className={['nt-btn', `nt-btn--${variant}`, `nt-btn--${size}`, className]
        .filter(Boolean)
        .join(' ')}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
