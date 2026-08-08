import type { ReactNode } from 'react';

export interface ButtonProps {
  /** `primary` is the ink fill; `secondary` the hairline outline. At most one
   *  accent fill per view — see the `tone` note below. */
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  onClick?: () => void;
  children: ReactNode;
  className?: string;
}

/**
 * `primary` is an `--ink` fill whose label is `--on-ink` — the *field* colour,
 * not white. That is the pack's one counter-intuitive button rule and it is
 * measured: the reference tints its button labels with the page.
 *
 * Press is instant on purpose. Hover scales to 1.02 over `--dur-base`; the
 * active state drops to 0.98 with **zero** duration, so the button answers the
 * finger rather than easing after it.
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
      className={['cy-btn', `cy-btn--${variant}`, `cy-btn--${size}`, className]
        .filter(Boolean)
        .join(' ')}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
