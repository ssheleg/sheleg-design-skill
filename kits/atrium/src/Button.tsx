import type { ReactNode } from 'react';

export interface ButtonProps {
  /**
   * The pill triad, and there is no fourth: `primary` is the solid accent,
   * `secondary` the accent-outline on the field, `ghost` the beige pill that
   * sits on photography.
   */
  variant?: 'primary' | 'secondary' | 'ghost';
  /** `md` is the pack's pill (12px 25px). `sm`/`lg` rescale it, nothing else. */
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
      className={['at-btn', `at-btn--${variant}`, `at-btn--${size}`, className]
        .filter(Boolean)
        .join(' ')}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
