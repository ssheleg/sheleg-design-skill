import type { ReactNode } from 'react';

export interface ButtonProps {
  /**
   * `primary` is the candy pill — the pack's one orange object. Exactly one
   * per view; a second is a second action competing for the same click.
   */
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
      className={['orch-btn', `orch-btn--${variant}`, `orch-btn--${size}`, className]
        .filter(Boolean)
        .join(' ')}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
