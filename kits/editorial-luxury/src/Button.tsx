import type { ReactNode } from 'react';

export interface ButtonProps {
  /** `primary` is the sage fill — the one action the page is asking for. */
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
      className={['el-btn', `el-btn--${variant}`, `el-btn--${size}`, className]
        .filter(Boolean)
        .join(' ')}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
