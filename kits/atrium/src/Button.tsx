import { forwardRef } from 'react';
import type { ButtonHTMLAttributes, ReactNode } from 'react';

export interface ButtonProps
  extends Omit<ButtonHTMLAttributes<HTMLButtonElement>, 'className'> {
  /**
   * The pill triad, and there is no fourth: `primary` is the solid accent,
   * `secondary` the accent-outline on the field, `ghost` the beige pill that
   * sits on photography.
   */
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
      className={['at-btn', `at-btn--${variant}`, `at-btn--${size}`, className]
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
