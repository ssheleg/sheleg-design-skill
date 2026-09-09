import { forwardRef } from 'react';
import type { ButtonHTMLAttributes, ReactNode } from 'react';

export interface ButtonProps
  extends Omit<ButtonHTMLAttributes<HTMLButtonElement>, 'className'> {
  /** `primary` is the pack's default fill — at most one accent action per view. */
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  children: ReactNode;
  className?: string;
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(function Button(
  { variant = 'primary', size = 'md', className, type, children, ...rest },
  ref,
) {
  return (
    <button
      ref={ref}
      // default is `button`, but an explicit caller `type` (submit, reset) wins —
      // a design default must never silently erase a prop the caller set.
      type={type ?? 'button'}
      className={['mq-btn', `mq-btn--${variant}`, `mq-btn--${size}`, className]
        .filter(Boolean)
        .join(' ')}
      // native + ARIA + state pass through: aria-label for icon-only buttons,
      // aria-controls / aria-expanded for trigger controls, disabled, and onClick
      // with its real event. The spine forwards, it does not swallow.
      {...rest}
    >
      {children}
    </button>
  );
});
